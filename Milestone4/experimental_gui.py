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

        self.title_font = tkfont.Font(name="Vermin Vibes 2 Soft", size=18, weight="bold")
        self.title("UVSim")
        self.iconbitmap(default='assets/UVSim_icon.ico')
        
        self.primary_color = BG_COLOR_GREEN_DEFAULT
        self.secondary_color = BG_COLOR_GREY_DEFAULT

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainScreen, SettingsScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def update_primary_color(self, hex_value):
        self.primary_color = "#" + str(hex_value)
        self.__init__()


class MainScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.configure(bg=controller.primary_color, padx=0, pady=0)

        controller.title("UVSim")

        subframe_0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_0.configure(bg=controller.primary_color)
        subframe_0.pack()

        uvsim_label = tk.Label(subframe_0, text="UVSim", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        uvsim_label.configure(font=FONT_TUPLE_TITLE)
        uvsim_label.grid(row=0, column=0)

        subframe_1 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_1.configure(bg=controller.primary_color)
        subframe_1.pack()

        subframe_1_0 = tk.LabelFrame(subframe_1, padx=5, pady=5, bd=0)
        subframe_1_0.configure(bg=controller.primary_color)
        subframe_1_0.grid(row=0, column=0)

        subframe_1_1 = tk.LabelFrame(subframe_1_0, padx=5, pady=5, bd=0)
        subframe_1_1.configure(bg=controller.primary_color)
        subframe_1_1.pack()

        import_button = tk.Button(subframe_1_1, text="Import .txt File", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color)
        import_button.configure(font=FONT_TUPLE_REG)
        import_button.grid(row=0, column=0, padx=5)

        selected_file_label = tk.Label(subframe_1_1, text="Selected File: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        selected_file_label.configure(font=FONT_TUPLE_REG)
        selected_file_label.grid(row=0, column=1, padx=5)

        subframe_1_0_1 = tk.LabelFrame(subframe_1_0, padx=5, pady=5, bd=0)
        subframe_1_0_1.configure(bg=controller.primary_color)
        subframe_1_0_1.pack()

        selected_file_text_box = tk.Entry(subframe_1_0_1, width=35, bg=BG_COLOR_GREY_DEFAULT)
        selected_file_text_box.grid(row=0, column=0, padx=5)

        subframe_1_1 = tk.LabelFrame(subframe_1, padx=5, pady=5, bd=0)
        subframe_1_1.configure(bg=controller.primary_color)
        subframe_1_1.grid(row=0, column=1)

        load_button = tk.Button(subframe_1_1, text="Load Selected Program", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=25)
        load_button.configure(font=FONT_TUPLE_REG)
        load_button.grid(row=0, column=0, pady=5)

        save_button = tk.Button(subframe_1_1, text="Save Program Changes", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=25)
        save_button.configure(font=FONT_TUPLE_REG)
        save_button.grid(row=1, column=0, pady=5)

        subframe_1_2 = tk.LabelFrame(subframe_1, padx=5, pady=5, bd=0)
        subframe_1_2.configure(bg=controller.primary_color)
        subframe_1_2.grid(row=0, column=2)

        run_button = tk.Button(subframe_1_2, text="Run Program", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=25)
        run_button.configure(font=FONT_TUPLE_REG)
        run_button.grid(row=1, column=0)

        subframe_2 = tk.LabelFrame(self, padx=0, pady=5, bd=0)
        subframe_2.configure(bg=controller.primary_color)
        subframe_2.pack()

        scroll_y = tk.Scrollbar(subframe_2)
        text_area_program = tk.Text(subframe_2, bg=BG_COLOR_WHITE_DEFAULT, bd=5, font=FONT_TUPLE_TEXT, relief="ridge", yscrollcommand=scroll_y.set, width=88, height=10)
        text_area_program.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E, pady=10)
        scroll_y.grid(row=0, column=1, sticky=tk.N+tk.S, pady=10)

        subframe_3 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_3.configure(bg=controller.primary_color)
        subframe_3.pack()

        output_label = tk.Label(subframe_3, text="Output: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        output_label.configure(font=FONT_TUPLE_REG)
        output_label.grid(row=0, column=0)

        subframe_4 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_4.configure(bg=controller.primary_color)
        subframe_4.pack()

        scroll_y_2 = tk.Scrollbar(subframe_4)
        text_area_output = tk.Text(subframe_4, bg=BG_COLOR_WHITE_DEFAULT, bd=5, font=FONT_TUPLE_TEXT, relief="ridge", yscrollcommand=scroll_y_2.set, width=88, height=10)
        text_area_output.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E, pady=10)
        scroll_y_2.grid(row=0, column=1, sticky=tk.N+tk.S, pady=10)

        subframe_5 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_5.configure(bg=controller.primary_color)
        subframe_5.pack()

        settings_button = tk.Button(subframe_5, text="Settings", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=25, command=lambda: controller.show_frame("SettingsScreen"))
        settings_button.configure(font=FONT_TUPLE_REG)
        settings_button.grid(row=0, column=0,)


class SettingsScreen(tk.Frame):

    def update_primary_color(self, hex_value):
        self.controller.primary_color = "#" + str(hex_value)
        tk.Tk.update(self)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.configure(bg=controller.primary_color, padx=0, pady=0)

        subframe_0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_0.configure(bg=controller.primary_color)
        subframe_0.pack()

        rgb_label = tk.Label(subframe_0, text="Color Configuration: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        rgb_label.configure(font=FONT_TUPLE_REG)
        rgb_label.grid(row=0, column=0)

        subframe_1 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_1.configure(bg=controller.primary_color)
        subframe_1.pack()

        primary_label = tk.Label(subframe_1, text="Primary Color: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        primary_label.configure(font=FONT_TUPLE_REG)
        primary_label.grid(row=0, column=0)

        subframe_1_0 = tk.LabelFrame(subframe_1, padx=5, pady=5, bd=0)
        subframe_1_0.configure(bg=controller.primary_color)
        subframe_1_0.grid(row=1, column=0)

        red_label_0 = tk.Label(subframe_1_0, text="Red Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        red_label_0.configure(font=FONT_TUPLE_REG)
        red_label_0.grid(row=0, column=0)

        red_slider_0 = tk.Scale(subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        red_slider_0.grid(row=0, column=1)

        green_label_0 = tk.Label(subframe_1_0, text="Green Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        green_label_0.configure(font=FONT_TUPLE_REG)
        green_label_0.grid(row=1, column=0)

        green_slider_0 = tk.Scale(subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        green_slider_0.grid(row=1, column=1)

        blue_label_0 = tk.Label(subframe_1_0, text="Blue Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        blue_label_0.configure(font=FONT_TUPLE_REG)
        blue_label_0.grid(row=2, column=0)

        blue_slider_0 = tk.Scale(subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        blue_slider_0.grid(row=2, column=1)

        subframe_1_1 = tk.LabelFrame(subframe_1, padx=5, pady=5, bd=0)
        subframe_1_1.configure(bg=controller.primary_color)
        subframe_1_1.grid(row=2, column=0)

        hex_label_0 = tk.Label(subframe_1_1, text="Hex Value: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        hex_label_0.configure(font=FONT_TUPLE_REG)
        hex_label_0.grid(row=0, column=0)

        hex_text_box_0 = tk.Entry(subframe_1_1, width=10, bg=BG_COLOR_GREY_DEFAULT)
        hex_text_box_0.grid(row=0, column=1)

        apply_button_0 = tk.Button(subframe_1_1, text="Apply", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=10, command=lambda: self.update_primary_color(str(hex_text_box_0.get())))
        apply_button_0.configure(font=FONT_TUPLE_REG)
        apply_button_0.grid(row=0, column=2, padx=10)

        subframe_2 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_2.configure(bg=controller.primary_color)
        subframe_2.pack()

        secondary_label = tk.Label(subframe_2, text="Secondary Color: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        secondary_label.configure(font=FONT_TUPLE_REG)
        secondary_label.grid(row=0, column=0)

        subframe_2_0 = tk.LabelFrame(subframe_2, padx=5, pady=5, bd=0)
        subframe_2_0.configure(bg=controller.primary_color)
        subframe_2_0.grid(row=1, column=0)

        red_label_1 = tk.Label(subframe_2_0, text="Red Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        red_label_1.configure(font=FONT_TUPLE_REG)
        red_label_1.grid(row=0, column=0)

        red_slider_1 = tk.Scale(subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        red_slider_1.grid(row=0, column=1)

        green_label_1 = tk.Label(subframe_2_0, text="Green Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        green_label_1.configure(font=FONT_TUPLE_REG)
        green_label_1.grid(row=1, column=0)

        green_slider_1 = tk.Scale(subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        green_slider_1.grid(row=1, column=1)

        blue_label_1 = tk.Label(subframe_2_0, text="Blue Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        blue_label_1.configure(font=FONT_TUPLE_REG)
        blue_label_1.grid(row=2, column=0)

        blue_slider_1 = tk.Scale(subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        blue_slider_1.grid(row=2, column=1)

        subframe_2_1 = tk.LabelFrame(subframe_2, padx=5, pady=5, bd=0)
        subframe_2_1.configure(bg=controller.primary_color)
        subframe_2_1.grid(row=2, column=0)

        hex_label_1 = tk.Label(subframe_2_1, text="Hex Value: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        hex_label_1.configure(font=FONT_TUPLE_REG)
        hex_label_1.grid(row=0, column=0)

        hex_text_box_1 = tk.Entry(subframe_2_1, width=10, bg=BG_COLOR_GREY_DEFAULT)
        hex_text_box_1.grid(row=0, column=1)

        apply_button_1 = tk.Button(subframe_2_1, text="Apply", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=10, command=lambda: controller.show_frame("MainScreen"))
        apply_button_1.configure(font=FONT_TUPLE_REG)
        apply_button_1.grid(row=0, column=2, padx=10)

        subframe_x = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        subframe_x.configure(bg=controller.primary_color)
        subframe_x.pack()

        done_button = tk.Button(subframe_x, text="Done", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=25, command=lambda: controller.show_frame("MainScreen"))
        done_button.configure(font=FONT_TUPLE_REG)
        done_button.grid(row=0, column=0, pady=10)




if __name__ == "__main__":
    app = UVSimGui()
    app.mainloop()
    