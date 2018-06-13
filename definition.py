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
        pass