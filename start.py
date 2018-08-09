gen_data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import tkinter as tk
import random

class NWHCWalletGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.words = tk.Button(self)
        self.words["text"] = "Generate password"
        self.words["command"] = self.encGen
        self.words.pack(side="top")

    def encGen(self):
        print("Note that the other window may not be responding.\nThis is normal.")
        data = random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data) + random.choice(gen_data)
        print(data)
        password = hash(data)
        data = "no"
        print("Please confirm password.")
        check = input('> ')
        if (hash(check) == password):
            check = 'no'
            print("Password confirmed.")
        else:
            print("Incorrect. Please press \"Generate password\" again.")
        
root = tk.Tk()
app = NWHCWalletGUI()
app.master.title("NowhereCoin Wallet")
app.master.geometry("875x445")
app.master.iconbitmap('.\icon.ico')
app.mainloop()
