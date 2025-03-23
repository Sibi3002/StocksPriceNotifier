from tkinter import *
from tkinter import messagebox
from customtkinter import *
from yahoo_fin import stock_info
import storage, time
from stock_class import data

class App:
    def __init__(self,):
        self.root = Tk()
        self.root.geometry("800x500+375+200")
        self.root.title("Stock Price Alerter !")
        self.all_frames=[]
        self.phone = storage.read_phone()
        self.nav_bar()
        self.add_stock_frame()
        self.menu()
        self.create_main_frame()
        self.from_storage()
        photo = PhotoImage(file = "f1.png")
        self.root.iconphoto(False, photo)
        self.root.resizable(0,0)
        self.root.mainloop()


    def nav_bar(self):
        self.nav_bar = CTkFrame(master=self.root, width=800, height=40, fg_color="#797979", )
        phone_label = CTkLabel(master=self.nav_bar, text="Phone No. : ", width=40, height=30)
        phone_number = CTkEntry(master=self.nav_bar, width=100, height=25, corner_radius=25)
        change = CTkButton(master=self.nav_bar, text="Change", corner_radius=25, width=40, command= lambda : self.change_no(phone_number.get()))
        change.place(relx=0.88, rely=0.15)
        phone_number.place(relx=0.75, rely=0.2)
        phone_label.place(relx=0.66, rely=0.2)
        self.nav_bar.place(relx=0, rely=0,) 


    def menu(self):
        self.menu_frame = CTkFrame(master=self.root, width=800, height=40, fg_color="#ffff80")
        stockname = CTkLabel(master=self.menu_frame, text="Stock Name")
        currentprice = CTkLabel(master=self.menu_frame, text="Current Price")
        alertprice = CTkLabel(master=self.menu_frame, text="Alert Price")
        alertto = CTkLabel(master=self.menu_frame, text="Alert to")
        status = CTkLabel(master=self.menu_frame, text="status")
        update = CTkLabel(master=self.menu_frame, text="Update")
        self.exchange = CTkLabel(master= self.menu_frame, text = "Exchange")
        self.exchange.place(relx=0.03, rely=0.2)

        update.place(relx=0.8, rely=0.2)
        status.place(relx=0.61, rely=0.2)
        alertto.place(relx=0.47, rely=0.2)
        alertprice.place(relx=0.36, rely=0.2)
        currentprice.place(relx=0.24, rely=0.2)
        stockname.place(relx=0.13, rely=0.2)
        self.menu_frame.place(relx=0, rely=0.179)
    
    def add_stock_frame(self):
        self.add_frame = CTkFrame(master=self.root, width=800, height=50, fg_color="#333333",)
        stocktype = CTkComboBox(master=self.add_frame, values=["IND", "US"], corner_radius=40, width=100, )
        stocktype.place(relx=0.03, rely=0.2, )
        entry = CTkEntry(master=self.add_frame, width=420, height=40, fg_color="#454545", text_color="#ffffff",
                            placeholder_text="Enter the stock code here.", corner_radius=40)
        entryprice = CTkEntry(master=self.add_frame, width=100, height=30, fg_color="#454545",
                            placeholder_text="Alert Price", text_color="#ffffff")
        alerttype = CTkComboBox(master=self.add_frame, values=["BUY","SELL"], width=90, corner_radius=20, bg_color="#454545")
        button = Button(master=self.add_frame, text="Add",
                            command=lambda: self.add(entry.get().upper(), stocktype.get(), entryprice.get() , alerttype.get()))
        
        #width=70, height=30, corner_radius=30, 
        alerttype.place(relx=0.60, rely=0.2)
        entryprice.place(relx=0.755, rely=0.2)
        button.place(relx=0.9, rely=0.25)
        entry.place(relx=0.2, rely=0.1,)
        self.add_frame.place(relx=0, rely=0.08)
    
    def create_main_frame(self):
        self.main_frame = Frame(self.root,)
        self.main_frame.pack(side=BOTTOM, fill=BOTH,) 
        canvas = Canvas(self.main_frame, height=368, width=750, background="#F9CCD3")
        canvas.pack(side=LEFT, fill=BOTH, expand=1)         #canvas 
        # create ttk scrollbar
        scrollbar = Scrollbar(self.main_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        # connect textbox scroll event to CTk scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)#create new frame
        self.canvas_frame = Frame(canvas, background="#F9CCD3")
        self.canvas_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        #create a window
        canvas.create_window(0,0, window=self.canvas_frame, anchor="nw",)
        canvas.configure(bg = "#F9CCD3")

    def add(self,code, type, at, ap, status=1, new=0):
        content = storage.read()
        unique = []
        for x in content:
            unique.append(x[0])
        if code in unique and new == 0:
            messagebox.showinfo('STOCK ALDREADY ADDED',"You can edit if you want")
        else:
            t = data(code, type, at, ap, status, new, self.canvas_frame)
            

    def change_no(self, number):
        if len(number)!=10:
            messagebox.showinfo('Incorrect phone number',"Length of the phone number must be 10.")
        else:
            try :
                num = int (number)
            except:
                messagebox.showinfo('Incorrect phone number',"your phone number has digits other than numbers")
            self.phone = number
            storage.store_phone(number)

    def from_storage(self):
        read = storage.read()
        #from database retriving the stocks
        for i in read:
            self.add(i[0],i[1],i[2],i[3],i[4], 1)

if __name__ == '__main__':
    a = App()