import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        pass
    
    def __str__(self):
        return (f"{self.rank} of {self.suit}")
        pass

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                pass
    
    def __str__(self):
        string = ""
        for c in self.deck:
            string += (f"{c.rank} of {c.suit}\n")
        return string
        pass

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card = self.deck.pop(0)
        #print (card)
        return card
        pass

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        pass
    
    def get_value(self):
        self.value = 0
        has_ace = 0
        for card in self.cards:
            #print (f"{card} has value {values.get(card.rank)}")
            self.value += values.get(card.rank)
            if card.rank == 'Ace':
                has_ace += 1
        while has_ace > 0 and self.value > 21:
            self.value -= 10
            has_ace -= 1
        return self.value
        pass
 
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        #print(f"winning, before adding, total is {self.total}, bet is {self.bet}")
        self.total += (self.bet * 2)
        self.bet = 0
        #print(f"winning, after adding, total is {self.total}, bet is {self.bet}")
        pass
    
    def lose_bet(self):
        #print(f"lossing, before adding, total is {self.total}, bet is {self.bet}")
        #self.total -= self.bet
        self.bet = 0
        #print(f"lossing, after adding, total is {self.total}, bet is {self.bet}")
        pass


def take_bet(chips):
    while True:
        try: 
            new_bet = int(input(f"How much would you like to bet on? Your current bet is {chips.bet} and you have {chips.total} chips. "))
        except:
            print ("Not a valid entry, please enter an integer.")
            continue
        if new_bet > chips.total:
            print ("Your bet is over you available chips.")
            continue
        chips.total -= new_bet
        print (f"new total chips is {chips.total}")
        chips.bet += new_bet
        print (f"current bet is {chips.bet}")
        break    
    pass

def hit(deck,hand):
    #print ("Hit is called.")
    hand.add_card(deck.deal())
    #print (hand.cards[0])
    pass

def hit_or_stand(deck,hand):
    global hitting
    print (f"Your hand has {hand.get_value()}.")
    play_ans = input("Hit(h) or Stand(s): ")
    if not play_ans.lower() in ("h","s"):
        print("Not valid input.")
    elif play_ans.lower() == "h":
        hitting = True
        hit(deck,hand)
    else:
        hitting = False

def show_some(player,dealer):
    player_hand = ""
    for card in player.cards:
        player_hand += (f"{card.rank} of {card.suit},") 
    print (f"Player's hand: {player_hand}")
    print (f"Player's value is {player.get_value()}")
    dealer_hand = "hidden, "
    for card in dealer.cards[1:]:
        #print (type(card))
        dealer_hand += (f"{card.rank} of {card.suit},")
    print (f"Dealer's hand: {dealer_hand}")
    pass
    
def show_all(player,dealer):
    player_hand = ""
    for card in player.cards:
        player_hand += (f"{card.rank} of {card.suit},") 
    print (f"Player's hand: {player_hand}")
    print (f"Player's value is {player.get_value()}")
    dealer_hand = ""
    for card in dealer.cards:
        dealer_hand += (f"{card.rank} of {card.suit},")
    print (f"Dealer's hand: {dealer_hand}")
    print (f"Dealer's value: {dealer.get_value()}")
    pass

def player_busts(hand):
    print (f"Busted!! Your total value is {hand.get_value()}")
    pass

def player_wins(player, dealer,chips):
  show_all(player,dealer)
  print (f"You win!!! You have {player.get_value()} and the dealer has {dealer.get_value()}")
  chips.win_bet()
  chips.bet = 0

def dealer_busts(hand):
    print (f"Dealer busted!! Dealer total value is {hand.get_value()}")
    pass
    
def dealer_wins(player, dealer,chips):
  show_all(player,dealer)
  print (f"You lose!! Dealer has {dealer.get_value()} and you have {player.get_value()}")
  chips.lose_bet()
  chips.bet = 0
    
    
def push(chips):
    if chips.total <= 0:
        print ("Game Over")
        return True
    return False
    pass


# Print an opening statement
#new game
print ("Welcome to Black-Jack game!!")
playing_game = True
# Set up the Player's chips
player_chip = Chips()
print (f"Your initial chip amount is {player_chip.total}.")

  
  
# Create & shuffle the deck, deal two cards to each playe
#new session
playing = True
while playing:

  print ("-------------------------")
  game_deck = Deck()
  game_deck.shuffle()
	#print(game_deck)

  player = Hand()
  dealer = Hand()
  
  hit(game_deck,player)
  hit(game_deck,player)
  hit(game_deck,dealer)
  hit(game_deck,dealer)
  
  
      
  
  
  # Prompt the Player for their bet
  take_bet(player_chip)
  
  # Show cards (but keep one dealer card hidden)
  

  hitting = True
  while hitting:  # recall this variable from our hit_or_stand function
    # Prompt for Player to Hit or Stand
    show_some(player,dealer)
    hit_or_stand(game_deck,player)
    
    # Show cards (but keep one dealer card hidden)
     
    # If player's hand exceeds 21, run player_busts() and break out of loop
    if player.get_value() > 21:
      player_busts(player)
      dealer_wins(player,dealer,player_chip)
      break
      
  # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
  if player.get_value() <= 21:

    while dealer.get_value() < 17:
          hit(game_deck,dealer)

    if dealer.get_value() > 21:
	    dealer_busts(dealer)
	    player_wins(player,dealer,player_chip)
    elif player.get_value() > dealer.get_value():
	    player_wins(player,dealer,player_chip)
    else:
	    dealer_wins(player,dealer,player_chip)

  # update chips
  # prompt for another game
  if player_chip.total <= 0:
    print ("You don't have any more chips. \nGame Over!")
    playing_game = False
    break
  else:
    print (f"Your new chip total is {player_chip.total}")
    while True:
      session_input = input(f"Would you like another game: ('Y' or 'N')")
      if session_input.lower() == 'y':
        playing = True
        break
      elif session_input.lower() == 'n':
        playing = False
        break
      else:
        print ("Invalid input, please enter 'Y' or 'N'")


