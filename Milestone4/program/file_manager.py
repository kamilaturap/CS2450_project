import tkinter as tk


class FileManager:
    """Separates file functionality from RunProgram. So far not sure if this class is needed."""

    def __init__(self):
        pass


    def RunFile(self, prog, gui):
        text = gui.frames["MainScreen"].text_area_program.get('1.0', tk.END)
        lst = text.split("\n")
        if len(lst) > 100:
            gui.invalid_input()
        else:
            prog.readProgram(text)
