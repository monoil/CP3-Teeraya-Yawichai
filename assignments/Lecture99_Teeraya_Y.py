# โปรแกรมคำนวณดัชนีมวลกาย BMI
from tkinter import *


def leftClickBtn(event):
    h = float(textBoxHeight.get())
    w = float(textBoxWeight.get())
    bmi = w/((h/100)**2)
    print(bmi)
    resultValueLabel.configure(text=str(bmi))
    '''
        Source: https://www.si.mahidol.ac.th/th/healthdetail.asp?aid=1361
        ค่า BMI < 18.5  แสดงถึง อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม
        ค่า BMI 18.5 – 22.90 แสดงถึง อยู่ในเกณฑ์ปกติ
        ค่า BMI 23 – 24.90 แสดงถึง  น้ำหนักเกิน
        ค่า BMI 25 – 29.90  แสดงถึง  โรคอ้วนระดับที่ 1
        ค่า BMI 30 ขึ้นไป  แสดงถึง  โรคอ้วนระดับที่ 2
    '''
    if bmi < 18.50:
        resultMeaningLabel.configure(text="อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม", fg="red")
    elif bmi >= 18.50 and bmi < 23.00:
        resultMeaningLabel.configure(text="อยู่ในเกณฑ์ปกติ", fg="green")
    elif bmi >= 23.00 and bmi < 25.00:
        resultMeaningLabel.configure(text="น้ำหนักเกิน", fg="red")
    elif bmi >= 25.00 and bmi < 30.00:
        resultMeaningLabel.configure(text="โรคอ้วนระดับที่ 1", fg="red")
    elif bmi >= 30:
        resultMeaningLabel.configure(text="โรคอ้วนระดับที่ 2", fg="red")


mainWindow = Tk()          # สร้างตัวแปรเก็บหน้าต่างเปล่า
labelHeight = Label(mainWindow, text="ส่วนสูง (ซม.)").grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0, column=1)

labelWeight = Label(mainWindow, text="น้ำหนัก (กก.)").grid(row=1, column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1, column=1)

weight = textBoxWeight.get()
height = textBoxHeight.get()

submitButton = Button(mainWindow, text="คำนวณ")
submitButton.grid(row=3, column=1)
submitButton.bind('<Button-1>', leftClickBtn)

resultLabel = Label(mainWindow, text="ผลลัพธ์:", anchor="e")
resultLabel.grid(row=4, column=0)

resultValueLabel = Label(mainWindow, text="", anchor="e")
resultValueLabel.grid(row=4, column=1)

MeaningLabel = Label(mainWindow, text="แปลผลค่า BMI: ", anchor="e")
MeaningLabel.grid(row=5, column=0)

resultMeaningLabel = Label(mainWindow, text="")
resultMeaningLabel.grid(row=5, column=1)

mainWindow.mainloop()      # สั่งให้แสดงผลหน้าต่าง