from nicegui import ui
import webview
import tempfile
import signal
import os
import multiprocessing


# NOW I WANT DESIGN PAGE WITH LABEL AND BUTTON
ui.label("my nice gui").classes("font-xl")
ui.button("show button",on_click=lambda:ui.notify("hello guys"))
ui.button("show button")
ui.button("show button")
ui.button("show button")



def open_window(event):
	window = webview.create_window("My Nice",url="http://localhost:8080")
	# and CLOSE WINDOW CLOSING
	window.events.closing += event.set
	webview.start(storage_path=tempfile.mkdtemp())

shutdown = multiprocessing.Event()

# AND CHECK  every 1 second if program terminated
ui.timer(0.1,lambda:os.kill(os.getpid(os.getpid()),signal.SIGTERM) if shutdown.is_set() else None)

if __name__ == "__main__":
	multiprocessing.Process(target=open_window,args=(shutdown,), daemon=False).start()

ui.run(show=False)	
