from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#above are tkinter libraries
import requests

import smtplibgit
#smtplib module is used to send otp via e-mail

from bs4 import BeautifulSoup
#BeautifulSoup is used to webscrape 

#starting frontend
root = Tk()
root.geometry("600x600")
root.configure(bg='white')
def horoscope(zodiac_sign: int, day: str) :
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day_name.get()}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text

    
def printvals():
    print(type(birthdatevalue.get()))
    print(birthdatevalue.get())
    month=birthmonthvalue.get()
    date=birthdatevalue.get()
    
    if birthdatevalue.get()>31 or birthdatevalue.get==0:
        Label(root,text='               Please enter valid date from 1 to 31 only.         ',fg='black',bg='white',font=("Times",10)).grid(row=11,column=10)
            
    elif birthmonthvalue.get()>12 or birthmonthvalue.get()==0:
         Label(root,text='          Please enter valid month number  1 to 12 only.        ',fg='black',bg='white',font=("Times",10)).grid(row=11,column=10)
    elif  "@" not in emailvalue.get():
         Label(root,text='     Please enter valid e-mail id     ',fg='black',bg='white',font=("Times",10)).grid(row=11,column=10)
        
        
    else:
         Label(root,text='Hey! {} check your email for the horoscope!'.format(namevalue.get()),fg='black',bg='white',font=("Times",10)).grid(row=11,column=10)
        
    sign=''
    if month == 12:
        if (date < 22):
            sign = 'Sagittarius'
        else:
            'Capricorn'
    elif month == 1:
        if (date < 20):
            sign = 'Capricorn'
        else:
            'Aquarius'
    elif month == 2:
        if (date < 19):
            sign = 'Aquarius'
        else:
            sign='Pisces'
    elif month == 3:
        if (date < 21):
            sign = 'Pisces'
        else:
            'Aries'
    elif month == 4:
        if (date < 20):
            sign = 'Aries'
        else:
            sign='Taurus'
    elif month == 5:
        if (date < 21):
            sign = 'Taurus'
        else:
            sign='Gemini'
    elif month == 6:
        if (date < 21):
            sign = 'Gemini'
        else:
            sign='Cancer'
    elif month == 7:
        if (date < 23):
            sign = 'Cancer'
        else:
            sign='Leo'
    elif month == 8:
        if (date < 23):
            sign = 'Leo'
        else:
            sign='Virgo'
    elif month == 9:
        if (date < 23):
            sign= 'Virgo'
        else:
            sign='Libra'
    elif month == 10:
        if (date < 23):
            sign = 'Libra'
        else:
            sign='Scorpio'
    elif month == 11:
        if (date < 22):
            sign= 'Scorpio'
        else:
            sign='Sagittarius'
    if sign =='Aries':
        zodiac_sign=1

    if sign=='Taurus':
        zodiac_sign=2

    if sign=='Gemini':
        zodiac_sign=3
    if sign=='Cancer':
        zodiac_sign=4
    if sign=='Leo':
        zodiac_sign=5
    if sign=='Virgo':
        zodiac_sign=6
    if sign=='Libra':
        zodiac_sign=7

    if sign=='Scorpio':
        zodiac_sign=8

    if sign=='Sagittarius':
        zodiac_sign=9
    if sign=='Capricorn':
        zodiac_sign=10
    if sign=='Aquarius':
        zodiac_sign=11
    if sign=='Pisces':
        zodiac_sign=12
    horoscope_text = horoscope(zodiac_sign, day_name.get())
    #print(horoscope_text)
    # constructing a server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # providing security to the server
    server.starttls()
    server.login('sachdeva.aaryan22@gmail.com', 'emxtjdnhwvtawmfh')
    message = 'Hello {}, your zodiac sign is {} and horoscope for {} is {} '.format(namevalue.get(),sign,day_name.get(),horoscope_text)
    reciever = emailvalue.get()
    server.sendmail('sachdeva.aaryan22@gmail.com', reciever, message)
    



Label(root, text='                    WELCOME TO HOROSCOPE PREDICTOR                            ',fg='black',bg="white",anchor=NE,font=("Times",35)).grid(row=0,column=10)






#image
image=Image.open('horofinal.jpg')
resize_image=image.resize((470,350))
photo = ImageTk.PhotoImage(resize_image)
label = Label(root,image = photo)
label.image = photo
label.grid(row=2,column=10,sticky="n")
#take details


#Text for our form
name = Label(root, text="Enter your Name                                                                                                                                    ",fg='black',bg='white',font=('Times',12))
birthdate = Label(root, text="Birthday date (1 to 31)                                                                                                                           ",fg='black',bg='white',font=('Times',12))
birthdaymonth = Label(root, text="Birthday month -eg. 10 for October                                                                                                        ",fg='black',bg='white',font=('Times',12))
email= Label(root, text="Email-id                                                                                                                                                  ",fg='black',bg='white',font=('Times',12))
day= Label(root, text="     Select day from the given list                                                                                                                         ",fg='black',bg='white',font=('Times',12))
speed_list = ['yesterday', 'today', 'tomorrow']


#Pack text for our form
name.grid(row=4, column=10)
birthdate.grid(row=5, column=10)
birthdaymonth.grid(row=6, column=10)
email.grid(row=7, column=10)
day.grid(row=8,column=10)



# Tkinter variable for storing entries
namevalue = StringVar()
birthdatevalue = IntVar()
birthmonthvalue = IntVar()
emailvalue = StringVar()
day_name=StringVar()



#Entries for our form
nameentry = Entry(root,width=30,textvariable=namevalue)
birthdateentry = Entry(root,width=30,textvariable=birthdatevalue)
birthmonthentry = Entry(root,width=30,textvariable=birthmonthvalue)
emailentry = Entry(root,width=30,textvariable=emailvalue)
day_menu = ttk.Combobox(root, textvariable=day_name, values=speed_list,width=27)
day_menu.grid(row=8, column=10, padx=20, pady=5)



# Packing the Entries
nameentry.grid(row=4, column=10)
birthdateentry.grid(row=5, column=10)
birthmonthentry.grid(row=6, column=10)
emailentry.grid(row=7, column=10)

#Button & packing it and assigning it a command
Button(text="Submit", command=printvals).grid(row=10, column=10)
root.mainloop()
#some changes made by aaryan
#some more changes as a branch

#some more more more more changes as a branch
#some even more more more more changes as a branch
