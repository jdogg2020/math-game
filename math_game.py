import os
import sys
import random
from PIL import Image

import round_engine

class Game():
  def __init__(self, upper_limit):
    self.games = {}
    self.rounds_to_play = 10
    self.correct = 0
    self.upper_limit = upper_limit

  def PlayGame(self):
    for each in range(self.rounds_to_play):
      print 'Question %s:' % (each)
      self.games[each] = round_engine.Round(self.upper_limit)
      if self.games[each][0]:
        self.correct += 1
    final_score = (self.correct / float(self.rounds_to_play) * 100)
    print 'Your score is %s' %  (final_score)
    if final_score == 100.0:
      pic_to_display = random.choice(os.listdir('images'))
      pic = Image.open(os.path.join('images', pic_to_display))
      pic.show()
      return True
    else:
      print 'Missed questions:\n'
      for played_round in self.games.itervalues():
        if played_round[0] is False:
          print 'Question: %syour answer: %s, correct answer: %s\n' % (played_round[1],
                                                                   played_round[2],
                                                                   played_round[3])
      return False
    

def main(upper_limit=10):
  while True:
    a = Game(upper_limit)
    increase_limit = a.PlayGame()
    play_again = raw_input('Do you want to play again? Y/N\n')
    if play_again.lower() == 'y':
      if increase_limit:
        user_choice = raw_input('Do you want to make it harder? Y/N\n')
        if user_choice.lower() == 'y':
          main(upper_limit + 10)
      else:
        main(upper_limit)
    else:
      sys.exit()


if __name__=='__main__':
  main()
