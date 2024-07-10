import psutil
import time

def kill_process_by_name(process_name):
    """Kill process by its name."""
    for proc in psutil.process_iter(['pid', 'name']):
        # Check if process name matches
        if proc.info['name'].lower() == process_name.lower():
            try:
                proc.kill()
                print(f"Process {process_name} with PID {proc.info['pid']} has been killed.")
            except psutil.NoSuchProcess:
                print(f"Process {process_name} does not exist.")
            except psutil.AccessDenied:
                print(f"Permission denied to kill {process_name}.")

def main():
    process_name = input("Enter the process name to kill (default 'RSIGuard.exe'): ") or 'RSIGuard.exe'
    interval = input("Enter the check interval in seconds (default 21600): ") or 21600
    
    interval = int(interval)  # Ensure the interval is an integer
    
    while True:
        kill_process_by_name(process_name)
        time.sleep(interval)

if __name__ == "__main__":
    main()