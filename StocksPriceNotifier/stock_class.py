from customtkinter import *
from yahoo_fin import stock_info
from tkinter import *
from tkinter import messagebox
import storage,time, random, alert_on
class data:
    def __init__(self, code, type, ap, at, status, new, canvas_frame):
        self.code=code
        self.type=type
        self.alertto= at
        self.status=status              #1=yet to alert   0=alerted
        self.new = new
        flag=1
        self.alertprice=ap
        self.check=0
        self.canvas_frame=canvas_frame
        try:
            if type == 'IND':
                self.curprice='%.2f'%(stock_info.get_live_price(f'{code}.NS'))
            else:
                self.curprice='%.2f'%(stock_info.get_live_price(f'{code}'))
        except:
            messagebox.showinfo('Invaid Input',"Check if the stock ticker is valid. and verify the Exchange")
            flag = 0
        
        if flag ==1:
            if new == 0:
                storage.add(code, type, ap, at, status)
            self.createframe()
        
    #edit frame
    def editframe(self):
        #erase
        self.at.place_forget()
        self.ap.place_forget()
        self.edit.place_forget()
        self.status_label.place_forget()
        #display
        self.alertprice_entry.delete(0, END)
        self.alertprice_entry.insert(END, self.alertprice)
        self.alertprice_entry.place(relx=0.36,rely=0.2)
        self.stat.place(relx=0.6, rely=0.2)
        self.update_btn.place(relx=0.8, rely=0.2)
        self.alertto_combo.place(relx=0.485, rely=0.2)


    def update(self,at,ap):
        #erase
        self.alertprice_entry.place_forget()
        self.stat.place_forget()
        self.update_btn.place_forget()
        self.alertto_combo.place_forget()
        #edit database
        storage.edit(self.code, self.type, ap, at, self.status)
        self.alertprice = ap
        self.alertto = at
        #display()
        if self.type == 'IND':
            self.ap = CTkLabel(master=self.add_frame, text=f'₹ {self.alertprice}')
        else:
            self.ap = CTkLabel(master=self.add_frame, text=f'$ {self.alertprice}')
        self.at = CTkLabel(master=self.add_frame, text=f'{self.alertto}')
        
        self.ap.place(relx=0.38,rely=0.2)
        self.at.place(relx=0.49, rely=0.2)
        self.status_label.place(relx=0.61, rely=0.2)
        self.edit.place(relx=0.82, rely=0.2)

    def reset(self):
        if self.stat.get()=="on":
            if self.status == 0:
                self.status=1
                self.status_label.configure(text="Yet to alert")
            else:
                self.status=0
                self.status_label.configure(text='Alerted')
        else:
            pass
        
    def delframe(self):
        storage.delete(self.code)
        self.add_frame.destroy()

    def refresh(self):
        if self.type == 'IND':
                self.curprice='%.2f'%(stock_info.get_live_price(f'{self.code}.NS'))
                self.curprice_label.configure(text = f'₹ {self.curprice}')
        else:
            self.curprice='%.2f'%(stock_info.get_live_price(f'{self.code}'))
            self.curprice_label.configure(text = f'$ {self.curprice}')

        """refresh"""
        # self.curprice_label.configure(text = str(random.randint(0,1000)))
        self.curprice_label.after(30000, self.refresh)

    
    def createframe(self):
        self.add_frame = CTkFrame(master=self.canvas_frame, height=50, width=780, fg_color="#ADD8E6", border_color= "#6F8FAF", border_width= 3, bg_color="#F9CCD3", )
        self.st = CTkLabel(master=self.add_frame, text=f'{self.type}')
        self.stock_name = CTkLabel(master=self.add_frame, text=f"{self.code}")
        if self.type == 'IND':
            self.curprice_label = CTkLabel(master=self.add_frame, text=f'₹ {self.curprice} ')
        else:
            self.curprice_label = CTkLabel(master=self.add_frame, text=f'$ {self.curprice}')
        if self.type == 'IND':
                self.ap = CTkLabel(master=self.add_frame, text=f'₹ {self.alertprice}')
        else:
                self.ap = CTkLabel(master=self.add_frame, text=f'$ {self.alertprice}')
        self.at = CTkLabel(master=self.add_frame, text=f'{self.alertto}')
        if self.status==0:
            self.status_label = CTkLabel(master=self.add_frame, text="Alerted")
        else:
            self.status_label = CTkLabel(master=self.add_frame, text="Yet to alert")
        self.edit = Button(self.add_frame, text='Edit', command=self.editframe)
        self.x = Button(self.add_frame, text='x', command=self.delframe)
        

        self.stock_name.place(relx=0.15, rely=0.2)
        self.st.place(relx=0.05, rely=0.2)
        self.curprice_label.place(relx=0.27, rely=0.2)
        self.ap.place(relx=0.38,rely=0.2)
        self.at.place(relx=0.49, rely=0.2)
        self.status_label.place(relx=0.61, rely=0.2)
        self.edit.place(relx=0.82, rely=0.2)
        self.x.place(relx=0.94, rely=0.2)
        #hidden
        if self.alertto =="BUY":
            self.alertto_combo = CTkComboBox(master=self.add_frame, values=["BUY","SELL"], width=70)
        else:
            self.alertto_combo = CTkComboBox(master=self.add_frame, values=["SELL","BUY"], width=70)
        self.alertprice_entry = CTkEntry(master=self.add_frame, width=70, height=30,fg_color= "#ADD8E6",
                      placeholder_text="Alert Price")
        self.update_btn = CTkButton(master=self.add_frame, width=70, height=30, corner_radius=30, text="Update", command=lambda: self.update(self.alertto_combo.get(),self.alertprice_entry.get()))
        self.stat = CTkCheckBox(master=self.add_frame, text='Change status', command=self.reset, onvalue="on", offvalue="off")
        """for live updates"""
        self.refresh()

        self.add_frame.pack()
