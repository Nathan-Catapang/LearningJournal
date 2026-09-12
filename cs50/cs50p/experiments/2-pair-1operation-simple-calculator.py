# just tried without dictionaries and lists. I will learn them soon but I just wanted to make a simple calculator that can do basic operations and compare the results.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return round(x / y, 2)
    else:
        print("Syntax Error. Try again!")
        return None
def main():
    while True:
        print("\nSimple Calculator")
        print("a. Add two numbers")
        print("s. Subtract two numbers")
        print("m. Multiply two numbers")
        print("d. Divide two numbers")
        print("n. Exit")

        choice = input("Choose an option: ")

        if choice in ["a", "s", "m", "d"]:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))

            if choice == "a":
                result = add(x, y)
            elif choice == "s":
                result = subtract(x, y)
            elif choice == "m":
                result = multiply(x, y)
            elif choice == "d":
                result = divide(x, y)

            if result is not None:
                print (f"Result: {result}")


        elif choice == "n":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


main()


#I still haven't learn abt lists LO. I just tried and played but I will soon. I just wanted to make a simple calculator that can do basic operations and compare the results.
#imma do a full functional calcu tomorrow with lists and dictionaries and maybe even classes.
# I just wanted to make a simple one first to get the hang of conditionals lol.
