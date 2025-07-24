import tkinter
def cal_bmi():
    h=float(ht_val.get())
    w=float(wt_val.get())
    h1=h/100
    bmi=w/h1**2
    if bmi<=18.5:
        status="underweight"
    elif 18.5 < bmi <= 24.9:
        status="Normal"
    elif 25 < bmi < 30:
        status="overweight"
    else:
        status="obesity"

    res.config(text=f"BMI is{bmi:2f} ({status})",bg="blue")
root=tkinter.Tk()
root.geometry("500x500")
root.title("BMI CALCULATOR")
root.config(bg="#f0f0f0")

head=tkinter.Label(root,text="BMI CALCULATOR",font=("Arial",20,"bold"))
head.pack(pady=50)

fr=tkinter.Frame(root,bg="#f0f0f0")
fr.pack(pady=5)

ht=tkinter.Label(fr,text="HEIGHT(in cm)",font=("Arial",15))
ht.grid(row=1,column=0,padx=5,pady=5)

ht_val=tkinter.Entry(fr)
ht_val.grid(row=1,column=1,padx=5,pady=5)

wt=tkinter.Label(fr,text="WEIGHT(in kg)",font=("Arial",15))
wt.grid(row=3,column=0,padx=5,pady=5)

wt_val=tkinter.Entry(fr)
wt_val.grid(row=3,column=1,padx=5,pady=5)

bt=tkinter.Button(fr,text="CALCULATE",font=("Arial",18,"bold"),fg="red",command=cal_bmi)
bt.grid(row=6,column=0,padx=5,pady=5)

res=tkinter.Label(text="BMI CALCULATOR",bg="blue")
res.pack(pady=10)

root.mainloop()