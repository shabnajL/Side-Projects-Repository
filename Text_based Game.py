import time

true = ["t", "T", "True", "true"]
false = ["f", "F", "False", "false"]

count = 0 #for calculating correct ans
print("Hello there! I am TexBaG.\tWhat's your name?")
name = input("Enter gamer name : ")

print("\nok,"+ name + ",nice to meet you.")
print("\nGame Rule: You'll be given 7 questions. Ans them in either true or false.")
print("If it's True: type T/t/true/True and if it's False: type f/F/False/false")
ready = input("So are You ready?\t[press enter]")
print("Let's get it,"+ name +"!😎")
time.sleep(1)

print("1.Namjoon is rrrrrrrapmostaaa")
ans = input("Your choice >>> ")
if ans in true:
    count += 1
else:
    count += 0

print("\n2.Jimin got no jams.")
ans = input("Your choice >>> ")
if ans in true:
    count += 1
else:
    count += 0

print("\n3.S in Suga stands for SWAAGG")
ans = input("Your choice >>> ")
if ans in true:
    count += 1
else:
    count += 0

print("\n4.Poison apple doesn't harm kookie because he is JK")
ans = input("Your choice >>> ")
if ans in true:
    count += 1
else:
    count += 0

print("\n5.Hoseok is Moonshine.")
ans = input("Your choice >>> ")
if ans in false:
    count += 1
else:
    count += 0

print("\n6.Jin is an 8")
ans = input("Your choice >>> ")
if ans in false:
    count += 1
else:
    count += 0

print("\n7.v.....")
print("Your choice >>> ")
print("wait...!\nNuga nareul magado\tNaui gal gireul gandago\nInsaeng han bangirago\tLeggo (Leggo!)\tLeggo (Leggo!)\n")
time.sleep(1)
print("🤣🤣🤣🤣🤣\n")
print("You've finished," + name + ".  You got ", count, "out of 6 correct!\n")

