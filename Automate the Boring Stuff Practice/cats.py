print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) < 0:
        print('You cant have negative cats.')
    else:
        print('That is not a lot')
except ValueError:
    print('You did not enter a number.')
