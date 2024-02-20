import random
def rolldice():
    s=random.randint(1,6)
    return s
def game():
    print('welcome to the game')
    play = 'yes'
    while play =='yes':
        input('press Enter to roll the dice')
        result=rolldice()
        print('you rolled a', {result})
        play=input('do you want to roll again?(yes/no):')
    print('Thanks for playing')    
game()
