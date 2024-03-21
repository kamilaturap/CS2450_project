import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog as tkfile

from breezypythongui import EasyFrame
from Memory import *

BG_COLOR_GREEN_DEFAULT = "#275d38"
BG_COLOR_GREY_DEFAULT = "#e8e8e8"
BG_COLOR_WHITE_DEFAULT = "#FFFFFF"
BG_COLOR_BLACK_DEFAULT = "#000000"

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

        self.subframe_0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_0.configure(bg=controller.primary_color)
        self.subframe_0.pack()

        self.uvsim_label = tk.Label(self.subframe_0, text="UVSim", bg=controller.primary_color, fg=controller.secondary_color)
        self.uvsim_label.configure(font=FONT_TUPLE_TITLE)
        self.uvsim_label.grid(row=0, column=0)

        self.subframe_1 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_1.configure(bg=controller.primary_color)
        self.subframe_1.pack()

        self.subframe_1_0 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_0.configure(bg=controller.primary_color)
        self.subframe_1_0.grid(row=0, column=0)

        self.subframe_1_0_0 = tk.LabelFrame(self.subframe_1_0, padx=5, pady=5, bd=0)
        self.subframe_1_0_0.configure(bg=controller.primary_color)
        self.subframe_1_0_0.pack()

        self.import_button = tk.Button(self.subframe_1_0_0, text="Import .txt File", bg=controller.secondary_color, fg=controller.primary_color)
        self.import_button.configure(font=FONT_TUPLE_REG)
        self.import_button.grid(row=0, column=0, padx=5)

        self.selected_file_label = tk.Label(self.subframe_1_0_0, text="Selected File: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.selected_file_label.configure(font=FONT_TUPLE_REG)
        self.selected_file_label.grid(row=0, column=1, padx=5)

        self.subframe_1_0_1 = tk.LabelFrame(self.subframe_1_0, padx=5, pady=5, bd=0)
        self.subframe_1_0_1.configure(bg=controller.primary_color)
        self.subframe_1_0_1.pack()

        self.selected_file_text_box = tk.Entry(self.subframe_1_0_1, width=35, bg=controller.secondary_color, fg=BG_COLOR_BLACK_DEFAULT, font=FONT_TUPLE_TEXT)
        self.selected_file_text_box.grid(row=0, column=0, padx=5)

        self.subframe_1_1 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_1.configure(bg=controller.primary_color)
        self.subframe_1_1.grid(row=0, column=1)

        self.load_button = tk.Button(self.subframe_1_1, text="Load Selected Program", bg=controller.secondary_color, fg=controller.primary_color, width=25)
        self.load_button.configure(font=FONT_TUPLE_REG)
        self.load_button.grid(row=0, column=0, pady=5)

        self.save_button = tk.Button(self.subframe_1_1, text="Save Program Changes", bg=controller.secondary_color, fg=controller.primary_color, width=25)
        self.save_button.configure(font=FONT_TUPLE_REG)
        self.save_button.grid(row=1, column=0, pady=5)

        self.subframe_1_2 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_2.configure(bg=controller.primary_color)
        self.subframe_1_2.grid(row=0, column=2)

        self.run_button = tk.Button(self.subframe_1_2, text="Run Program", bg=controller.secondary_color, fg=controller.primary_color, width=25)
        self.run_button.configure(font=FONT_TUPLE_REG)
        self.run_button.grid(row=1, column=0)

        self.subframe_2 = tk.LabelFrame(self, padx=0, pady=5, bd=0)
        self.subframe_2.configure(bg=controller.primary_color)
        self.subframe_2.pack()

        self.scroll_y = tk.Scrollbar(self.subframe_2)
        self.text_area_program = tk.Text(self.subframe_2, bg=BG_COLOR_WHITE_DEFAULT, fg=BG_COLOR_BLACK_DEFAULT, bd=5, font=FONT_TUPLE_TEXT, relief="ridge", yscrollcommand=self.scroll_y.set, width=88, height=10)
        self.text_area_program.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E, pady=10)
        self.scroll_y.grid(row=0, column=1, sticky=tk.N+tk.S, pady=10)

        self.subframe_3 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_3.configure(bg=controller.primary_color)
        self.subframe_3.pack()

        self.output_label = tk.Label(self.subframe_3, text="Output: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.output_label.configure(font=FONT_TUPLE_REG)
        self.output_label.grid(row=0, column=0)

        self.subframe_4 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_4.configure(bg=controller.primary_color)
        self.subframe_4.pack()

        self.scroll_y_2 = tk.Scrollbar(self.subframe_4)
        self.text_area_output = tk.Text(self.subframe_4, bg=BG_COLOR_WHITE_DEFAULT, fg=BG_COLOR_BLACK_DEFAULT, bd=5, font=FONT_TUPLE_TEXT, relief="ridge", yscrollcommand=self.scroll_y_2.set, width=88, height=10)
        self.text_area_output.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E, pady=10)
        self.scroll_y_2.grid(row=0, column=1, sticky=tk.N+tk.S, pady=10)

        self.subframe_5 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_5.configure(bg=controller.primary_color)
        self.subframe_5.pack()

        self.settings_button = tk.Button(self.subframe_5, text="Settings", bg=controller.secondary_color, fg=controller.primary_color, width=25, command=lambda: controller.show_frame("SettingsScreen"))
        self.settings_button.configure(font=FONT_TUPLE_REG)
        self.settings_button.grid(row=0, column=0)


class SettingsScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.configure(bg=controller.primary_color, padx=0, pady=0)

        self.subframe_0 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_0.configure(bg=controller.primary_color)
        self.subframe_0.pack()

        self.rgb_label = tk.Label(self.subframe_0, text="Color Configuration: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.rgb_label.configure(font=FONT_TUPLE_REG)
        self.rgb_label.grid(row=0, column=0)

        self.subframe_1 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_1.configure(bg=controller.primary_color)
        self.subframe_1.pack()

        self.primary_label = tk.Label(self.subframe_1, text="Primary Color: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.primary_label.configure(font=FONT_TUPLE_REG)
        self.primary_label.grid(row=0, column=0)

        self.subframe_1_0 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_0.configure(bg=controller.primary_color)
        self.subframe_1_0.grid(row=1, column=0)

        self.red_label_0 = tk.Label(self.subframe_1_0, text="Red Value:", bg=controller.primary_color, fg=controller.secondary_color)
        self.red_label_0.configure(font=FONT_TUPLE_REG)
        self.red_label_0.grid(row=0, column=0)

        self.red_slider_0 = tk.Scale(self.subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=controller.secondary_color, orient=tk.HORIZONTAL)
        self.red_slider_0.set(int(self.controller.primary_color[1:3], 16))
        self.red_slider_0.grid(row=0, column=1)

        self.green_label_0 = tk.Label(self.subframe_1_0, text="Green Value:", bg=controller.primary_color, fg=controller.secondary_color)
        self.green_label_0.configure(font=FONT_TUPLE_REG)
        self.green_label_0.grid(row=1, column=0)

        self.green_slider_0 = tk.Scale(self.subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=controller.secondary_color, orient=tk.HORIZONTAL)
        self.green_slider_0.set(int(self.controller.primary_color[3:5], 16))
        self.green_slider_0.grid(row=1, column=1)

        self.blue_label_0 = tk.Label(self.subframe_1_0, text="Blue Value:", bg=controller.primary_color, fg=controller.secondary_color)
        self.blue_label_0.configure(font=FONT_TUPLE_REG)
        self.blue_label_0.grid(row=2, column=0)

        self.blue_slider_0 = tk.Scale(self.subframe_1_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=controller.secondary_color, orient=tk.HORIZONTAL)
        self.blue_slider_0.set(int(self.controller.primary_color[5:7], 16))
        self.blue_slider_0.grid(row=2, column=1)

        self.subframe_1_1 = tk.LabelFrame(self.subframe_1, padx=5, pady=5, bd=0)
        self.subframe_1_1.configure(bg=controller.primary_color)
        self.subframe_1_1.grid(row=2, column=0)

        self.hex_label_0 = tk.Label(self.subframe_1_1, text="Hex Value: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.hex_label_0.configure(font=FONT_TUPLE_REG)
        self.hex_label_0.grid(row=0, column=0)

        self.hex_text_box_0 = tk.Entry(self.subframe_1_1, width=10, bg=controller.secondary_color, fg=BG_COLOR_BLACK_DEFAULT, font=FONT_TUPLE_TEXT)
        self.hex_text_box_0.insert(0, self.controller.primary_color[1:])
        self.hex_text_box_0.grid(row=0, column=1)

        self.apply_button_0 = tk.Button(self.subframe_1_1, text="Apply", bg=controller.secondary_color, fg=controller.primary_color, width=10, command=lambda: update_primary_color(self, str(self.hex_text_box_0.get()), int(self.red_slider_0.get()), int(self.green_slider_0.get()), int(self.blue_slider_0.get())))
        self.apply_button_0.configure(font=FONT_TUPLE_REG)
        self.apply_button_0.grid(row=0, column=2, padx=10)

        self.subframe_2 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_2.configure(bg=controller.primary_color)
        self.subframe_2.pack()

        self.secondary_label = tk.Label(self.subframe_2, text="Secondary Color: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.secondary_label.configure(font=FONT_TUPLE_REG)
        self.secondary_label.grid(row=0, column=0)

        self.subframe_2_0 = tk.LabelFrame(self.subframe_2, padx=5, pady=5, bd=0)
        self.subframe_2_0.configure(bg=controller.primary_color)
        self.subframe_2_0.grid(row=1, column=0)

        self.red_label_1 = tk.Label(self.subframe_2_0, text="Red Value:", bg=controller.primary_color, fg=controller.secondary_color)
        self.red_label_1.configure(font=FONT_TUPLE_REG)
        self.red_label_1.grid(row=0, column=0)

        self.red_slider_1 = tk.Scale(self.subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=controller.secondary_color, orient=tk.HORIZONTAL)
        self.red_slider_1.set(int(self.controller.secondary_color[1:3], 16))
        self.red_slider_1.grid(row=0, column=1)

        self.green_label_1 = tk.Label(self.subframe_2_0, text="Green Value:", bg=controller.primary_color, fg=controller.secondary_color)
        self.green_label_1.configure(font=FONT_TUPLE_REG)
        self.green_label_1.grid(row=1, column=0)

        self.green_slider_1 = tk.Scale(self.subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=controller.secondary_color, orient=tk.HORIZONTAL)
        self.green_slider_1.set(int(self.controller.secondary_color[3:5], 16))
        self.green_slider_1.grid(row=1, column=1)

        self.blue_label_1 = tk.Label(self.subframe_2_0, text="Blue Value:", bg=controller.primary_color, fg=controller.secondary_color)
        self.blue_label_1.configure(font=FONT_TUPLE_REG)
        self.blue_label_1.grid(row=2, column=0)

        self.blue_slider_1 = tk.Scale(self.subframe_2_0, from_=0, to=255, bd=0, highlightthickness=0, length=255, bg=controller.primary_color, fg=controller.secondary_color, orient=tk.HORIZONTAL)
        self.blue_slider_1.set(int(self.controller.secondary_color[5:7], 16))
        self.blue_slider_1.grid(row=2, column=1)

        self.subframe_2_1 = tk.LabelFrame(self.subframe_2, padx=5, pady=5, bd=0)
        self.subframe_2_1.configure(bg=controller.primary_color)
        self.subframe_2_1.grid(row=2, column=0)

        self.hex_label_1 = tk.Label(self.subframe_2_1, text="Hex Value: ", bg=controller.primary_color, fg=controller.secondary_color)
        self.hex_label_1.configure(font=FONT_TUPLE_REG)
        self.hex_label_1.grid(row=0, column=0)

        self.hex_text_box_1 = tk.Entry(self.subframe_2_1, width=10, bg=controller.secondary_color, fg=BG_COLOR_BLACK_DEFAULT, font=FONT_TUPLE_TEXT)
        self.hex_text_box_1.insert(0, self.controller.secondary_color[1:])
        self.hex_text_box_1.grid(row=0, column=1)

        self.apply_button_1 = tk.Button(self.subframe_2_1, text="Apply", bg=controller.secondary_color, fg=controller.primary_color, width=10, command=lambda: update_secondary_color(self, str(self.hex_text_box_1.get()), int(self.red_slider_1.get()), int(self.green_slider_1.get()), int(self.blue_slider_1.get())))
        self.apply_button_1.configure(font=FONT_TUPLE_REG)
        self.apply_button_1.grid(row=0, column=2, padx=10)

        self.subframe_3 = tk.LabelFrame(self, padx=5, pady=5, bd=0)
        self.subframe_3.configure(bg=controller.primary_color)
        self.subframe_3.pack()

        self.done_button = tk.Button(self.subframe_3, text="Done", bg=controller.secondary_color, fg=controller.primary_color, width=25, command=lambda: controller.show_frame("MainScreen"))
        self.done_button.configure(font=FONT_TUPLE_REG)
        self.done_button.grid(row=0, column=0, pady=10)


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

    screen.controller.frames["MainScreen"].configure(bg=hex_value)

    screen.controller.frames["MainScreen"].subframe_0.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_1.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_1_0.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_1_0_0.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_1_0_1.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_1_1.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_1_2.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_2.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_3.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_4.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].subframe_5.configure(bg=hex_value)

    screen.controller.frames["MainScreen"].uvsim_label.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].selected_file_label.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].output_label.configure(bg=hex_value)

    screen.controller.frames["MainScreen"].import_button.configure(fg=hex_value)
    screen.controller.frames["MainScreen"].save_button.configure(fg=hex_value)
    screen.controller.frames["MainScreen"].load_button.configure(fg=hex_value)
    screen.controller.frames["MainScreen"].run_button.configure(fg=hex_value)
    screen.controller.frames["MainScreen"].settings_button.configure(fg=hex_value)

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

    screen.controller.frames["MainScreen"].uvsim_label.configure(fg=hex_value)
    screen.controller.frames["MainScreen"].selected_file_label.configure(fg=hex_value)
    screen.controller.frames["MainScreen"].output_label.configure(fg=hex_value)

    screen.controller.frames["MainScreen"].import_button.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].load_button.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].save_button.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].run_button.configure(bg=hex_value)
    screen.controller.frames["MainScreen"].settings_button.configure(bg=hex_value)


def to_hex(value: int) -> str:
    hex_value = hex(value)[2:]

    if len(hex_value) == 1:
        hex_value = '0' + hex_value
    return hex_value


if __name__ == "__main__":
    app = UVSimGui()
    app.mainloop()
    