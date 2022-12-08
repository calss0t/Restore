from js import document, console
from pyodide.ffi import create_proxy

import random


def my_function(*args, **kwargs):
        
            userInput = Element('rock-paper-scissors-input').element.value
            # user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
            computer = random.choice(['r', 'p', 's'])

            console.log(f'text: {userInput}')
        
            if userInput == computer:
                pyscript.write("result", 'It\'s a tie')
        
            # r > s, s > p, p > r
            if is_win(userInput, computer):
                pyscript.write("result",'You won!')
            
            else:
                pyscript.write("result",'You lost!')
        
def is_win(player, opponent):
            # return true if player wins
            # r > s, s > p, p > r
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
                or (player == 'p' and opponent == 'r'):
                return True
        
                
function_proxy = create_proxy(my_function)

document.getElementById("button").addEventListener("click", function_proxy)    
