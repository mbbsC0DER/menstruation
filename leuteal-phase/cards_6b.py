import random

# Create suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']

# Create the deck
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(rank + ' of ' + suit)

# Display original deck
print("Original Deck:")
print(deck)

# Shuffle the deck
random.shuffle(deck)

# Display shuffled deck
print("\nShuffled Deck:")
for card in deck:
    print(card)