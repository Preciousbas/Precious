import random

def play():
    user = input('''
What is your choice?
'R' for rock,
'P' for paper
'S' for scissors\n
''')
    options = ['R', 'P', 'S']
    user= user.upper()
    if user in options:

        CPU =random.choice(['R', 'P', 'S'])
        
    else:
        print('Error! Try again')
        return play()

    print('Player {} : CPU {}'.format(user, CPU))
    if user==CPU:
        print( "It's a tie. Play again.")
        return play()
    

    if winner(user, CPU):
        print( "You are the winner")
    else:   
        print ('You have lost.')

def winner(user, CPU):
    if(user=='R' and CPU =='S') or (user =='S' and CPU =='P') or (user =='P' and CPU == 'R'):
        return True
    else:
        return False

#if _name_ == '_main_':
play()
