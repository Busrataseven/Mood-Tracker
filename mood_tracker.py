
import matplotlib.pyplot as plt

print("Mood Tracker for the last 2 weeks")
print("Please enter one of the moods below each day:")
print("Happy, Stressed, Tired, Excited, Sad, Calm, Angry, Motivated \n")

moods = []
valid_moods = ["Happy","Stressed","Tired","Excited","Sad","Calm","Angry","Motivated"]

for i in range(1,15):
  while True:
    mood = input("Mood for day " + str(i)+ ":").capitalize().strip()
    if mood in valid_moods:
      moods.append(mood)
      break
    else:
      print("Mood is not in the list. Choose another option")

dates = []
for i in range(1,15):
  day = "Day" + str(i)
  dates.append(day)

score = {"Angry":1,"Sad":2,"Stressed":3,"Tired":4,"Calm":5,"Motivated":6,"Excited":7,"Happy":8}

scores = []
for i in moods:
  if i in score:
    point = score[i]
  else:
    point=0
  scores.append(point)

average = sum(scores) / len(scores)

if average < 3:
  suggestion = "You might be feeling unwell. Try to rest"
elif average < 5:
  suggestion = "You look tired. Take a break"
elif average < 7:
   suggestion= "You are usually calm. Try something new!"
else:
     suggestion = "You are doing great! Keep it up!"

plt.plot(dates,scores,marker = "o",color="blue")
plt.axhline(average,color="green",linestyle="--")
plt.title("14 Day Mood Graph")
plt.xticks(rotation=45)
plt.show()

print("\nYour average mood score:",average)
print("\nSuggestion:",suggestion)

print("\nAnother solutions:\n")

if average < 3:
  print("Rest well and avoid stress.")
  print("Listen to calming music.")
  print("Talk to someone you trust.")
elif average < 5:
  print("Stretch your body.")
  print("Drink water.")
  print("Get some fresh air.")
elif average < 7:
  print("Try your thoughts in a journal.")
  print("Set a personal goal.")
  print("Do something creative.")
elif average > 7:
  print("Celebrate yourself!")
  print("Spread your good energy!")
  print("Start a new project!")