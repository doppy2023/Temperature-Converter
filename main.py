units = ["1", "2", "3", "4", "5", "6"]

choose_unit = input(
    "What unit would you like to convert?\n\n C = Celsius\n F = Fahrenheit\n K = Kelvin\n\nOptions: \n \n 1| C TO F \n 2| C TO K \n 3| F TO C \n 4| F TO K \n 5| K TO C \n 6| K TO F \n\nChoose a number: "
)

if choose_unit == "1":

    try:
        x = float(
            input(
                "\nWhat number in Celsius would you like to convert to Fahrenheit?\n\nInput your number: "
            ))
        print(x, "C° is:")
        x = x * 1.8 + 32

        print(x, "F°")
        quit

    except Exception:
        print('\nThis is not a number, please try again.')

if choose_unit == "2":
    try:
        x = float(
            input(
                "\nWhat number in Celsius would you like to convert to Kelvin?\n\nInput your number: "
            ))
        print(x, "C° is:")
        x = x + 273.15
        print(x, "K")
        quit

    except Exception:
        print('\nThis is not a number, please try again.')

if choose_unit == "3":
    try:
        x = float(
            input(
                "\nWhat number in Fahrenheit would you like to convert to Celsius?\n\nInput your number: "
            ))
        print(x, "F° is:")
        x = (x - 32) * 5 / 9
        print(x, "C°")
        quit

    except Exception:
        print('\nThis is not a number, please try again.')

if choose_unit == "4":
    try:
        x = float(
            input(
                "\nWhat number in Fahrenheit would you like to convert to Kelvin?\n\nInput your number: "
            ))
        print(x, "F° is:")
        x = (x - 32) * 5 / 9 + 273.15
        print(x, "K")
        quit

    except Exception:
        print('\nThis is not a number, please try again.')

if choose_unit == "5":
    try:
        x = float(
            input(
                "\nWhat number in Kelvin would you like to convert to Celsius?\n\nInput your number: "
            ))
        print(x, "K is:")
        x = x - 273.15
        print(x, "C°")
        quit

    except Exception:
        print('\nThis is not a number, please try again.')

if choose_unit == "6":
    try:
        x = float(
            input(
                "\nWhat number in Kelvin would you like to convert to Fahrenheit?\n\nInput your number: "
            ))
        print(x, "K is:")
        x = (x - 273.15) * 9 / 5 + 32
        print(x, "F°")
        quit

    except Exception:
        print('\nThis is not a number, please try again.')

if choose_unit not in units:
    print("\nInvalid option, please choose one of the options")
    quit()
