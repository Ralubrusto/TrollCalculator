from tkinter import *
import guiconfig as _gui


class TrollCalculator(Tk):

    def __init__(self):
        super(TrollCalculator, self).__init__()

        # Main frames
        self.top_frame = Frame(self)
        self.bottom_frame = Frame(self)
        self.top_frame.grid(row=1)
        self.bottom_frame.grid(row=2)

        # Troll
        self.troll_enable = BooleanVar(value=False)
        self.troll_box = Checkbutton(self.bottom_frame,
                                     text='Enable \nTroll \nMode',
                                     variable=self.troll_enable)

        # Entry + history
        self.__create_entry_widgets()

        # Buttons
        self.buttons = []
        self.__number_button()
        self.__operation_buttons()
        self.__pack_buttons(_gui.BUTTONPOSITION)

        # Calculator
        self.ans = self.tmp = self.operation = None

    def __create_entry_widgets(self):
        # Text entry
        self.entry_text = StringVar(value=0)
        self.entry_widget = Entry(self.top_frame,
                                  textvariable=self.entry_text,
                                  justify=RIGHT)
        self.entry_widget.grid(row=2,
                               pady=10)

        # Auxilliary frames
        self.history_text = StringVar(value='')
        self.history = Label(self.top_frame,
                             textvariable=self.history_text,
                             justify=RIGHT)
        self.operation_text = StringVar(value='')
        self.operation_label = Label(self.top_frame,
                                     textvariable=self.operation_text,
                                     justify=CENTER)
        self.history.grid(row=1)
        self.operation_label.grid(row=1,
                                  column=1,
                                  padx=10)

    def __number_button(self):
        _config = {'font': ('Helvetica', 10),
                   'width': 15,
                   'height': 8}
        for n in range(10):
            _button = Button(self.bottom_frame,
                             text=str(n),
                             command=lambda x=n: self.__write_number(str(x)),
                             **_config)
            self.buttons.append(_button)

    def __operation_buttons(self):
        _config = {'font': ('Helvetica', 10),
                   'width': 15,
                   'height': 8
                   }
        for op in ['+', '-', 'x', '/', '<<', '=']:
            _button = Button(self.bottom_frame,
                             text=op,
                             command=lambda x=op: self.__operation_command(x),
                             **_config)
            self.buttons.append(_button)

    def __pack_buttons(self, mapper):

        for button in self.buttons:
            position = mapper[button['text']]
            button.grid(**position)

    def __write_number(self, number):
        if not self.troll_enable.get():
            _text = self.entry_text.get()
            if number == '<<':
                self.entry_text.set('0' if len(_text) == 1 else _text[:-1])
            else:
                self.entry_text.set(number if _text == '0' else _text + number)
        else:
            self.__do_trolling()

    def __operation_command(self, operation):
        if not self.troll_enable.get():
            if operation == '<<':
                self.__write_number(operation)
            elif operation == '=':
                if self.operation is not None:
                    self.__run_equal()
                    self.__update_labels()
                self.operation = None
                self.entry_text.set(0)
            else:
                self.operation = operation
                self.tmp = float(self.entry_text.get())
                self.ans = self.tmp
                self.__update_labels()
                self.entry_text.set(0)
        else:
            self.__do_trolling()

    def __run_equal(self):
        self.tmp = float(self.entry_text.get())
        self.ans = self.__math()

    def __math(self):
        print(self.operation)
        if self.operation == '+':
            return self.ans + self.tmp
        elif self.operation == '-':
            return self.ans - self.tmp
        elif self.operation == 'x':
            return self.ans * self.tmp
        elif self.operation == '/':
            try:
                return self.ans / self.tmp
            except ZeroDivisionError:
                self.__show_troll()
                return 0
        else:
            self.operation = self.tmp = None
            return 0

    def __update_labels(self):
        self.operation_text.set(self.operation)
        self.history_text.set(self.ans)

    def __show_troll(self):
        self.troll_box.grid(row=3, column=4)

    def __do_trolling(self):
        new_mapping = _gui.scramble_positions()
        for button in self.buttons:
            button.grid_forget()
            position = new_mapping[button['text']]
            button.grid(**position)


if __name__ == '__main__':
    my_calc = TrollCalculator()
    my_calc.mainloop()
