import pystray
import PIL.Image
import main, alert_on, time

import threading

image = PIL.Image.open('f1.png')

def on_click(icon, item):
    if str(item) == "Open App":
        main.App()
    elif str(item) == "Exit":
        icon.stop()

def window_icon():
    icon = pystray.Icon("Stock Alerter", image, menu=pystray.Menu(
        pystray.MenuItem(text="Open App",action=on_click,default=True),
        pystray.MenuItem("Exit", on_click)
    ))

    icon.run()

def alerts():
    alert_on.background()


Thread1 = threading.Thread(target=window_icon)
Thread2 = threading.Thread(target=alerts)

Thread1.start()
Thread2.start()

Thread1.join()
Thread2.join()