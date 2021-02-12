def enter_number():
    flat = True
    while flat == True:
        number = input("Enter the number to convert: ")
        try:
            number = float(number)
            flat = False
        except ValueError:
            print("\033[;31m"+str('"'+number+'"') + " No is a number, trie againt\n" +'\033[0;m')
    return number

def convert(number, measure):
    if measure == 1:
        return number*5/18
    else:
        return number*18/5

def unit_measure(measure):
    if measure == 1:
        return "m/s"
    elif measure == 2:
        return "km/h"
    else:
        return ""


def menu_options():
    print("Choose the unit of your number")
    print("----------------------------------------")
    print("Option 1: km/h")
    print("Option 2: m/s")
    print("Option 0: SALIR")
    print("----------------------------------------")

def menu_validation():
        while True:
            menu_options()
            try:
                option = int(input("Select option: "))

                if option in range(3):

                    if option == 0:
                        print("bye! see you soon")
                    print()
                    return option
                else:
                    print("\033[;31m"+'Error, only numbers from 0 to 2'+'\033[0;m')

            except ValueError:
                print("\033[;31m"+"Error, only numbers"+'\033[0;m')


if __name__ == '__main__':
    print("//***********************************//")
    print("WELCOME TO THE PHYSICAL UNIT CONVERTER")
    print("----------------------------------------")
    number = enter_number()
    print("----------------------------------------")
    option_num = menu_validation()
    if option_num!=0:
        print('\033[;32m' + "The conversion is: " + str(convert(number, option_num)) + " "+ unit_measure(option_num) + '\033[0;m')
