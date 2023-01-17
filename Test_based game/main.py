import time

true = ["t", "T", "True", "true"]
false = ["f", "F", "False", "false"]

count = 0  # for calculating correct ans
print("Hello there! I am TexBaG.\tWhat's your name?")
name = input("Enter gamer name : ")

print("\nok," + name + ",nice to meet you.")
print("\nGame Rule: You'll be given 4 questions. Ans them in either /btrue or /bfalse.\n")
print("If it's True: type T/t/true/True and if it's False: type f/F/False/false")
ready = input("So are You ready?\t[press enter]")
print("Let's get it," + name + "!😎")
time.sleep(1)

print("Q1. FIFO is First In First Out.")
ans = input("Your choice >>> ")
if ans in true:
    count += 1
else:
    count += 0

print("\nQ2. Int hold decemals numbers.")
ans = input("Your choice >>> ")
if ans in false:
    count += 1
else:
    count += 0

print("\nQ3. v != t means v is not equal to t")
ans = input("Your choice >>> ")
if ans in true:
    count += 1
else:
    count += 0

print("\nQ4. The data structure that implements LIFO is Queues.")
ans = input("Your choice >>> ")
if ans in false:
    count += 1
else:
    count += 0

print("\n")
time.sleep(1)

print("You've finished," + name + ".  You got ",count, "out of 4 correct!\n")
