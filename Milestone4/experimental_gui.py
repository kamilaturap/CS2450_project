import tkinter as tk
from tkinter import font as tkfont


BG_COLOR_GREEN_DEFAULT = "#275d38"
BG_COLOR_GREY_DEFAULT = "#e8e8e8"
BG_COLOR_WHITE_DEFAULT = "#FFFFFF"

FONT_TUPLE_TITLE = ("Vermin Vibes 2 Soft", 48)
FONT_TUPLE_REG = ("Cascadia Code Bold", 8)
FONT_TUPLE_TEXT = ("Cascadia Code", 8)


class UVSimGui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(name='SP DEMO - Gelica Rg"', size=18, weight="bold")
        self.title("UVSim")
        self.iconbitmap(default='assets/UVSim_icon.ico')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainScreen, SettingsScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.configure(bg=BG_COLOR_GREEN_DEFAULT, padx=0, pady=0)

        controller.title("UVSim")

        subframe0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe0.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe0.pack()

        uvsim_label = tk.Label(subframe0, text="UVSim", bg=BG_COLOR_GREEN_DEFAULT, fg=BG_COLOR_GREY_DEFAULT)
        uvsim_label.configure(font=FONT_TUPLE_TITLE)
        uvsim_label.grid(row=0, column=0)

        subframe1 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe1.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe1.pack()

        subframe1_0 = tk.LabelFrame(subframe1, padx=5, pady=5, bd=0)
        subframe1_0.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe1_0.grid(row=0, column=0)

        subframe1_0_0 = tk.LabelFrame(subframe1_0, padx=5, pady=5, bd=0)
        subframe1_0_0.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe1_0_0.pack()

        import_button = tk.Button(subframe1_0_0, text="Import .txt File", bg=BG_COLOR_GREY_DEFAULT, fg=BG_COLOR_GREEN_DEFAULT)
        import_button.configure(font=FONT_TUPLE_REG)
        import_button.grid(row=0, column=0, padx=5)

        selected_file_label = tk.Label(subframe1_0_0, text="Selected File: ", bg=BG_COLOR_GREEN_DEFAULT, fg=BG_COLOR_GREY_DEFAULT)
        selected_file_label.configure(font=FONT_TUPLE_REG)
        selected_file_label.grid(row=0, column=1, padx=5)

        subframe1_0_1 = tk.LabelFrame(subframe1_0, padx=5, pady=5, bd=0)
        subframe1_0_1.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe1_0_1.pack()

        selected_file_text_box = tk.Entry(subframe1_0_1, width=35, bg=BG_COLOR_GREY_DEFAULT)
        selected_file_text_box.grid(row=0, column=0, padx=5)

        subframe1_1 = tk.LabelFrame(subframe1, padx=5, pady=5, bd=0)
        subframe1_1.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe1_1.grid(row=0, column=1)

        load_button = tk.Button(subframe1_1, text="Load Selected Program", bg=BG_COLOR_GREY_DEFAULT, fg=BG_COLOR_GREEN_DEFAULT, width=25)
        load_button.configure(font=FONT_TUPLE_REG)
        load_button.grid(row=0, column=0, pady=5)

        save_button = tk.Button(subframe1_1, text="Save Program Changes", bg=BG_COLOR_GREY_DEFAULT, fg=BG_COLOR_GREEN_DEFAULT, width=25)
        save_button.configure(font=FONT_TUPLE_REG)
        save_button.grid(row=1, column=0, pady=5)

        subframe1_2 = tk.LabelFrame(subframe1, padx=5, pady=5, bd=0)
        subframe1_2.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe1_2.grid(row=0, column=2)

        run_button = tk.Button(subframe1_2, text="Run Program", bg=BG_COLOR_GREY_DEFAULT, fg=BG_COLOR_GREEN_DEFAULT, width=25)
        run_button.configure(font=FONT_TUPLE_REG)
        run_button.grid(row=1, column=0)

        subframe2 = tk.LabelFrame(self, padx=0, pady=5, bd=0)
        subframe2.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe2.pack()

        scroll_y = tk.Scrollbar(subframe2)
        text_area_program = tk.Text(subframe2, bg=BG_COLOR_WHITE_DEFAULT, bd=5, font=FONT_TUPLE_TEXT, relief="ridge", yscrollcommand=scroll_y.set, width=88, height=10)
        text_area_program.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E, pady=10)
        scroll_y.grid(row=0, column=1, sticky=tk.N+tk.S, pady=10)

        subframe3 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe3.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe3.pack()

        output_label = tk.Label(subframe3, text="Output: ", bg=BG_COLOR_GREEN_DEFAULT, fg=BG_COLOR_GREY_DEFAULT)
        output_label.configure(font=FONT_TUPLE_REG)
        output_label.grid(row=0, column=0)

        subframe4 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe4.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe4.pack()

        scroll_y_2 = tk.Scrollbar(subframe4)
        text_area_output = tk.Text(subframe4, bg=BG_COLOR_WHITE_DEFAULT, bd=5, font=FONT_TUPLE_TEXT, relief="ridge", yscrollcommand=scroll_y_2.set, width=88, height=10)
        text_area_output.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E, pady=10)
        scroll_y_2.grid(row=0, column=1, sticky=tk.N+tk.S, pady=10)

        subframe5 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe5.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe5.pack()

        settings_button = tk.Button(subframe5, text="Settings", bg=BG_COLOR_GREY_DEFAULT, fg=BG_COLOR_GREEN_DEFAULT, width=25, command=lambda: controller.show_frame("SettingsScreen"))
        settings_button.configure(font=FONT_TUPLE_REG)
        settings_button.grid(row=0, column=0,)


class SettingsScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.configure(bg=BG_COLOR_GREEN_DEFAULT, padx=0, pady=0)

        controller.title("UVSim")

        subframe0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe0.configure(bg=BG_COLOR_GREEN_DEFAULT)
        subframe0.pack()

        done_button = tk.Button(subframe0, text="Done", bg=BG_COLOR_GREY_DEFAULT, fg=BG_COLOR_GREEN_DEFAULT, width=25, command=lambda: controller.show_frame("MainScreen"))
        done_button.configure(font=FONT_TUPLE_REG)
        done_button.grid(row=0, column=0,)


if __name__ == "__main__":
    app = UVSimGui()
    app.mainloop()
    