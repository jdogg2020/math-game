import random

def Round(upper_limit):
  round_list = [random.randint(1, upper_limit),
                random.randint(1, upper_limit)]
  round_list.sort()
  symbol = random.randint(1,2)
  if symbol == 1:
    question = ('%s + %s\n') % (round_list[0], round_list[1])
    user_answer = GetAnswer(question)
    real_answer = round_list[0] + round_list[1]
    if int(user_answer) == real_answer:
      print 'Great!\n'
      return True, question, user_answer, real_answer
    else:
      print 'Sorry, the right answer was %s\n' % (real_answer)
      return False, question, user_answer, real_answer
  else:
    question = ('%s - %s\n') % (round_list[1], round_list[0])
    user_answer = GetAnswer(question)
    real_answer = round_list[1] - round_list[0]
    if int(user_answer) == real_answer:
      print 'Great!\n'
      return True, question, user_answer, real_answer
    else:
      print 'Sorry, the right answer was %s\n' % (real_answer)
      return False, question, user_answer, real_answer

def GetAnswer(question):
  while True:
    print question
    user_answer = raw_input('What is the answer?\n')
    try:
      int(user_answer)
      return user_answer
    except:
      continue
