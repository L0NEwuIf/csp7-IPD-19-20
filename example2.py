####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Baboons'
strategy_name = 'Collude and then betray'
strategy_description = '''collude the first round. If they betray more than 20 times, then we betray. \n'''
    
def move(my_history, their_history, my_score, their_score):
  theirB = 0
  if len(my_history) == 0:
      return 'c'
  for action in their_history:
    if action == 'b':
      theirB+=1 
  if theirB >= 20: 
      return 'b'        
  else:
      return 'c'