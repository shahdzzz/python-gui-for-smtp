import smtplib
from tkinter import *
import webbrowser


def send_message():

    address_info=address.get()
    email_body_info = email_body.get()
    subject_info=subject.get()
    sender = account.get()
    pswrd = password.get()

    # create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #authentication
    server.login(sender, pswrd)
    # message
    msg = "From: " + sender + "\n" + "To: " + address_info + "\n" + "Subject: " + subject_info + "\n" + email_body_info
    server.sendmail(sender,address_info, msg)
    e=Label( text="Email sent successfully")
    e.place(x=400, y=620)
    sender_entry.delete(0, END)
    password_entry.delete(0, END)
    address_entry.delete(0, END)
    subject_entry.delete(0, END)
    email_body_entry.delete(0, END)


def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")



app = Tk()

app.geometry("800x800")

app.title("Python send mail app")

heading = Label(text="Python GUI for SMTP", bg="black", fg="white", font="10", width="500", height="1")

heading.pack()

a = Label( text="To use this app turn this setting ON for your account", fg="black",font="0.1", width="300", height="2")

a.bind("<Button-1>", setup)
a.pack()


sender_field = Label(text="sender Address :")
password_field = Label(text="sender password :")
address_field = Label(text="Receiver Address :")
subject_body_field = Label(text="subject :")
email_body_field = Label(text="Message content :")




sender_field.place(x=15, y=70)
password_field.place(x=15, y=130)
address_field.place(x=15, y=210)
subject_body_field.place(x=15, y=270)
email_body_field.place(x=15, y=330)


address = StringVar()
email_body = StringVar()
subject=StringVar()
account = StringVar()
password = StringVar()

sender_entry = Entry(textvariable=account, width="50")
password_entry = Entry(textvariable=password, width="50",show="*")
address_entry = Entry(textvariable=address, width="50")
email_body_entry = Entry(textvariable=email_body)
subject_entry = Entry(textvariable=subject, width="50")
email_body_entry.place(width="600",height="180")


sender_entry.place(x=15, y=100)
password_entry.place(x=15, y=160)
address_entry.place(x=15, y=240)
subject_entry.place(x=15, y=300)
email_body_entry.place(x=15, y=360)

button = Button(app, text="Send Message", command=send_message, width="30", height="2", bg="grey")

button.place(x=180, y=550)

mainloop()

