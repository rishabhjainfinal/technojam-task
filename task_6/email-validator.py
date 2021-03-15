# email validator GUI
from tkinter import *
import re
from threading import Thread
from time import sleep as nap

class validator(object):
    def __init__(self,master):
        self.email_patern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w{2,3}){1,2}$'
        self.root = master
        self.root.title('Email validator ')
        self.height = 200
        self.width = 600
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.configure(bg ='#34495E')
        self.results_color = 'white'
        self.last_value = ''
        self.smoothness = 0.95 # value between 0.1 and 1 "nap time between each check"
        self.gui(self.root)
        th = Thread(target=self.result_thread,daemon=True)
        th.start()
    
    def validate_email(self,mail_text):
        '''Take the input as the text and verify the email address'''
        if re.search(self.email_patern,mail_text) :
            return True
        return False
    
    def gui(self,master):
        self.email_text = StringVar()
        # Enter the email "Enter box"
        Enter_eamil_lable = Label(master, text="Enter Email to validate.",bg ='#34495E',fg = "White",font=('arial',21,'bold') )
        Enter_eamil_lable.place(x=int((self.width/2 - len(Enter_eamil_lable['text'])/2)/2))
        self.Enter_eamil = Entry(master,textvariable=self.email_text,bd =5,font=('arial',21,'bold'))
        self.Enter_eamil.place(y= 50,x=60,height = 50,width = 480)
        self.update_result(master)
        
    def update_result(self,master):
        border_frame = Frame(master, background=self.results_color) 
        valid_lable = Label(border_frame , text="valid",bg ='#34495E',fg = self.results_color,font=('arial',26,'bold'))
        valid_lable.pack(padx=0.8, pady=0.8) 
        border_frame.place(x=int((self.width/2 - len(valid_lable['text'])/2)/1.2),y = 120) 

    def result_thread(self):
        while True:
            nap(1 - self.smoothness)
            if self.last_value == self.email_text.get() :
                # if there is no change in the value
                continue
            if self.email_text.get() == "":
                # default color
                self.results_color = 'white'
            elif self.validate_email(self.email_text.get()):
                # update the colours to green 
                self.results_color = '#b2ff96'
            else :
                # update the colours to red
                self.results_color = '#ff7a7f'
            self.update_result(self.root)
            self.last_value = self.email_text.get()

    @classmethod
    def runner(cls):
        root = Tk()
        validator_cls = cls(root)
        root.mainloop()

if __name__== "__main__":
    a = validator.runner()
    # examples 
        # thisistheway@myworld.com
        # print(a.validate_email("rishabhjainfinal@gmail.com"))