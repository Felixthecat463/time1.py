#Avant 8h affiche pause
#   après 20h affiche pause
#   Running le reste du temps

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M")
print("Current Time =", current_time)

current_time = now.strftime("%H")
current_time=int(current_time)
#Pause=[20,21,22,23,0,1,2,3,4,5,6,7]
Running=[8,9,10,11,12,13,14,15,16,17,18,19]
print(current_time in Running)
if True:
    print("Running")
else:
    print("En pause de 20h à 8h")




