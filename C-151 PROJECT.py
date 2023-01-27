from tkinter import *
root = Tk()

root.title(" SALES APPLICATION")
root.geometry("400x400")
root.configure(background="yellow")

lable_month = Label(root)
lable_profits = Label(root)

lable_max_profit = Label(root)
lable_max_month = Label(root)

lable_min_profit = Label(root)
lable_min_month = Label(root)

month = ("january","february","march","april","may","june","july","august","september",
         "october","november","december")

profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

lable_month["text"] = "Month" + str(month)
lable_month.place(relx=0.5,rely=0.2,anchor=CENTER)

lable_profits["text"] = "Profit" + str(profits)
lable_profits.place(relx=0.5,rely=0.3,anchor=CENTER)

def max_profit():
    lable_max_month = max(profits)
    lable_max_month_index = profits.index(lable_max_month)
    print(lable_max_month_index)
    lable_max_profit = month[lable_max_month_index]
    print("maximum profit of " + str(lable_max_month) + " was recorded in the month of " 
    + str(lable_max_profit))

def min_profit():
    lable_min_month = min(profits)
    lable_min_month_index = profits.index(lable_min_month)
    print(lable_min_month_index)
    lable_min_profit = month[lable_min_month_index]
    print("minimum profit of " + str(lable_min_month) + " was recorded in the month of " 
    + str(lable_min_profit))

btn_max=Button(root,text="Show maxsimum profible month", command=max_profit,bg="Light green",fg="Black")
btn_max.place(relx=0.5,rely=0.4,anchor=CENTER)

btn_max=Button(root,text="Show miniimum profible month", command=min_profit,bg="Light green",fg="Black")
btn_max.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

