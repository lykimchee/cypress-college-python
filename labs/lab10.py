import tkinter
import tkinter.messagebox


class ScoresGUI:

    def __init__(self):
        self._main_window = tkinter.Tk()
        self._main_window.title("Scores")

        self._value = tkinter.StringVar()

        self._top_frame = tkinter.Frame(self._main_window)
        self._middle_frame = tkinter.Frame(self._main_window)
        self._bottom_frame = tkinter.Frame(self._main_window)
        self._prompt_label1 = tkinter.Label(self._top_frame, text="Score #1: ")
        self._prompt_label2 = tkinter.Label(self._middle_frame, text="Score #2: ")
        self._prompt_label3 = tkinter.Label(self._bottom_frame, text="Score #3: ")

        self._entry1 = tkinter.Entry(self._top_frame, width=10)
        self._entry2 = tkinter.Entry(self._middle_frame, width=10)
        self._entry3 = tkinter.Entry(self._bottom_frame, width=10)

        self._average_button = tkinter.Button(self._main_window, text="Average", command=self.avg_function)

        self._result_label = tkinter.Label(self._main_window, textvariable=self._value)

        self._top_frame.pack()
        self._middle_frame.pack()
        self._bottom_frame.pack()
        self._prompt_label1.pack(padx=10, pady=5, side="left")
        self._prompt_label2.pack(padx=10, pady=5, side="left")
        self._prompt_label3.pack(padx=10, pady=5, side="left")
        self._entry1.pack(padx=(0, 20), pady=5, side="left")
        self._entry2.pack(padx=(0, 20), pady=5, side="left")
        self._entry3.pack(padx=(0, 20), pady=5, side="left")
        self._average_button.pack(pady=(0, 10))
        self._result_label.pack(pady=(0, 10))

        tkinter.mainloop()

    def avg_function(self):
        try:
            total = float(self._entry1.get()) + float(self._entry2.get()) + float(self._entry3.get())
            average = total / 3
            self._value.set("Average: " + str(average))
        except ValueError:
            self._value.set("")
            tkinter.messagebox.showerror("Error", "Enter a number!")
