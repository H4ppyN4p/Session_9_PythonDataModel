class Deck:

    def __init__(self):
        self.items = {
            'cards': ['A', 'K', 4, 7]
            }

    def __setitem__(self, key, newValue):
        if key=='cards' and newValue != None:
            self.items[key].append( newValue)

    def __getitem__(self, key):
        return self.items[key]        

    def __str__(self):
        return f'cards in deck: {self.__getitem__("cards")}'
    
    
    def __len__(self):
        return len(self.__getitem__('cards'))
    
    def __add__(self, other):
        newDeck = (self.__getitem__('cards') + other.__getitem__('cards'))
        return newDeck
    
    def addCard(self, value):
        self.__setitem__('cards', value)


deck1 = Deck()
deck2 = Deck()

#ToString method implement
print(deck1)

#Len method implemented
print(len(deck1))

#Add method to add two decks together
print(deck1 + deck2)

#Using setitem magic method
deck1.addCard(9)

print(deck1)