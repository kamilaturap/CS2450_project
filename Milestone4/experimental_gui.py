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


def to_hex(value: int) -> str:

    hex_value = hex(value)[2:]

    if len(hex_value) == 1:
        hex_value = '0' + hex_value
    return hex_value


def update_primary_color(screen, hex_value: str, red_value: int, green_value: int, blue_value: int) -> None:

    current_color = screen.controller.primary_color
    current_red = int(current_color[1:3], 16)
    current_green = int(current_color[3:5], 16)
    current_blue = int(current_color[5:7], 16)

    if hex_value == "":
        red_value = to_hex(red_value)
        green_value = to_hex(green_value)
        blue_value = to_hex(blue_value)

        hex_value = red_value + green_value + blue_value

        screen.hex_text_box_0.insert(0, hex_value)

    elif current_red != red_value or current_green != green_value or current_blue != blue_value:

        red_value = to_hex(red_value)
        green_value = to_hex(green_value)
        blue_value = to_hex(blue_value)

        hex_value = red_value + green_value + blue_value

        screen.hex_text_box_0.delete(0, "end")
        screen.hex_text_box_0.insert(0, hex_value)

    else:
        red_value = int(hex_value[0:2], 16)
        green_value = int(hex_value[2:4], 16)
        blue_value = int(hex_value[4:6], 16)

        screen.red_slider_0.set(red_value)
        screen.green_slider_0.set(green_value)
        screen.blue_slider_0.set(blue_value)

    hex_value = "#" + hex_value

    screen.controller.primary_color = hex_value

    screen.configure(bg=hex_value)
    screen.subframe_0.configure(bg=hex_value)
    screen.subframe_1.configure(bg=hex_value)
    screen.subframe_1_0.configure(bg=hex_value)
    screen.subframe_1_1.configure(bg=hex_value)
    screen.subframe_2.configure(bg=hex_value)
    screen.subframe_2_0.configure(bg=hex_value)
    screen.subframe_2_1.configure(bg=hex_value)
    screen.subframe_3.configure(bg=hex_value)

    screen.rgb_label.configure(bg=hex_value)
    screen.primary_label.configure(bg=hex_value)
    screen.red_label_0.configure(bg=hex_value)
    screen.green_label_0.configure(bg=hex_value)
    screen.blue_label_0.configure(bg=hex_value)
    screen.hex_label_0.configure(bg=hex_value)
    screen.secondary_label.configure(bg=hex_value)
    screen.red_label_1.configure(bg=hex_value)
    screen.green_label_1.configure(bg=hex_value)
    screen.blue_label_1.configure(bg=hex_value)
    screen.hex_label_1.configure(bg=hex_value)

    screen.red_slider_0.configure(bg=hex_value)
    screen.green_slider_0.configure(bg=hex_value)
    screen.blue_slider_0.configure(bg=hex_value)
    screen.red_slider_1.configure(bg=hex_value)
    screen.green_slider_1.configure(bg=hex_value)
    screen.blue_slider_1.configure(bg=hex_value)

    screen.apply_button_0.configure(fg=hex_value)
    screen.apply_button_1.configure(fg=hex_value)
    screen.done_button.configure(fg=hex_value)


def update_secondary_color(screen, hex_value: str, red_value: int, green_value: int, blue_value: int) -> None:

    current_color = screen.controller.secondary_color
    current_red = int(current_color[1:3], 16)
    current_green = int(current_color[3:5], 16)
    current_blue = int(current_color[5:7], 16)

    if hex_value == "":
        red_value = to_hex(red_value)
        green_value = to_hex(green_value)
        blue_value = to_hex(blue_value)

        hex_value = red_value + green_value + blue_value

        screen.hex_text_box_1.insert(0, hex_value)

    elif current_red != red_value or current_green != green_value or current_blue != blue_value:

        red_value = to_hex(red_value)
        green_value = to_hex(green_value)
        blue_value = to_hex(blue_value)

        hex_value = red_value + green_value + blue_value

        screen.hex_text_box_1.delete(0, "end")
        screen.hex_text_box_1.insert(0, hex_value)

    else:
        red_value = int(hex_value[0:2], 16)
        green_value = int(hex_value[2:4], 16)
        blue_value = int(hex_value[4:6], 16)

        screen.red_slider_1.set(red_value)
        screen.green_slider_1.set(green_value)
        screen.blue_slider_1.set(blue_value)

    hex_value = "#" + hex_value

    screen.controller.secondary_color = hex_value

    screen.rgb_label.configure(fg=hex_value)
    screen.primary_label.configure(fg=hex_value)
    screen.red_label_0.configure(fg=hex_value)
    screen.green_label_0.configure(fg=hex_value)
    screen.blue_label_0.configure(fg=hex_value)
    screen.hex_label_0.configure(fg=hex_value)
    screen.secondary_label.configure(fg=hex_value)
    screen.red_label_1.configure(fg=hex_value)
    screen.green_label_1.configure(fg=hex_value)
    screen.blue_label_1.configure(fg=hex_value)
    screen.hex_label_1.configure(fg=hex_value)

    screen.red_slider_0.configure(fg=hex_value)
    screen.green_slider_0.configure(fg=hex_value)
    screen.blue_slider_0.configure(fg=hex_value)
    screen.red_slider_1.configure(fg=hex_value)
    screen.green_slider_1.configure(fg=hex_value)
    screen.blue_slider_1.configure(fg=hex_value)

    screen.apply_button_0.configure(bg=hex_value)
    screen.apply_button_1.configure(bg=hex_value)
    screen.done_button.configure(bg=hex_value)


class SettingsScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.configure(bg=controller.primary_color, padx=0, pady=0)

        self.subframe_0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_0.configure(bg=controller.primary_color)
        self.subframe_0.pack()

        self.rgb_label = tk.Label(self.subframe_0, text="Color Configuration: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.rgb_label.configure(font=FONT_TUPLE_REG)
        self.rgb_label.grid(row=0, column=0)

        self.subframe_1 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_1.configure(bg=controller.primary_color)
        self.subframe_1.pack()

        self.primary_label = tk.Label(self.subframe_1, text="Primary Color: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.primary_label.configure(font=FONT_TUPLE_REG)
        self.primary_label.grid(row=0, column=0)

        self.subframe_1_0 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_0.configure(bg=controller.primary_color)
        self.subframe_1_0.grid(row=1, column=0)

        self.red_label_0 = tk.Label(self.subframe_1_0, text="Red Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.red_label_0.configure(font=FONT_TUPLE_REG)
        self.red_label_0.grid(row=0, column=0)

        self.red_slider_0 = tk.Scale(self.subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        self.red_slider_0.set(int(self.controller.primary_color[1:3], 16))
        self.red_slider_0.grid(row=0, column=1)

        self.green_label_0 = tk.Label(self.subframe_1_0, text="Green Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.green_label_0.configure(font=FONT_TUPLE_REG)
        self.green_label_0.grid(row=1, column=0)

        self.green_slider_0 = tk.Scale(self.subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        self.green_slider_0.set(int(self.controller.primary_color[3:5], 16))
        self.green_slider_0.grid(row=1, column=1)

        self.blue_label_0 = tk.Label(self.subframe_1_0, text="Blue Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.blue_label_0.configure(font=FONT_TUPLE_REG)
        self.blue_label_0.grid(row=2, column=0)

        self.blue_slider_0 = tk.Scale(self.subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        self.blue_slider_0.set(int(self.controller.primary_color[5:7], 16))
        self.blue_slider_0.grid(row=2, column=1)

        self.subframe_1_1 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_1.configure(bg=controller.primary_color)
        self.subframe_1_1.grid(row=2, column=0)

        self.hex_label_0 = tk.Label(self.subframe_1_1, text="Hex Value: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.hex_label_0.configure(font=FONT_TUPLE_REG)
        self.hex_label_0.grid(row=0, column=0)

        self.hex_text_box_0 = tk.Entry(self.subframe_1_1, width=10, bg=BG_COLOR_GREY_DEFAULT)
        self.hex_text_box_0.insert(0, self.controller.primary_color[1:])
        self.hex_text_box_0.grid(row=0, column=1)

        self.apply_button_0 = tk.Button(self.subframe_1_1, text="Apply", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=10, command=lambda: update_primary_color(self, str(self.hex_text_box_0.get()), int(self.red_slider_0.get()), int(self.green_slider_0.get()), int(self.blue_slider_0.get())))
        self.apply_button_0.configure(font=FONT_TUPLE_REG)
        self.apply_button_0.grid(row=0, column=2, padx=10)

        self.subframe_2 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_2.configure(bg=controller.primary_color)
        self.subframe_2.pack()

        self.secondary_label = tk.Label(self.subframe_2, text="Secondary Color: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.secondary_label.configure(font=FONT_TUPLE_REG)
        self.secondary_label.grid(row=0, column=0)

        self.subframe_2_0 = tk.LabelFrame(self.subframe_2, padx=5, pady=5, bd=0)
        self.subframe_2_0.configure(bg=controller.primary_color)
        self.subframe_2_0.grid(row=1, column=0)

        self.red_label_1 = tk.Label(self.subframe_2_0, text="Red Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.red_label_1.configure(font=FONT_TUPLE_REG)
        self.red_label_1.grid(row=0, column=0)

        self.red_slider_1 = tk.Scale(self.subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        self.red_slider_1.set(int(self.controller.secondary_color[1:3], 16))
        self.red_slider_1.grid(row=0, column=1)

        self.green_label_1 = tk.Label(self.subframe_2_0, text="Green Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.green_label_1.configure(font=FONT_TUPLE_REG)
        self.green_label_1.grid(row=1, column=0)

        self.green_slider_1 = tk.Scale(self.subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        self.green_slider_1.set(int(self.controller.secondary_color[3:5], 16))
        self.green_slider_1.grid(row=1, column=1)

        self.blue_label_1 = tk.Label(self.subframe_2_0, text="Blue Value:", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.blue_label_1.configure(font=FONT_TUPLE_REG)
        self.blue_label_1.grid(row=2, column=0)

        self.blue_slider_1 = tk.Scale(self.subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT, orient=tk.HORIZONTAL)
        self.blue_slider_1.set(int(self.controller.secondary_color[5:7], 16))
        self.blue_slider_1.grid(row=2, column=1)

        self.subframe_2_1 = tk.LabelFrame(self.subframe_2, padx=5, pady=5, bd=0)
        self.subframe_2_1.configure(bg=controller.primary_color)
        self.subframe_2_1.grid(row=2, column=0)

        self.hex_label_1 = tk.Label(self.subframe_2_1, text="Hex Value: ", bg=controller.primary_color, fg=BG_COLOR_GREY_DEFAULT)
        self.hex_label_1.configure(font=FONT_TUPLE_REG)
        self.hex_label_1.grid(row=0, column=0)

        self.hex_text_box_1 = tk.Entry(self.subframe_2_1, width=10, bg=BG_COLOR_GREY_DEFAULT)
        self.hex_text_box_1.insert(0, self.controller.secondary_color[1:])
        self.hex_text_box_1.grid(row=0, column=1)

        self.apply_button_1 = tk.Button(self.subframe_2_1, text="Apply", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=10, command=lambda: update_secondary_color(self, str(self.hex_text_box_1.get()), int(self.red_slider_1.get()), int(self.green_slider_1.get()), int(self.blue_slider_1.get())))
        self.apply_button_1.configure(font=FONT_TUPLE_REG)
        self.apply_button_1.grid(row=0, column=2, padx=10)

        self.subframe_3 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_3.configure(bg=controller.primary_color)
        self.subframe_3.pack()

        self.done_button = tk.Button(self.subframe_3, text="Done", bg=BG_COLOR_GREY_DEFAULT, fg=controller.primary_color, width=25, command=lambda: controller.show_frame("MainScreen"))
        self.done_button.configure(font=FONT_TUPLE_REG)
        self.done_button.grid(row=0, column=0, pady=10)


if __name__ == "__main__":
    app = UVSimGui()
    app.mainloop()
    