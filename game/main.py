import random

options = ('piedra', 'tijera', 'papel')
computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  print('computer_wins ', computer_wins)
  print('user_wins ', user_wins)
  user_option = input('piedra, papel o tijera: ')
  user_option = user_option.lower()
  
  
  if not user_option in options:
    print('esa opcion no es valida')
    continue
  rounds += 1

  computer_option = random.choice(options)

  print('User option: ', user_option)
  print('Computer option: ', computer_option)

  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computador gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computador gano!')
      computer_wins += 1
  if computer_wins == 2:
    print('el ganador es computadora')
    break
  if user_wins == 2:
    print('el ganador es usuario')
    break
  
