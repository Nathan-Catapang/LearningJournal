import time
def timed():
    time.sleep(1.5)

Friends = ["Jade", "Raniel", "Reuven", "Denver"]
while True:
    name = input("What is your name? ").strip()
    name_caps = name.capitalize()

    if not name_caps:
        print("Error! You aint slick manigguh!!")
        continue
    else:
        print(f"Hello, {name_caps}!")
        timed()
        break

print("Kill Yourself" if name_caps in Friends else "Hi Cutie!!")
timed()
input("Have you eaten yet?" )
timed()
input("Nice LOl")
timed()
print(f"Nice, either way, it's nice to meet you, {name_caps}!")
input("Press Enter to see your future...")
print("yea you really are friends lol")
