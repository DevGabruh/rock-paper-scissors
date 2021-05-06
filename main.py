rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for scissors. ")

if game == "0":
  print(rock)
elif game == "1":
  print(paper)
elif game == "2":
  print(scissors)

import computer
