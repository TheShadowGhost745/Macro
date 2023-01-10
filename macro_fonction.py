from pynput import mouse
import os

def get_coords():
    coords = []

    def on_click(x, y, button, pressed):
        if not button == mouse.Button.left:
            return False

        if pressed:
            print('{} at {}'.format('Click', (x, y)))
            coords.append((x, y))

    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()

    return coords


def create_directory():
    desktop = os.path.join(os.environ["HOMEPATH"], "OneDrive/Bureau")

    if "registered macro" not in os.listdir(desktop):
        os.mkdir(f"{desktop}/registered macro")
