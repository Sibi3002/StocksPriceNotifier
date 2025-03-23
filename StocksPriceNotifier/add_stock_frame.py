from tkinter import *
from customtkinter import *
import 

def get_new_stock(stocktype, button):
    new_stock_type=stocktype.get()
    new_stock_code=button.get()

    new_stock=stock_class.stock(new_stock_code, new_stock_type)


def add_stock_frame(root):
    frame = CTkFrame(master=root, width=800, height=50, fg_color="#333333", )
    stocktype = CTkComboBox(master=frame, values=["NSE", "BSE"], corner_radius=40)
    stocktype.place(relx=0.1, rely=0.2)
    entry = CTkEntry(master=frame, width=400, height=40, fg_color="#454545", 
                     placeholder_text="Enter the stock code here.", corner_radius=40)
    button = CTkButton(master=frame, width=70, height=40, fg="#", corner_radius=40, command=lambda: get_new_stock(stocktype, button))
    entry.place(relx=0.3, rely=0.1,)
    frame.place(relx=0, rely=0.08)