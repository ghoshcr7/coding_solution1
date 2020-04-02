from random import randint

game_running=True

while game_running==True:
    player={'name':'Soumalya','attack':15,'heal':6,'health':100}
    monster={'name':'Abhijit','attack_min':15,'attack_max':20,'health':100}
    print('---'*7)
    print('Enter player name')
    player['name']=input()
    

    print(player['name']+' has '+str(player['health'])+' health')
    print(monster['name']+' has '+str(monster['health'])+' health')
    
    new_round = True

    while new_round == True:
        player_won=False
        monster_won=False
        print('---'*7)
        print('please select action')
        print('1)Attack')
        print('2)Heal')
        print('3)Exit')
        print('---'*7)
        player_choice=int(input())

        if player_choice==1:
            monster['health']=monster['health']-player['attack']
            if monster['health']<=0:
                player_won=True
            else:
                monster_attack = randint(monster['attack_min'],monster['attack_max'])
                player['health']=player['health']-monster_attack
                if player['health']<=0:
                    monster_won=True
    
        elif player_choice==2:
            player['health']=player['health']+player['heal']
            monster_attack = randint(monster['attack_min'],monster['attack_max'])
            player['health']=player['health']-monster_attack
            if player['health']<=0:
                monster_won=True
        elif player_choice == 3:
            game_running=False
            new_round=False
        else:
            print('invalid input')
        if player_won == False or monster_won == True:
            print(player['name']+' has '+str(player['health'])+' left')
            print(monster['name']+' has '+str(monster['health'])+' left')
        elif player_won:
            print(player['name']+' won')
            new_round=False
        elif monster_won:
            print(monster['name']+' won')
            new_round=False

      




 
    
   
