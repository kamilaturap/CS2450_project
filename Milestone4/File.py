import tkinter as tk


class FileManager:
    """Separates file functionality from RunProgram. So far not sure if this class is needed."""
    def __init__(self):
        pass

    def RunFile(self, prog, gui):
        text = gui.progField.get('1.0', tk.END)
        prog.readProgram(text)
