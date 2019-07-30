# Create an horoscope list
# Create list of 3 horoscopes
# Set up user input asking for birthday
# Create function to return zodiac sign by number using if statements
# Pass zodiac sign to function that randomly picks horoscope
# Return zodiac sign along with horoscope
# Stretch Goals
# Stretch One: Add method to add and delete horoscopes
# Stretch Two: Add in checks for all the user input. If incorrect user input either give the option to reenter the input or end program
import random

hList = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

horoList = ['Put yourself in the service of someone or something else today.', 'Avoid anything that looks like it could evolve into a combative situation today.', 'Do not worry if the road you are traveling on right now is banked in fog.']

def getBday():
    bday = input('Enter your birthday as <month> <day>: ')
    bList = bday.split(' ')
    print(bList)
    if bList[0] == 'March':
        if int(bList[1]) >= 21:
            print(hList[0])
        else: print(hList[11])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'April':
        if int(bList[1]) >= 21:
            print(hList[1])
        else: print(hList[0])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'May':
        if int(bList[1]) >= 22:
            print(hList[2])
        else: print(hList[1])     
        rand = random.randint(0,2)
        print(horoList[rand])       
    elif bList[0] == 'June':
        if int(bList[1]) >= 22:
            print(hList[3])
        else: print(hList[2])
        rand = random.randint(0,2)
        print(horoList[rand])    
    elif bList[0] == 'July':
        if int(bList[1]) >= 23:
            print(hList[4])
        else: print(hList[3])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'August':
        if int(bList[1]) >= 23:
            print(hList[5])
        else: print(hList[4])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'September':
        if int(bList[1]) >= 24:
            print(hList[6])
        else: print(hList[5])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'October':
        if int(bList[1]) >= 24:
            print(hList[7])
        else: print(hList[6])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'November':
        if int(bList[1]) >= 23:
            print(hList[8])
        else: print(hList[7])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'December':
        if int(bList[1]) >= 22:
            print(hList[9])
        else: print(hList[8])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'January':
        if int(bList[1]) >= 21:
            print(hList[10])
        else: print(hList[9])
        rand = random.randint(0,2)
        print(horoList[rand])
    elif bList[0] == 'February':
        if int(bList[1]) >= 22:
            print(hList[11])
        else: print(hList[10])
        rand = random.randint(0,2)
        print(horoList[rand])             


getBday()
