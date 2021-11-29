#this is a review option button screen
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox

root = Tk()
root.title('Rate our program')
#defining buttons
Button_one = Button
Button_two = Button
Button_three = Button
Button_four = Button
Button_five = Button
#message after choosing a rating
def Clicked():
        tkinter.messagebox.showinfo("", "Thank you for leaving a review")
        exit()



# one star review
Label(root, text = 'One star review', font =('Verdana', 12)).pack(side = TOP, pady = 10)
photo_one = PhotoImage(file = r"C:\Users\X\Desktop\Project\Star review images\onestar.png")
Button_one(root, text='One star review', image= photo_one, command =Clicked).pack()

# two star review
Label(root, text = 'two star review', font =('Verdana', 12)).pack(side = TOP, pady = 10)
photo_two = PhotoImage(file = r"C:\Users\X\Desktop\Project\Star review images\twostar.png")
Button_two(root, text='two star review', image= photo_two, command =Clicked).pack()

#three star review
Label(root, text = 'Three star review', font =('Verdana', 12)).pack(side = TOP, pady = 10)
photo_three = PhotoImage(file = r"C:\Users\X\Desktop\Project\Star review images\threestar.png")
Button_three(root, text='three star review', image= photo_three, command =Clicked).pack()

#Four star review
Label(root, text = 'Four star review', font =('Verdana', 12)).pack(side = TOP, pady = 10)
photo_four = PhotoImage(file = r"C:\Users\X\Desktop\Project\Star review images\fourstar.png")
Button_three(root, text='Four star review', image= photo_four, command =Clicked).pack()

#five star review
Label(root, text = 'five star review', font =('Verdana', 12)).pack(side = TOP, pady = 10)
photo_five = PhotoImage(file = r"C:\Users\X\Desktop\Project\Star review images\fivestar.png")
Button_three(root, text='Four star review', image= photo_five, command =Clicked).pack()
#Later on, the choosen score will be added to the user's review and calculated among all other.

root.mainloop()