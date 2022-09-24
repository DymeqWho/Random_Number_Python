import random

random_number = random.randint(1,100)
close_range = 3
close_small_border_number = random_number - close_range
close_big_border_number = random_number + close_range

print("Gissa talet\nDu ska nu gissa ett tal mellan 1 och 100, så varsågod...\nSkriv in ett tal")
guess = int(input())

def OutOfRange():
    return guess > 100 or guess < 1

def CloseBigEnough ():
    return guess <= (random_number + close_range) and guess > random_number

def CloseSmallEnough():
   return guess >= (random_number - close_range) and guess < random_number

def TooSmall():
   return guess < close_small_border_number

def TooBig():
    return guess > close_big_border_number

if OutOfRange():
    print("Du måste skriva in ett tal mellan 1 och 100!")
elif CloseBigEnough():
    print("Dit tal är för stort. Gissa på ett mindre tal\nDu är dock nära och det bränns")   
elif CloseSmallEnough():
    print("Dit tal är för litet. Gissa på ett större tal\nDu är dock nära och det bränns")
elif TooSmall():
    print("Dit tal är för litet.")
elif TooBig():
    print("Dit tal är för stort.")
else:
    print("Du gissade! Grattis!")

print("\nProgramet är slut\nPress any key")
exit = input()
