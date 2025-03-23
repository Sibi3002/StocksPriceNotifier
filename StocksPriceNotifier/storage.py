import csv
from tkinter import messagebox

def add(code, exchange, alertprice, alertto, status):
    content = read()
    unique = []
    for x in content:
        unique.append(x[0])
    if code in unique:
        pass
    else:
        with open('stock_data.csv','a+') as file:
            lst = [code, exchange, alertprice, alertto, status]

            for i in lst:
                file.write(str(i)+',')
            file.write('\n')

def delete(code):
    lst=[]
    with open('stock_data.csv','r+') as file:
        csv_reader = csv.reader(file)
        rows = [row for row in csv_reader]
        for row in rows:
            lst.append(row)
            if row[0]==code and row != '':
                lst.remove(row)

    with open('stock_data.csv','w') as file:
        for data in lst:
            for i in data:
                if i != '':
                    file.write(str(i)+',')
            file.write('\n')

def read():
    with open('stock_data.csv','r') as file:
        lst = []
        content = csv.reader(file)
        lst=[row for row in content]
        return lst

def edit(code, exchange, alertprice, alertto, status):
    lst=[]
    with open('stock_data.csv','r+') as file:
        csv_reader = csv.reader(file)
        rows = [row for row in csv_reader]
        for row in rows:
            lst.append(row)
            if row[0]==code and row != '':
                lst.remove(row)
                lst.append([code, exchange, alertprice, alertto, status])
        
    with open('stock_data.csv','w') as file:
        for data in lst:
            for i in data:
                if i != '':
                    file.write(str(i)+',')
            file.write('\n')

def off_status(code):
    lst=[]
    with open('stock_data.csv','r+') as file:
        csv_reader = csv.reader(file)
        rows = [row for row in csv_reader]
        for row in rows:
            lst.append(row)
            if row[0]==code and row != '':
                lst.remove(row)
                update = row
                row[4] = 0
                lst.append(update)

    with open('stock_data.csv','w') as file:
        for data in lst:
            for i in data:
                if i != '':
                    file.write(str(i)+',')
            file.write('\n')

def store_phone(number):
    with open('phone.txt','w+') as file:
        file.write(number)
    
def read_phone():
    with open('phone.txt','r') as file:
        number = file.read()
        return number
