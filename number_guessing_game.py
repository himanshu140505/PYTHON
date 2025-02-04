import random
print("================================================")
print("||            NUMBER GUESSING GAME            ||")
print("================================================")

num = int(random.randint(1,100))
n = int(input("Enter your guess : "))
i=0
while(i<10):
    if (n == num):
        print("Correct Guess")
        print(f"You guessed the correct choice in {i} chances")
        break
    elif(n < num):
        print("Your GUESS is too LOWW!!")
    elif(n > num):
        print("Your GUESS is too HIGH!!!")
    n = int(input("Enter your guess : "))
    i = i+1
if(i == 10):
    print("YOUR GUESSES ARE OVER BUDDY")
    