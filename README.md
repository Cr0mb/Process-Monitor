# Process Monitor with Auto-Restart and Alarm

This Python script monitors a specific process on your system. If the process is not running, it will play an alarm sound and attempt to restart the process. The script allows you to select a process by its name or PID, and optionally provide the path to the executable for automatic restarting.

## Features
- List all running processes sorted alphabetically by name.
- Select a process to monitor by either name or PID.
- Check if the selected process is running.
- Play an alarm sound if the process stops.
- Optionally restart the process if its executable path is provided.

## Requirements
- Python 3.x
- `psutil` library (for managing system processes)
- `winsound` module (only available on Windows for alarm sound)
```
pip install psutil
```

