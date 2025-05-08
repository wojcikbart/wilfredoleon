import os
import signal
import psutil

def kill_processes_by_name(process_names):
    """
    Kills all processes whose names match the provided list.
    
    :param process_names: List of process names to kill (e.g., ['chrome.exe', 'python.exe'])
    """
    for process in psutil.process_iter(['name', 'pid']):
        try:
            # Match process names (case insensitive)
            if process.info['name'] and process.info['name'].lower() in [name.lower() for name in process_names]:
                print(f"Killing process {process.info['name']} with PID {process.info['pid']}")
                os.kill(process.info['pid'], signal.SIGTERM)  # Send termination signal
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignore processes that no longer exist or cannot be accessed
            pass

if __name__ == "__main__":
    processes_to_kill = ['chrome.exe', 'python.exe']
    kill_processes_by_name(processes_to_kill)