import random
'''
def genRandInt():
    number=random.randint(1,52)
    return(number)
'''
def genUnshuffledCards():
    cardNumbers=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    cardSuites=['Spades','Clubs','Hearts','Diamonds']
    unshuffledDeck=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    #print(len(unshuffledDeck))
    k=0
    for i in cardSuites:
        for j in cardNumbers:
            unshuffledDeck[k]=str(j)+' of '+str(i)
            #print(k)
            k=k+1
    return(unshuffledDeck)
def shuffleDeck(deckOfCards):
    shuffledDeck=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    m=0
    for card in deckOfCards:
        for n in range(52):
            m=random.randint(0,51)
            if(shuffledDeck[m]==''):
                shuffledDeck[m]=card
                break
            else:
                m=random.randint(0,51)
    return(shuffledDeck)
originalDeck=genUnshuffledCards()
print('Without shuffling the deck, the results are as follows:')
for elem in originalDeck:
    print(elem)
#print(shuffleDeck(originalDeck))
shuffleddDeck=shuffleDeck(originalDeck)
#print(len(shuffleddDeck))
print('After shuffling the deck 1 time, the results are as follows:')
for ele in shuffleddDeck:
    print(ele)
shuffleddDeck=shuffleDeck(originalDeck)
print('After shuffling the deck 2 times, the results are as follows:')
for elemm in shuffleddDeck:
    print(elemm)
#print(len(shuffleddDeck))
for o in range(998):
    shuffleddDeck=shuffleDeck(originalDeck)
print('After shuffling the deck 1000 times, the results are as follows:')
for elemmm in shuffleddDeck:
    print(elemmm)
