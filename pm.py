import subprocess
import time
import psutil
import winsound

def list_processes():
    processes = {proc.pid: proc.info['name'] for proc in psutil.process_iter(['name']) if proc.info['name']}
    sorted_processes = dict(sorted(processes.items(), key=lambda item: item[1].lower())) 
    print("Running processes (sorted alphabetically):")
    for pid, name in sorted_processes.items():
        print(f"{pid}: {name}")
    return sorted_processes

def select_process():
    processes = list_processes()
    selection = input("\nEnter the name or PID of the process you want to monitor: ")

    for pid, name in processes.items():
        if selection == str(pid) or selection.lower() == name.lower():
            print(f"Selected process: {name} (PID: {pid})")
            return pid, name
    print("Process not found. Please try again.")
    return select_process()

def is_process_running(pid):
    return psutil.pid_exists(pid)

def start_process(path):
    try:
        subprocess.Popen([path])
        print("Process started successfully.")
    except Exception as e:
        print(f"Failed to start the process: {e}")

def play_alarm():
    for _ in range(5): 
        winsound.Beep(1000, 500)  
        time.sleep(0.1)

def main():
    pid, process_name = select_process()

    exe_path = input(f"Enter the full path to the executable for {process_name} (optional, press Enter to skip): ")
    print("Process Monitor is running. Press Ctrl+C to exit.")

    while True:
        if not is_process_running(pid):
            print(f"{process_name} is not running. Playing alarm and attempting to restart it...")
            play_alarm()

            if exe_path:
                start_process(exe_path)
            else:
                print("No executable path provided. Cannot restart the process.")

        time.sleep(5)

if __name__ == "__main__":
    main()
