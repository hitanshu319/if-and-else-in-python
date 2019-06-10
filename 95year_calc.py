from datetime import datetime
name=input('What is your name? \n')
age=int(input('How old are you? \n'))
x= int((95-age) + datetime.now().year)
print("your name is:",name)
print ("You will turn 95 years old in:",x)
