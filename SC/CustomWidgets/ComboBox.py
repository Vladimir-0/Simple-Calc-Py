from customtkinter import CTkComboBox


class ComboBox(CTkComboBox):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Down>", lambda event=None: self._open_dropdown_menu())
        # Objects with a _ at the beginning of the name are considered inaccessible outside the class.
        # I inherit a class to have access to _open_dropdown_menu() method.
