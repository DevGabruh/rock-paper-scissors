###### Computer Side ######
import random

rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



print("Computer Chose: ")
random_num = random.randint(0, 2)

if random_num == 0:
    print(rock1)
elif random_num == 1:
    print(paper1)
elif random_num == 2:
    print(scissors1)