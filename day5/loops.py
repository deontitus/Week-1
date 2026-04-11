#Basic For Loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("------------------")

#String Iteration
name = "Deon"
print("Characters in the name:")
for char in name:
    print(char)

print("------------------")

#While Loop - Countdown Timer
print("Countdown Timer:")
count = 10
while count >= 0:
    print(count)
    count -= 1

print("-----------------")

#Sum of Numbers
total = 0
for i in range(1, 51):
    total += i

print("Sum of numbers from 1 to 50:", total)

print("------------------")

#Break Example
print("Break at 7:")
for i in range(1, 11):
    if i == 7:
        break
    print(i)

print("------------------")

#Continue Example
print("Skip 5 using continue:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("------------------")

#Nested Loops
print("5x5 Square of Stars:")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()