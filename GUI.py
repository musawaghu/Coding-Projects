import tkinter
import tkinter.messagebox


class GUI:
    def __init__(self):
        self.customer_name_label()
        self.crust_choice_radio_button()
        self.sauce_choice_radio_button()
        self.size_choice_radio_button()
        self.toppings_choice_radio_button()
        self._main_window.mainloop()

    def customer_name_label(self):
        self._main_window = tkinter.Tk()
        self._main_window.title("Pizza Order")
        self._1_frame = tkinter.Frame(self._main_window)
        self._2_frame = tkinter.Frame(self._main_window)
        self._3_frame = tkinter.Frame(self._main_window)
        self._name_label = tkinter.Label(self._1_frame, text="Enter your name: ")
        self._name_entry = tkinter.Entry(self._1_frame, width="10")
        self._name_label.pack(padx=10, pady=10, side="left")
        self._name_entry.pack(padx=10, pady=10, side="left")
        self._value = tkinter.StringVar()
        self._order_name_label = tkinter.Label(self._2_frame, text="Your order name is: ")
        self._order_name_label2 = tkinter.Label(self._2_frame, width=10, textvariable=self._value)
        self._order_name_label.pack(padx=10, pady=10, side="left")
        self._order_name_label2.pack(pady=10, padx=10, side="left")
        self._submit_button = tkinter.Button(self._3_frame, text="Submit", command=self.submit_callback)
        self._submit_button.pack(padx=10, pady=10, side="left")
        self._1_frame.pack()
        self._2_frame.pack()
        self._3_frame.pack()

    def submit_callback(self):
        text = self._name_entry.get()
        try:
            name = str(text)
            self._value.set(text)
        except:
            tkinter.messagebox.showerror("Error", "Please enter a name")

    def crust_choice_radio_button(self):
        self._4_frame = tkinter.Frame(self._main_window)
        self._5_frame = tkinter.Frame(self._main_window)
        self._radio_var = tkinter.IntVar()
        self._radio_var.set(1)
        self._rb1 = tkinter.Radiobutton(self._4_frame, text="Thin Crust", variable=self._radio_var, value=1)
        self._rb2 = tkinter.Radiobutton(self._4_frame, text="Regular", variable=self._radio_var, value=2)
        self._rb3 = tkinter.Radiobutton(self._4_frame, text="Deep Dish", variable=self._radio_var, value=3)
        self._ok_button = tkinter.Button(self._5_frame, text="Ok", command=self.show_crust_choice)
        self._4_frame.pack()
        self._5_frame.pack()
        self._rb1.pack()
        self._rb2.pack()
        self._rb3.pack()
        self._ok_button.pack()

    def show_crust_choice(self):
        tkinter.messagebox.showinfo("You chose " + str(self._radio_var.get()))

    def sauce_choice_radio_button(self):
        self._6_frame = tkinter.Frame(self._main_window)
        self._7_frame = tkinter.Frame(self._main_window)
        self._radio_var2 = tkinter.IntVar()
        self._radio_var2.set(4)
        self._rb4 = tkinter.Radiobutton(self._6_frame, text="Alfredo", variable=self._radio_var2, value=4)
        self._rb5 = tkinter.Radiobutton(self._6_frame, text="BBQ", variable=self._radio_var2, value=5)
        self._rb6 = tkinter.Radiobutton(self._6_frame, text="Regular", variable=self._radio_var2, value=6)
        self._ok_button1 = tkinter.Button(self._7_frame, text="Ok", command=self.show_sauce_choice)
        self._6_frame.pack()
        self._7_frame.pack()
        self._rb4.pack()
        self._rb5.pack()
        self._rb6.pack()
        self._ok_button1.pack()

    def show_sauce_choice(self):
        tkinter.messagebox.showinfo("You chose " + str(self._radio_var2.get()))

    def size_choice_radio_button(self):
        self._8_frame = tkinter.Frame(self._main_window)
        self._9_frame = tkinter.Frame(self._main_window)
        self._radio_var3 = tkinter.IntVar()
        self._radio_var3.set(7)
        self._rb5 = tkinter.Radiobutton(self._8_frame, text="Small", variable=self._radio_var3, value=7)
        self._rb6 = tkinter.Radiobutton(self._8_frame, text="Medium", variable=self._radio_var3, value=8)
        self._rb7 = tkinter.Radiobutton(self._8_frame, text="Large", variable=self._radio_var3, value=9)
        self._ok_button2 = tkinter.Button(self._9_frame, text="Ok", command=self.show_sauce_choice)
        self._8_frame.pack()
        self._9_frame.pack()
        self._rb5.pack()
        self._rb6.pack()
        self._rb7.pack()
        self._ok_button2.pack()

    def show_size_choice(self):
        tkinter.messagebox.showinfo("You chose " + str(self._radio_var3.get()))

    def toppings_choice_radio_button(self):
        self._10_frame = tkinter.Frame(self._main_window)
        self._11_frame = tkinter.Frame(self._main_window)
        self._12_frame = tkinter.Frame(self._main_window)
        self._13_frame = tkinter.Frame(self._main_window)
        self._14_frame = tkinter.Frame(self._main_window)
        self._pepporoni_label = tkinter.Label(self._10_frame, text="Enter how many pepperoni you want: ")
        self._pepporoni_entry = tkinter.Entry(self._10_frame, width="10")
        self._pepporoni_label.pack(padx=10, pady=10, side="left")
        self._pepporoni_entry.pack(padx=10, pady=10, side="left")
        self._olives_label = tkinter.Label(self._11_frame, text="Enter how many olives you want: ")
        self._olives_entry = tkinter.Entry(self._11_frame, width="10")
        self._olives_label.pack(padx=10, pady=10, side="left")
        self._olives_entry.pack(padx=10, pady=10, side="left")
        self._mushroom_label = tkinter.Label(self._12_frame, text="Enter how many mushrooms you want: ")
        self._mushroom_entry = tkinter.Entry(self._12_frame, width="10")
        self._mushroom_label.pack(padx=10, pady=10, side="left")
        self._mushroom_entry.pack(padx=10, pady=10, side="left")
        self._value2 = tkinter.StringVar()
        self._toppings_label = tkinter.Label(self._13_frame, text="Your pizza cost: ")
        self._toppings2_label = tkinter.Label(self._13_frame, width=10, textvariable=self._value2)
        self._toppings_label.pack(padx=10, pady=10, side="left")
        self._toppings2_label.pack(pady=10, padx=10, side="left")
        self._submit_button2 = tkinter.Button(self._14_frame, text="Submit", command=self.submit_callback2)
        self._submit_button2.pack(padx=10, pady=10, side="left")
        self._10_frame.pack()
        self._11_frame.pack()
        self._12_frame.pack()
        self._13_frame.pack()
        self._14_frame.pack()

    def submit_callback2(self):
        text = self._pepporoni_entry.get()
        text1 = self._olives_entry.get()
        text2 = self._mushroom_entry.get()
        try:
            toppings = float(text)
            toppings1 = float(text1)
            toppings2 = float(text2)
            if self._rb5 == 7:
                cost = 10 + (toppings * 0.50) + (toppings1 * 0.50) + (toppings2 * 0.50)
                self._value2.set(str(round(cost, 2)))
            elif self._rb6 == 8:
                cost = 11.50 + (toppings * 0.50) + (toppings1 * 0.50) + (toppings2 * 0.50)
                self._value2.set(str(round(cost, 2)))
            elif self._rb7 == 9:
                cost = 13 + (toppings * 0.50) + (toppings1 * 0.50) + (toppings2 * 0.50)
                self._value2.set(str(round(cost, 2)))
        except:
            tkinter.messagebox.showerror("Error", "Please enter a number")


