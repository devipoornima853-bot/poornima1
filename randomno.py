import random
n = random.randint(1,10)
g = int(input("Guess: "))
print("Correct" if g == n else "Wrong")
