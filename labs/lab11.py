import tkinter
import tkinter.messagebox


class CarGUI:

    def __init__(self):
        self._main_window = tkinter.Tk()
        self._main_window.title("Miles Per Gallon")

        self._value = tkinter.StringVar()

        self._top_frame = tkinter.Frame(self._main_window)
        self._bottom_frame = tkinter.Frame(self._main_window)

        self._prompt_label1 = tkinter.Label(self._top_frame, text="Number of miles driven: ")
        self._prompt_label2 = tkinter.Label(self._bottom_frame, text="Gallons of gas used: ")

        self._entry1 = tkinter.Entry(self._top_frame, width=5)
        self._entry2 = tkinter.Entry(self._bottom_frame, width=5)

        self._calculate_button = tkinter.Button(self._main_window, text="Calculate", command=self.calc_function)

        self._output_label = tkinter.Label(self._main_window, textvariable=self._value)

        self._top_frame.pack()
        self._bottom_frame.pack()
        self._prompt_label1.pack(padx=2, pady=10, side="left")
        self._prompt_label2.pack(padx=13, pady=0, side="left")
        self._entry1.pack(padx=(0, 20), pady=10, side="left")
        self._entry2.pack(padx=(0, 20), pady=10, side="left")
        self._calculate_button.pack(pady=(0, 10))
        self._output_label.pack(pady=(0, 10))

        tkinter.mainloop()

    def calc_function(self):
        try:
            result = round(float(self._entry1.get()) / float(self._entry2.get()), 2)
            self._value.set("Your car travels at about " + str(result) + " miles per gallon.")
        except ValueError:
            self._value.set("")
            tkinter.messagebox.showerror("Error", "Please enter a valid input.")
