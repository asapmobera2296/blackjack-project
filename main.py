############### Blackjack Project #####################
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """returns random card from deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(cards):
  """Take the cards and returns the calculated score of the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

  
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw :("
  elif computer_score == 0:
    return "You lost computer has blackjack"
  elif user_score == 0:
    return "Win with a blackjack!"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Opponent went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose :/"

  

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_gameover = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_gameover:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_gameover = True
    else:
      user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_gameover = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
  
