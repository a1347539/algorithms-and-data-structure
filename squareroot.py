def squareroot(x):
    accuracy = 0.00001
    guess = 9
    guessed = 0
    while True:
        newguess = guess - ((guess**2)-x)/(2*guess)
        guessed += 1;
        if abs(newguess-guess) < accuracy:
            print(guessed)
            return newguess
        guess = newguess
    

print(squareroot(900))
