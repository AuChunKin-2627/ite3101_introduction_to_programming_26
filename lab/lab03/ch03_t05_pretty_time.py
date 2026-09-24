from datetime import datetime

now = datetime.now()
print(now.hour)
print(now.minute)
print(now.second)

print('%02dh:%02d:%02d'%(now.hour,now.minute,now.second))