import smtplib
#smtplib module is used to send otp via e-mail

from bs4 import BeautifulSoup
def horoscope(zodiac_sign: int, day: str) :
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text
if __name__ == "__main__":
    print("This is a program to know your horoscope:")
    date = int(input("Enter your  birth date: \n"))

    if date > 31:
        print("Please enter the correct date. The date should not exceed 31\n")

    month = int(input(
        "Enter your birthday month in number format ( for example 1 for January, 2 for February,..... and  12 for December ): \n"))

    if month > 12:
        print("Please enter the correct month. The month should not exceed 12\n")

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
    print("\nYour Astrological sign is :", sign)


    print("Choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
    day = input("Input the day from said list: ")
    horoscope_text = horoscope(zodiac_sign, day)
    #print(horoscope_text)
    # constructing a server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # providing security to the server
    server.starttls()
    server.login('sachdeva.aaryan22@gmail.com', 'orjwaawshqqjrrup')
    message = 'Hello, your zodiac sign is {} and horoscope for {} is {}'.format(sign,day,horoscope_text)
    reciever = input('Enter your Gmail-id: ')
    server.sendmail('sachdeva.aaryan22@gmail.com', reciever, message)
    print('Check your E-mail for the horocope!')
