####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray unless colluded'
strategy_description = '''Betray first round. Betray, except in a round after getting a collude.\n'''
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: 
        return 'b'
    elif their_history[-1]=='c':
        return 'c' 
    else:
        return 'b'
