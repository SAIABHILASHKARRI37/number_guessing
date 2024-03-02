x='welcome to Quiz game 2024'
print(x.upper())
print('Do you want to take Quiz ')
answer=input()
if answer.lower() !='yes':
    quit()
count=0
print('Lets start the quiz:)')
answer=input('Is 2024 is leap year:')
if answer.lower()=='yes':
    print('Correct')
    count=count+1
else:
    print('Incorrect')
answer=input('Which month we got independence:')
if answer.lower()=='augest':
    print('Correct')
    count=count+1
else:
    print('Incorrect')
answer=input('iabh-use these words and make a name:')
if answer.lower()=='abhi':
    print('Correct')
    count=count+1
else:
    print('Incorrect')
print("no.of questions You got correct are "+str(count))
print("percentage is "+str((count/3)*100)+"%")
