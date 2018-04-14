'''
Created on 2018-03-07

@author: jetrat
'''



import sys
import os
import random



##########################################
##  VARS
##########################################

pos_count = 4



##########################################
##  FUNCTIONS
##########################################

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def tell_rules():
    clear_screen()
    print('I\'m thinking of ' + str(pos_count) +' numbers. You should guess it.')
    print('When number in your guess is "in place", I would say, that you have a "bull".')
    print('When number isn\'t "in place", but still in my number, I would say, that you have a "cow".')
    print('So, make a try)')
    print()
    None


def generate_combination(pos_count):
    combination = []
    
    while len(combination) < pos_count:
        combination.append(random.randint(0, 9))
    
    return combination


def ask_for_answer():
    while True:
        answer = input('Type answer (' + str(pos_count) + ' numbers), "new" (for new game) or "quit" (to finish playing):\n')
        
        if ((answer == 'quit') or (answer == 'new')):
            break
        
        if ((len(answer) == pos_count) and (answer.isdigit())):
            answer = list(answer)
            break
    
    return answer


def count_result(combination, answer):
    combination_test = combination[:]
    answer_test = dict(enumerate(answer))
    answer_not_bulls = {}
    
    for pos_num in answer_test:
        if int(answer_test[pos_num]) == combination_test[pos_num]:
            combination_test[pos_num] = 'b'
        else:
            answer_not_bulls[pos_num] = int(answer_test[pos_num])
    
    for pos_num in answer_not_bulls:
        if answer_not_bulls[pos_num] in combination_test:
            combination_test[combination_test.index(answer_not_bulls[pos_num])] = 'c'
    
    return [combination_test.count('b'), combination_test.count('c')]


def tell_result(result):
    print('Bulls/Cows: ' + str(result[0]) + '/' + str(result[1]) + '\n')
    if result[0] == pos_count:
        win()


def win():
    print('Yay! You\'ve won!')
    is_new_game = input('Do you wanna play again? (y/n)\n')
    if is_new_game == 'n':
        quit_game([])


def quit_game(combination):
    print()
    if combination != []:
        print('Combination was ' + ''.join(str(element) for element in combination))
    
    print('See ya!')
    input()
    sys.exit()



##########################################
##  MAIN
##########################################

if __name__ == '__main__':

    while True:
        tell_rules()
        
        
        combination = generate_combination(pos_count)
        
        #DEBUG
        #print(str(combination))
        
        
        while True:
            answer = ask_for_answer()
            
            if answer == 'quit':
                quit_game(combination)
            if answer == 'new':
                break
            
            result = count_result(combination, answer)
            
            tell_result(result)
            
            if result[0] == 4:
                break