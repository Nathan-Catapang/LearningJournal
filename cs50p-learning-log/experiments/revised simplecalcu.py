# Now i tried with dictionaries and functions. Still can't hhandle PEMDAS operations but I'm working my way up since i started from scatch.
# I also discovered the exception functions loll.
# also tried input.split()


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return round(x / y, 2)
    return None


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    while True:
        print("\nCalculator Revised")
        print("Enter format: number operator number (example: x + y)")
        print("Type 'n' to exit")

        user_input = input(">> ")

        if user_input.lower() == "n":
            print("Goodbye!")
            break

        try:
            x, op, y = user_input.split()

            x = int(x)
            y = int(y)

            if op in operations:
                result = operations[op](x, y)

                if result is None:
                    print("Error: invalid operation")
                else:
                    print(f"Result: {result}")
            else:
                print("Invalid operator")

        except ValueError:
            print("Invalid format. Use: number operator number")
        except Exception as e:
            print(f"An error occurred: {e}")


main()


# This is the new code I tried to implement earlier but with operations instead. Did it with 2 variables intended but seem to work if not applying PEMDAS.
# Will try to token parsing and stacks later on to handle that.
