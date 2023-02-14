from customtkinter import CTk, CTkFont, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkComboBox, CTkTextbox
from decimal import Decimal

from Utils import operations, perform_operation
from CustomWidgets.ComboBox import ComboBox


class MainFrame(CTkFrame):
    def __init__(self, master: CTk, elements_font: CTkFont = None) -> None:
        super().__init__(master, fg_color="transparent")

        # Create elements
        self._info_label = CTkLabel(self, text="Enter 2 numbers and select an operation", font=elements_font)

        self._input_frame = CTkFrame(self, fg_color="transparent")  # Invisible element for grouping
        self._a_entry = CTkEntry(self._input_frame, placeholder_text="0", width=205, font=elements_font)
        self._operation_combobox = ComboBox(
            self._input_frame, values=operations, width=115, font=elements_font)
        self._b_entry = CTkEntry(self._input_frame, placeholder_text="0", width=205, font=elements_font)

        self._result_textbox = CTkTextbox(self, width=535, font=elements_font, state='disabled')  # readonly
        self._ok_button = CTkButton(self, text="OK", command=self._ok_button_click, font=elements_font)

        self._bind_elements()
        self._display_elements()

    def _bind_elements(self) -> None:
        """
        Bind the keyboard keys to the elements.
        """
        # box.event_generate('<Down>')
        self._a_entry.bind("<Return>", lambda event=None: self._operation_combobox.focus())

        self._operation_combobox.bind("<Return>", lambda event=None: self._b_entry.focus())

        self._b_entry.bind("<Return>", lambda event=None: self._ok_button_click())
        # <Return> is Enter on the keyboard
        # lambda generates a function with an event variable as input to avoid an error

    def _display_elements(self) -> None:
        """
        Display all frame elements.
        """
        self._info_label.pack()

        self._input_frame.pack(pady=10)
        self._a_entry.grid(column=1, row=0, padx=5)
        self._operation_combobox.grid(column=2, row=0)
        self._b_entry.grid(column=3, row=0, padx=5)

        self._result_textbox.pack()
        self._ok_button.pack(pady=10)  # y-axis padding = 10px

    def _ok_button_click(self) -> None:
        """
        Put calculation results into the entry.
        """
        inp_a = self._a_entry.get()  # get first text
        inp_b = self._b_entry.get()  # get second text
        inp_operation = self._operation_combobox.get()  # get operation
        result = perform_operation(Decimal(inp_a), Decimal(inp_b), inp_operation)  # Calculate result

        self._result_textbox.configure(state="normal")
        self._result_textbox.delete(1.0, "end")  # delete all characters
        # enters the calculation result
        self._result_textbox.insert(1.0, result)
        self._result_textbox.configure(state="disabled")
