import random
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
choise=int(input("what do you choose? 0 for rock 1 for paper 2 for scissors\n"))
if choise>= 3 or choise< 0: 
  print("You typed an invalid number, you lose!")
  quit()



if choise==0:
  print(f"you choose: \n {rock}")
elif choise==1:
  print(f"you choose: \n {paper}")
else:
  print(f"you choose: \n {scissors}")

comb=[rock,paper,scissors]
computer_choise=random.randint(0,2)
computer_list=comb[computer_choise]
print(f"computer choose:\n{computer_list}")



if choise == computer_choise:
  print("Game tie")

elif choise == 0 and computer_choise==2:
  print("you win")
elif choise==1 and computer_choise==0:
  print("you win")


elif choise==2 and computer_choise==1:
  print("you win")
else:
  print("you lose")



  


  

  

 