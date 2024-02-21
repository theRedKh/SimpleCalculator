#Started : Thursday Jul 14th 2022
#Designing graphical user interface calculator - basics of Tkinter
#Goal: Create an APK graph calculator

#Program Start
from tkinter import *
import tkinter.font as font
root = Tk()
root.title("Calculator")

#Input box
dataEntry = Entry(root,width = 35, bg="white") 
dataEntry.grid(row=0, column =0, columnspan = 3, pady = 20)
#dataEntry.insert(0, "Enter a number")

#Button functions
def button_click(number):       #function for every button clicked, passing the parameter NUMBER
    current = dataEntry.get()   #store the current number in variable CURRENT
    dataEntry.delete(0,END)     #clear the stored NUMBER so that the next number can be stored to create more than one digit numbers
    dataEntry.insert(0,str(current) + str(number))  #concatenate CURRENT number with new NUMBER to create more than one digit number

def button_add():
    firstNum = dataEntry.get()  #collect the current number
    global f_Num                #make the current number a global variable so it can be accessed for the operation
    f_Num = int(firstNum)
    global math
    math = "add"
    dataEntry.delete(0,END)     #clear the screen for the next number to be typed in for operation

def button_subtract():
    firstNum = dataEntry.get()  #collect the current number
    global f_Num                #make the current number a global variable so it can be accessed for the operation
    f_Num = int(firstNum)
    global math
    math = "subtract"
    dataEntry.delete(0,END)     #clear the screen for the next number to be typed in for operation

def button_multiply():
    firstNum = dataEntry.get()  #collect the current number
    global f_Num                #make the current number a global variable so it can be accessed for the operation
    f_Num = int(firstNum)
    global math
    math = "multiply"
    dataEntry.delete(0,END)     #clear the screen for the next number to be typed in for operation

def button_divide():
    firstNum = dataEntry.get()  #collect the current number
    global f_Num                #make the current number a global variable so it can be accessed for the operation
    f_Num = int(firstNum)
    global math
    math = "divide"
    dataEntry.delete(0,END)     #clear the screen for the next number to be typed in for operation

def button_clear():
    dataEntry.delete(0,END)     #Clear the screen

def button_equals():
    secondNum = dataEntry.get() #Collect the second entered number for following operation
    dataEntry.delete(0,END)     #Clear screen to display answer
    if math == "add":
        dataEntry.insert(0,f_Num + int(secondNum))
    if math == "subtract":
        dataEntry.insert(0,f_Num - int(secondNum))
    if math == "multiply":
        dataEntry.insert(0,f_Num * int(secondNum))
    if math == "divide":
        dataEntry.insert(0,f_Num / int(secondNum))
#Define Buttons
button1 = Button(root, text= "1", padx = 30, pady= 20, bg= "black", fg = "white", command= lambda: button_click(1))
button2 = Button(root, text= "2", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(2))
button3 = Button(root, text= "3", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(3))
button4 = Button(root, text= "4", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(4))
button5 = Button(root, text= "5", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(5))
button6 = Button(root, text= "6", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(6))
button7 = Button(root, text= "7", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(7))
button8 = Button(root, text= "8", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(8))
button9 = Button(root, text= "9", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(9))
button0 = Button(root, text= "0", padx = 30, pady= 20, bg = "black", fg= "white", command= lambda: button_click(0))


#FUNCTION BUTTONS
buttonClr = Button(root, text= "Clear", padx = 60, pady= 20, bg= "white", fg= "black", command= button_clear)
buttonEquals = Button(root, text= "  =  ", padx = 60, pady= 20, bg= "red", fg= "white", command= button_equals)

button_add = Button(root, text= "+", padx= 30, pady= 20, bg= "black", fg= "white", command= button_add)
button_subtract = Button(root, text= "-", padx= 31, pady= 20, bg= "black", fg= "white", command= button_subtract)
button_multiply = Button(root, text= "*", padx= 31, pady= 20, bg= "black", fg= "white", command= button_multiply)
button_divide = Button(root, text= "/", padx= 31, pady= 20, bg= "black", fg= "white", command= button_divide)


#Button Position
button1.grid(row = 3, column= 0)
button2.grid(row = 3, column= 1)
button3.grid(row = 3, column= 2)

button4.grid(row = 2, column= 0)
button5.grid(row = 2, column= 1)
button6.grid(row = 2, column= 2)

button7.grid(row = 1, column= 0)
button8.grid(row = 1, column= 1)
button9.grid(row = 1, column= 2)

button0.grid(row = 4, column= 0)
buttonClr.grid(row = 5, column= 1, columnspan = 2)
buttonEquals.grid(row = 4, column= 1, columnspan= 2)

button_add.grid(row= 5, column= 0)
button_subtract.grid(row= 6, column= 0)
button_multiply.grid(row= 6, column= 1)
button_divide.grid(row= 6, column= 2)

root.mainloop()
