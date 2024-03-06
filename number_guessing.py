import random #by using this we get random numbers
type_of_range=input('enter number:')
if type_of_range.isdigit():
    type_of_range=int(type_of_range)
rand=random.randrange(type_of_range)
no_of_chances_took=0
while True:
    no_of_chances_took+=1
    guess=input("Guess the number:")
    if guess.isdigit():
        guess=int(guess)
    if guess==rand:
        print('your guess is correct')
        break
    else:
        print('your guess is not matched')
        continue
        
print('no of chances taken are '+str(no_of_chances_took))
    

    
