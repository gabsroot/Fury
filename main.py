from ui.menu import *
from cheat.overlay import *
from core.launch import *
from threading import Thread

# auto open cs2
launch = Launch()
launch.wait()

# dpg menu
app = Menu()
app.setup_registry()
app.create_viewport()

# overlay thread
overlay = Overlay()
thread = Thread(target=overlay.render, daemon=True)
thread.start()

app.run()
