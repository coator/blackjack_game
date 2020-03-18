import random


class CardLayout():
    def __init__(self, dealtcard):
        self.dealtcard = dealtcard

    def __str__(self):
        print("______")
        print("|   |")
        print("|{} {}|".format(self.dealtcard[0], self.dealtcard[1]))
        print("|   |")
        return ("______")


class CreateCardDeck:

    def __init__(self, deckamt=1):
        deck = []
        self.deckamt = deckamt

    def GenerateDeck(self, deckamt=1):
        deck = []
        hand = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        suit = ('♠', '♥', '♦', '♣')
        for decks in range(0, deckamt):
            for x in suit:
                for card in range(0, len(hand)):
                    deck.append((hand[card], x))
        return deck

    def __len__(self):
        deck = CreateCardDeck().GenerateDeck()
        return len(deck)


def starting_proc():
    name = str(input('What is your name '))
    if name == '':
        name = 'but cxhung'
    bank_balance = 0

    while bank_balance == 0:
        try:
            bank_balance = int(input('How much is your balance? (Please only input numbers) '))
        except:
            print('Please only type numbers.')

    gamestart = 'N'

    while gamestart != 'Y':
        gamestart = input('Your current bank balance is ${:0,.2f}, Would you like to play a game? \
        Y/N '.format(bank_balance)).capitalize()
        if gamestart == 'N':
            exit()
        else:
            return name, bank_balance


def activehand(totalcardsdealt):
    if amt_being_dealt == 0:
        return 0
    else:
        totalcardsdealt += amt_being_dealt
        return totalcardsdealt


def cardviewer(deck, amt_being_dealt, totalcardsdealt):
    total = 0
    print('the total cards dealt are {}'.format(totalcardsdealt))
    for x in range(amt_being_dealt):
        cardinfo = deck.pop()
        print(CardLayout(cardinfo))
        try:
            x = (cardinfo[0])
            int(x)
            total += int(x)
        except:
            if x in (['K', 'Q', 'J']):
                total += 10
            elif x == 'A' and totalcardsdealt == 2:
                total += 11
            elif x == 'A' and totalcardsdealt >= 3:
                total += 1
            else:
                print('it has esled')
                pass
    print('__________________________________________________________________')
    return total


def wager(bank):
    while True:
        if bank==0:
            print('sorry you are broke and must leave')
            exit()
        wager = int(input('how much would you like to wager? '))
        if wager > bank:
            print('error, cannot wager more than available balance, please try again')
        else:
            return wager


def dealer(wholedeck):
    totalcardsdealt = 2
    dealer_hand = cardviewer(wholedeck, 2, totalcardsdealt)
    if dealer_hand == 21:
        print('Dealer has 21!!')
        return dealer_hand
    while dealer_hand < 17:
        totalcardsdealt += 1
        dealer_hand += cardviewer(wholedeck, 1, totalcardsdealt)
    if dealer_hand > 21:
        print('dealer has a {} and busted!'.format(dealer_hand))
        return dealer_hand
    print('dealer has a ', dealer_hand)
    return dealer_hand


def endgameeval(dealertotal, playertotal, bet,bankbalance,wholedeck):
    print('You have {} and dealer has {}'.format(playertotal, dealertotal))
    if dealertotal < playertotal:
        print('you won ${:0,.2f}!'.format(bet))
        bankbalance=bankbalance+(bet*2)
    elif dealertotal == playertotal:
        print('push, no one wins')
    elif dealertotal > playertotal:
        print('you lost your bet of  ${:0,.2f}'.format(bet))
    print('Your new balance is ${:0,.2f}'.format(bankbalance))
    q = input('would you like to play again? Y/N')
    if q.capitalize()[0] == 'Y':
        gameplay(bankbalance, wholedeck, 0)
    else:
        exit()


def gameplay(bankbalance, wholedeck, totalcardsdealt):
    gameactive = True
    while gameactive:
        # this is the initial deal from the deck.
        ##I need to program is the deck runs out lol
        bet = wager(bankbalance)
        bankbalance -= bet
        totalcardsdealt += 2
        total = cardviewer(wholedeck, 2, totalcardsdealt)
        # hitstand method
        play = True
        while play == True:
            if total == 21:
                break
            elif total > 21:
                total=0
                break
            else:
                pass
            hit_stand = input(('Your Current Hand Value is {} would you like to hit or stand? H/S'.format(total)))
            if hit_stand.capitalize()[0] == 'H':
                totalcardsdealt += 1
                total += cardviewer(wholedeck, 1, totalcardsdealt)
            elif hit_stand.capitalize()[0] == 'S':
                play = False
        dealertotal = dealer(wholedeck)
        endgameeval(dealertotal, total, bet, bankbalance,wholedeck)


info = starting_proc()
deck = CreateCardDeck().GenerateDeck()
deck = (random.sample(deck, len(deck)))
gameplay(info[1], deck, 0)
