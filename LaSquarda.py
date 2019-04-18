team_name = 'LaSquarda'
strategy_name = 'Copy'
strategy_description = 'Collude first then copy the previous action of your opponent.'



def move(my_history, their_history, my_score, their_score):
     if len(my_history)==0: # It's the first round: collude
        return 'c'
     else:
           if 'b' in their_history[-1:]:
              return 'b'
           else:
              return 'c'
              #return the previous action of the opponent