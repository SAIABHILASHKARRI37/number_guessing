import random
#rock,paper,sissor game
p_points=0#p=player
c_points=0#c=computer
options=['rock','paper','sissor']
while True:
    user_guess=input('rock/paper/sissor or q to quit the game ').lower()
    if user_guess=='q':
        break
    if user_guess not in options:
        continue
    rand=random.randint(0,2)
    #0-rock 1-paper 2-sissor
    computer_guess=options[rand]
    if user_guess=='rock' and computer_guess=='sissor':
        print('You won')
        p_points+=1
    elif user_guess=='paper' and computer_guess=='rock':
        print('you won')
        p_points+=1
    elif user_guess=='sissor' and computer_guess=='paper':
        print('you won')
        p_points+=1
    else:
        print('you lost')
        c_points+=1
print('user points :',p_points)
print('computer points :',c_points)
