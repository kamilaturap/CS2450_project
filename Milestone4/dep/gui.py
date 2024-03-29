from tkinter import filedialog

from breezypythongui import EasyFrame
import tkinter as tk


class Gui(EasyFrame, tk.Tk):
    def __init__(self, run):
        EasyFrame.__init__(self, title="UV Sim", background='#275D38')
        self.initial_text = None
        self.file_save = None
        self.file_path = None
        self.prog = None
        self.run = run
        self.text = ''
        self.inField = ''
        self.load = self.addTextField(text='', row=6, column=2)
        self.addButton(text='Load Registers', row=6, column=1, command=self.load_program)
        self.addButton(text='Run Program', row=6, column=3, command=self.run_program)
        self.addLabel(text='Program Registers:', row=3, column=1, background='#275D38', foreground='#A7A8AA')
        self.progField = self.addTextArea(text=self.text, row=4, column=1, columnspan=3, rowspan=2, width=5, height=20)
        self.addButton(text='  Close File  ', row=9, column=3, command=self.clear)
        self.addButton(text="  Open File  ", row=1, column=1, command=self.import_file)
        self.addLabel(text="Output: ", row=7, column=1, background='#275D38', foreground='#A7A8AA')
        self.output_text = self.addTextArea(text='', row=8, column=1, columnspan=3, width=5, height=5)
        self.addButton(text="  Save File  ", row=9, column=1, command=self.save_file, state='disabled')
        self.addLabel(text='', row=0, column=0, background='#275D38')
        self.addLabel(text='', row=10, column=4, background='#275D38')

    def run_program(self):
        """Runs the main program that will parse through the commands."""
        self.load.setText('')
        self.run.execute_program()

    def output(self, o):
        """
        One parameter: o, the text to be output.
        Function: prints out the text passed through o.
        """
        self.output_text.appendText(o + '\n')

    def popup(self):
        '''Function: small popup prompting the user for an input'''
        return self.prompterBox(title='input', promptString='enter signed four-digit word')

    def clear(self):
        '''Function: resets all text fields and all information in the memory class.'''
        self.load.setText('')
        self.progField.setText('')
        self.run.clear()
        self.output_text.setText('')

    def load_program(self):
        """Function: branches to RunProgram to load the file and lets the user know it has
        been loaded."""
        self.output_text.setText('')
        self.run.load_file()
        self.load.setText('Loaded')

    def enable_save(self):
        if self.progField.get('1.0', tk.END) != self.initial_text:
            self.addButton(text="Save Changes", row=7, column=2, command=self.save_file)

    def set_registers(self, content):
        """Function: loads the function calls from the text file into the program."""
        self.progField.appendText(tk.END, content)

    def invalid_input(self):
        self.messageBox(title="Error", message="The allotted commands exceeds 100 registers. Please reduce amount.")

    def import_file(self):
        """Function: first clears all registers then prompts the user to select a file from a directory.
        The function then opens the file and reads in the text to a text box to be edited.
        """
        self.clear()
        self.file_path = filedialog.askopenfilename(title="Select a file",
                                                    filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        with open(self.file_path, "r") as file:
            content = file.read()
            self.progField.delete('1.0', tk.END)
            self.progField.insert(tk.END, content)

        self.initial_text = self.progField.get('1.0', tk.END)

    def get_file(self):
        """Function: A getter for the file_path variable"""
        return self.file_path

    def save_file(self):
        """Function: Allows the user to save the edited contents of the text area to a new file."""
        self.file_save = filedialog.asksaveasfile(title="Select a file", mode='w', defaultextension='.txt')
        self.file_save.write(self.progField.get('1.0', tk.END))
        self.file_save.close()
     
