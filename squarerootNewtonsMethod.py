def f(a):
    guess = -200
    ite = 0
    for i in range(10):
        print(ite)
        print(guess)
        guess = guess/2 + a/(2*guess)
        ite+=1
f(100)
