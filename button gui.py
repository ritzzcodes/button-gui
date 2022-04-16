import tkinter as tk 
class Test: 
 def __init__(self): 
 self.root=tk.Tk() 
 self.root.title("disapperaing button") 
 self.root.geometry("750x500") 
 self.Label=tk.Label(self.root,text='This message will disappear',bg='black',fg='orange').place() 
 
 self.ButtonForget=tk.Button(self.root,fg='orange',bg='black',text='click this to end') 
 self.ButtonForget.pack() 
 self.ButtonForget.place(x=260,y=280) 
 self.Label.pack() 
 self.Label.place(x=240,y=280) 
 self.root.mainloop() 
app=Test() 
