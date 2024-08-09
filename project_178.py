from tkinter import *
import random
root = Tk()
root.title("Encyclopedia")
root.geometry("600x600")
root.config(background = "blue")

label_score = Label(root, text = "Score: 0", font = ("Arial", 15, "bold"), bg = "white")
label_score.place(relx = 0.3, rely = 0.3, anchor = W)
label = Label(root, font = ("cursive", 15, "bold"), bg = "white")
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
input_value = Entry(root)

class game:
    def __init(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["BLUE", "PINK", "GREEN", "RED", "YELLOW", "CYAN"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["blue", "pink", "green", "red", "yellow", "cyan"]
        self.random_number_for_color = random.randint(0, 5)
        label["text"] = self.text[self.random_number_for_text]
        label["fg"] = self.color[self.random_number_for_color]
        
    def __updateGame(self, input_value):
        if(input_value == self.color[self.random_number_for_color]):
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(0, 10)
            label_score["text"] = "Score:- " + str(self.__score)
    
    def get_user_value(self, input_value):
        self.__updateGame(input_value)
        
obj = game()
     
def getInput():
    get.input_value(value)
    obj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0, END)

btn = Button(root, text = "START", command = obj, bg = "dark olive green", fg = "white", relief = FLAT, padx = 10, pady = 1, font = ("Arial",15))
btn.place(relx = 0.8, rely = 0.8, anchor = CENTER)

root.mainloop()
