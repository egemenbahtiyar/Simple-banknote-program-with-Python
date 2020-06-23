def main():
    print("Please select your option:\n 1 for Currency\n 2 for Goods")
    try:
        user_input1 = int(input("Selection:"))     # First Selection input
        if user_input1 == 1:
            selection1()              # if user chooses 1 it will run function 1.
        elif user_input1 == 2:
            selection2()              # if user chooses 2 it will run function 2.
        else:
            print("Please enter correct selection 1 or 2 !")  # if the user has entered an integer but this is not 1 and 2 this code will work.
    except ValueError:  # if the user used a character other than integer for selection, this exception code works.
        print("Please enter integer number just use 1 or 2 !")
        pass


def selection1():
    selection1_input1 = str(input("Please Enter Currency:").upper())  # first selection1 input for currency
    if selection1_input1 =="FF":  # if user enter FF to input this code will execute
        try:
            selection1_input2 = int(input("Please Enter Amount:")) # selection1 input for amount
            print("Your Anahtar result of {} {} is".format(selection1_input2, selection1_input1))
            amount = selection1_input2
            FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
            TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
            DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
        except ValueError: # if the user used a character other than integer for amount, this exception code works.
            print("Please enter integer number !")
            pass
    if selection1_input1 =="DM": # if user enter DM to input this code will execute
        try:
            selection1_input2 = int(input("Please Enter Amount:")) # selection1 input for amount
            print("Your Anahtar result of {} {} is".format(selection1_input2, selection1_input1))
            amount = selection1_input2
            FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
            TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
            DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
        except ValueError: # if the user used a character other than integer for amount, this exception code works.
            print("Please enter integer number !")
            pass
    if selection1_input1 =="TL": # if user enter TL to input this code will execute
        try:
            selection1_input2 = int(input("Please Enter Amount:")) # selection1 input for amount
            print("Your Anahtar result of {} {} is".format(selection1_input2, selection1_input1))
            amount = selection1_input2
            FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
            TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
            DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
        except ValueError: # if the user used a character other than integer for amount, this exception code works.
            print("Please enter integer number !")
            pass
    else:
        print("Please enter these currencies: FF,DM,TL")


def selection2():
    selection2_input1 =str(input("Please Enter Object:").lower())#Sadece car,plane,notebook,pencil,door kullanılacak#
    if selection2_input1 =="car": # if user choose car object this code will execute
        def converterToValue(good): #this function converts objects to their values in selection2 function.
            if good == "car":
                return 5000
            elif good == "plane":
                return 200000
            elif good == "notebook":
                return 70000
            elif good == "pencil":
                return 5000
            elif good == "door":
                return 2000
            else:
                print("invalid")

        converterToValue(selection2_input1)
        print("The value of a {} is {}".format(selection2_input1, converterToValue(selection2_input1)))
        amount = converterToValue(selection2_input1)
        FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
        TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
        DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
    elif selection2_input1 =="plane": # if user choose plane object this code will execute
        def converterToValue(good): #this function converts objects to their values in selection2 function.
            if good == "car":
                return 5000
            elif good == "plane":
                return 200000
            elif good == "notebook":
                return 70000
            elif good == "pencil":
                return 5000
            elif good == "door":
                return 2000
            else:
                print("invalid")

        converterToValue(selection2_input1)
        print("The value of a {} is {}".format(selection2_input1, converterToValue(selection2_input1)))
        amount = converterToValue(selection2_input1)
        FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
        TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
        DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
    elif selection2_input1 =="notebook": # if user choose notebook object this code will execute
        def converterToValue(good): #this function converts objects to their values in selection2 function.
            if good == "car":
                return 5000
            elif good == "plane":
                return 200000
            elif good == "notebook":
                return 70000
            elif good == "pencil":
                return 5000
            elif good == "door":
                return 2000
            else:
                print("invalid")

        converterToValue(selection2_input1)
        print("The value of a {} is {}".format(selection2_input1, converterToValue(selection2_input1)))
        amount = converterToValue(selection2_input1)
        FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
        TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
        DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
    elif selection2_input1 =="pencil": # if user choose pencil object this code will execute
        def converterToValue(good): #this function converts objects to their values in selection2 function.
            if good == "car":
                return 5000
            elif good == "plane":
                return 200000
            elif good == "notebook":
                return 70000
            elif good == "pencil":
                return 5000
            elif good == "door":
                return 2000
            else:
                print("invalid")

        converterToValue(selection2_input1)
        print("The value of a {} is {}".format(selection2_input1, converterToValue(selection2_input1)))
        amount = converterToValue(selection2_input1)
        FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
        TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
        DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
    elif selection2_input1 =="door": # if user choose door object this code will execute
        def converterToValue(good): #this function converts objects to their values in selection2 function.
            if good == "car":
                return 5000
            elif good == "plane":
                return 200000
            elif good == "notebook":
                return 70000
            elif good == "pencil":
                return 5000
            elif good == "door":
                return 2000
            else:
                print("invalid")

        converterToValue(selection2_input1)
        print("The value of a {} is {}".format(selection2_input1, converterToValue(selection2_input1)))
        amount = converterToValue(selection2_input1)
        FF(amount) #this function shows how many French Franc banknotes the amount entered is converted
        TL(amount) #this function shows how many Turkish Lira banknotes the amount entered is converted
        DM(amount) #this function shows how many Deutsche Mark banknotes the amount entered is converted
    else:
        print("Please Enter these objects: car,plane,notebook,pencil,door")

def DM(amount):
    print("\n\n-In DM")

    def func1(amount):
        name = ["Maria Sibylla Merian:", "Paul Ehrlich:", "Clara Schumann:","Balthasar Neumann:"]
        notes = [500, 200, 100, 50] #this part contains values according to values of 4 Deutsche Mark banknotes
        noteCounter = [0, 0, 0, 0, ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes, noteCounter, name):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func2(amount):
        name2 = ["Paul Ehrlich:", "Clara Schumann:","Balthasar Neumann:"]
        notes2 = [200, 100, 50] #this part contains values according to values of 3 Deutsche Mark banknotes
        noteCounter2 = [0, 0, 0, ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes2, noteCounter2, name2):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func3(amount):
        name3 = ["Clara Schumann:","Balthasar Neumann:"]
        notes3 = [100, 50] #this part contains values according to values of 2 Deutsche Mark banknotes
        noteCounter3 = [0, 0, ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes3, noteCounter3, name3):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func4(amount):
        name4 = ["Balthasar Neumann:"]
        notes4 = [50] #this part contains value according to values of 1 Deutsche Mark banknote
        noteCounter4 = [0] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes4, noteCounter4, name4):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")
                print("\n")

    if amount >= 500:   # These conditions determine the right operation of functions according to the amount.
        func1(amount)
        print("\n")
        func2(amount)
        print("\n")
        func3(amount)
        print("\n")
        func4(amount)
    if 200 < amount < 500:
        func2(amount)
        print("\n")
        func3(amount)
        print("\n")
        func4(amount)
    if amount == 200:
        func2(amount)
        print("\n")
        func3(amount)
        print("\n")
        func4(amount)
    if 100 < amount < 200:
        func3(amount)
        print("\n")
        func4(amount)
    if amount == 100:
        func3(amount)
        print("\n")
        func4(amount)
    if amount < 100:
        func4(amount)
    if amount < 50:
        print("No defined banknotes under 50 DM") # if amount lower than 50 Deutsche Mark this code will execute


def FF(amount):
    print("\n")
    print("-In FF")

    def func1(amount):
        name = ["Marie Curie:", "Gustave Eiffel:", "Paul Cézanne:","Antoine de Saint-Exupéry"]
        notes = [500, 200, 100,50] #this part contains values according to values of 4 French Franc banknotes
        noteCounter = [0, 0, 0, 0  ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes, noteCounter, name):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func2(amount):
        name2 = ["Gustave Eiffel:", "Paul Cézanne:","Antoine de Saint-Exupéry"]
        notes2 = [200, 100,50] #this part contains values according to values of 3 French Franc banknotes
        noteCounter2 = [0, 0, 0 ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes2, noteCounter2, name2):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func3(amount):
        name3 = ["Paul Cézanne:","Antoine de Saint-Exupéry"]
        notes3 = [100,50] #this part contains values according to values of 2 French Franc banknotes
        noteCounter3 = [0, 0 ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes3, noteCounter3, name3):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func4(amount):
        name4 = ["Antoine de Saint-Exupéry:"]
        notes4 = [50] #this part contains values according to value of 1 French Franc banknote
        noteCounter4 = [0] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes4, noteCounter4, name4):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    if amount >=500:  # These conditions determine the right operation of functions according to the amount.
        func1(amount)
        print("\n")
        func2(amount)
        print("\n")
        func3(amount)
        print("\n")
        func4(amount)
    if 200 < amount <500:
        func2(amount)
        print("\n")
        func3(amount)
        print("\n")
        func4(amount)
    if amount == 200:
        func2(amount)
        print("\n")
        func3(amount)
        print("\n")
        func4(amount)
    if 100<amount<200:
        func3(amount)
        print("\n")
        func4(amount)
    if amount == 100:
        func3(amount)
        print("\n")
        func4(amount)
    if amount < 100:
        func4(amount)
    if amount < 50:
        print("No defined banknotes under 50 FF") # if amount lower than 50 French Franc this code will execute

def TL(amount):
    print("\n\n-In TL")

    def func1(amount):
        name = ["1 Izmir Clock Tower:", "Mehmet Akif Ersoy:", "Students:"]
        notes = [500, 100, 10] #this part contains values according to values of 3 Turkish Lira banknotes
        noteCounter = [0, 0, 0, ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes, noteCounter, name):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func2(amount):
        name2 = ["Mehmet Akif Ersoy:", "Students:"]
        notes2 = [100, 10] #this part contains values according to values of 2 Turkish Lira banknotes
        noteCounter2 = [0, 0, ] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes2, noteCounter2, name2):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    def func3(amount):
        name3 = ["Students:"]
        notes3 = [10] #this part contains values according to value of 1 Turkish Lira banknotes
        noteCounter3 = [0,] #this part contains,amount divided by notes quantities according to for highest banknote
        for i, j, z in zip(notes3, noteCounter3, name3):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(z, j, end=" ")

    if amount >=500:  # These conditions determine the right operation of functions according to the amount.
        func1(amount)
        print("\n")
        func2(amount)
        print("\n")
        func3(amount)
    if amount==100:
        func2(amount)
        print("\n")
        func3(amount)
    if amount<100:
        func3(amount)
    if amount < 10:
        print("No defined banknotes under 10 TL") # if amount lower than 10 Turkish Lira this code will execute

main()


















