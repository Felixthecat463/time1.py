from datetime import datetime

now = datetime.now()
print("")
print("Etat du système")
print("")

current_time = now.strftime("%H:%M")
print("Current Time =", current_time)

current_time = now.strftime("%H")
current_time=int(current_time)
if current_time>=10:
    print("Running")
elif current_time<10:
    print("Pause")