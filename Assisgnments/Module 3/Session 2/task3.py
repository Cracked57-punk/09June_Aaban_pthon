import os
os.chdir("Assisgnments/Module 3/Session 2")

orders = open("orders.txt", "w")
orders.write("Order 1\nOrder 2\nOrder 3\nOrder 4\nOrder 5")
orders.close()

orders = open("orders.txt", "r")
count = 1

"""for line in orders:
    print(f"{count}) {line.strip()}")
    count += 1
    print(orders.tell())"""

"""Python doesnt actually read one line at a time under the hood.To make iteration fast,it reads a big chunk of the file into an internal buffer at once,then hands you lines out of that buffer as the loop progresses.Because of this,the actual file pointer jumps ahead in large chunks—it's no longer at a position that corresponds to "end of the line you just printed."Python knows this and deliberately blocks tell() during iteration with that OSError, rather than give you a number that would be misleading."""
#This is the reason we are using while loop.


while True:
    line = orders.readline()
    if line == "":
        break
    print(f"{count}) {line.strip()}")
    count += 1
    print(orders.tell())

orders.close()