import datetime

name =input("Enter your Name:::: ")
d=datetime.datetime.now()
curhour=d.hour
curmin=d.minute
if curhour<12:
	print("Good Morning",name)
elif curhour>12 and curhour<=16:
	print("Good Afternoon",name)
elif curhour > 16 and curhour <=21:
	print("Good Evening",name)
else:
	print("Good Night",name)
