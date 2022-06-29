#----Final Project-----#
# Authors: [Tanya Chisepo
#----------------------------------------

import requests
import json
import random

print("WELCOME TO THE WORLD TRIVIA GAME\n"+"⭐️"*35)


print("\nChoose a category from the following:\n9. General Knowledge\n10.Entertainment: Books\n11. Entertainment:Film\n12. Entertainment: Music\n13. Entertainment:Musicals & Theatres\n14. Entertainment: Television\n15. Entertainment: Video Games\n16. Entertainment: Board Games\n17. Science & Nature\n18. Science: Computers\n19. Science: Mathematics\n20. Mythology\n21. Sports\n22. Geography\n23. History\n24. Politics\n25. Art\n26. Celebrities\n27. Animals\n28. Vehicles\n29. Entertainment: Comics\n30.Science: Gadgets\n31. Entertainment: Japanese Anime & Manga\n32.Entertainment: Cartoons and Anime\n")

while True:
  category = int(input())
  if category in range(9,33):
    break
  else:
    print("Invalid option.Try again")

print("\nChoose a level of difficulty:\n1. Easy\n2. Medium\n3. Hard")
while True:
  choice= int(input())
  if choice == 1:
    difficulty = "easy"
    break
  elif choice == 2:
    difficulty = "medium"
    break
  elif choice == 3:
    difficulty = "hard"
    break
  else :
    print("Invalid option. Try again")

print("\nDifficulty: {}\n".format(difficulty))

response = requests.get("https://opentdb.com/api.php?amount=10&category={}&type=multiple&difficulty={}".format(category,difficulty))

api_data = response.text
quiz_data = json.loads(api_data)



i = 0
points = 0
while i <= 9:
  question = quiz_data['results'][i]['question']
  print(question)
  correct_answer = quiz_data['results'][i]['correct_answer']

  answers = [quiz_data['results'][i]['incorrect_answers'][0], quiz_data['results'][i]['incorrect_answers'][1], quiz_data['results'][i]['incorrect_answers'][2],quiz_data['results'][i]['correct_answer']]
    
  random.shuffle(answers)
  answer_list = random.sample(answers,4)
    
  print("1. "+answer_list[0])
  print("2. "+answer_list[1])
  print("3. "+answer_list[2])
  print("4. "+answer_list[3])

  user_answer = int(input("your answer:\t"))

  if user_answer == 1:
    tag = answer_list[0]
  elif user_answer == 2:
    tag = answer_list[1]
  elif user_answer == 3:
    tag = answer_list[2]
  elif user_answer == 4:
    tag = answer_list[3]
    
  if tag == correct_answer:
    points += 1
    print('\nYayy!You got it right!👏')
    print("You have {} points".format(points))
  else :
    print('❌Oops! Wrong answer')
    print("The correct answer is : ",correct_answer)
  print("~"*65)
  i += 1

if points >= 7:
  print("🎊 🎉CONGRATULATIONS!YOU WON WITH {} points".format(points))
else:
  print("YOU LOSE!\n Try Again")


