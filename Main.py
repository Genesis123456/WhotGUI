from random import shuffle
from random import choice
from ImageCopy import images
import tkinter as tk

class Whot(images):
    'A Game of cards usually involving two players by default see manual for more info'
    def __init__(self):
        super().__init__()
        
    def InitDepot(self):
        Whot.Cards = self._DepotMarket.copy()
        shuffle(Whot.Cards)
        #return Whot.Cards

    def NormCards(self):
        'Normalize the cards if startcard has whot 20 in it'
        if self.PlayedCards()[len(self.PlayedCards())-1][1][1] == 20:
            try:
                misc_cards = []
                for i in Whot.Cards[0], Whot.Cards[1], Whot.Cards[2], Whot.Cards[3]:
                    misc_cards.append(i)
                    Whot.Cards.remove(i)
                shuffle(misc_cards)
                self.PlayedCards().append(choice(misc_cards))
                self.NormCards()
            except:
                pass
            
        
    def InitPlayerCards(self):
        'Initialize player cards and Starting (played) cards'
        self._startcard1 = []
        self._startcard2 = []
        for i in Whot.Cards[0], Whot.Cards[1], Whot.Cards[2], Whot.Cards[3], Whot.Cards[4]:
            self._startcard1.append(i)
            Whot.Cards.remove(i)
        for i in Whot.Cards[5], Whot.Cards[6], Whot.Cards[7], Whot.Cards[8], Whot.Cards[9]:
            self._startcard2.append(i)
            Whot.Cards.remove(i)
        self.PlayedCards().append(Whot.Cards[10])
        Whot.Cards.pop(10)
        #self._completed = []
        pass

    def LoopDepot(self):
        'Loops depot cards if they are less than or equal to 14'
        if len(Whot.Cards) <= 14:
            self.InitDepot()


    def PlayedCards(self, cards=[]):
        'Returns the played cards in a nested tuple'
        return cards

    def InitComputerCards(self):
        'Initializes the cards for Player1 (computer) to start'
        global card1
        card1 = self._startcard1

    def InitPlayer2Cards(self):
        'Initializes the cards for Player2 to start'
        global card2
        card2 = self._startcard2
        
    def ComputerCards(self):
        for i in card1:
            print( i[1])
        #return card1

    def Player2Cards(self):
        for i in card2:
            print( i[1])
        #return card2
    
class Computer(Whot):
    'Objects and attributes for Player1'
    def __init__(self):
        super().__init__()
        self.compup2=[0]
        self.compup8=[0]
        self.compup1=[0]
        self.compup14=[0]
        self.compup20=[0]

    def play(self, playcard):
        'Player1 Plays a valid card in his/her cardstack'
        self.LoopDepot()
        if playcard in self.cards():
            if playcard[1][0] == self.PlayedCards()[len(self.PlayedCards())-1][1][0] or\
               playcard[1][1] == self.PlayedCards()[len(self.PlayedCards())-1][1][1] or\
               playcard[1][1] == 20 or self.PlayedCards()[len(self.PlayedCards())-1][1][1] == 20:
                print(playcard[1], "Has been played")
                if playcard[1][1] == 2:
                    self.compup2.insert(0,2)
                    print('Pick Two Cards')
                elif playcard[1][1] == 1:
                    self.compup1.insert(0,1)
                    print('Hold On')
                elif playcard[1][1] == 8:
                    self.compup8.insert(0,8)
                    print("Hold On")
                elif playcard[1][1] == 14:
                    self.compup14.insert(0,14)
                    print("General Market")
                elif playcard[1][1] == 20:
                    self.compup20.insert(0,20)
                    print('Ask for a card...')
                self.PlayedCards().append(playcard)
                self.cards().remove(playcard)
                if len(self.cards()) == 1:
                    print("Last Card")
                elif len(self.cards()) == 0:
                    print("Checkmate.....!")
                return True
            else:
                raise WhotException("Error: Invalid Move!")
        else:
            raise WhotException("Error: Playcard is not in your cardstack!")

    def cards(self):
        "returns player1's (computer) cards"
        return card1

    def gomart(self):
        'Sends Player1 to Market'
        self.LoopDepot()
        self.cards().append(Whot.Cards[11])
        Whot.Cards.remove(Whot.Cards[11])

    def gogenmart(self):
        "General market"
        self.LoopDepot()
        self.cards().append(Whot.Cards[12])
        Whot.Cards.remove(Whot.Cards[12])

class Player2(Whot):
    'Objects and attributes for Player2'
    def __init__(self):
        super().__init__()
        self.player2up2=[0]
        self.player2up1=[0]
        self.player2up8=[0]
        self.player2up14=[0]
        self.player2up20=[0]
        
        self.check_requested = None
        self.request = None
        
    def play(self, playcard):
        'Player2 Plays a valid card in his/her cardstack'
        self.LoopDepot()
        if playcard in self.cards():
            if playcard[1][0] == self.PlayedCards()[len(self.PlayedCards())-1][1][0] or\
               playcard[1][1] == self.PlayedCards()[len(self.PlayedCards())-1][1][1] or\
               playcard[1][1] == 20 or self.PlayedCards()[len(self.PlayedCards())-1][1][1] == 20:
                if self.check_requested:
                    if self.request != playcard[1][0] and playcard[1][1] != 20:
                        raise WhotException("Concur to your opponents request")
                print(playcard[1], "Has been played")
                if playcard[1][1] == 2:
                    self.player2up2.insert(0,2)
                    print('Pick Two Cards')
                elif playcard[1][1] == 1:
                    self.player2up1.insert(0,1)
                    print('Hold On')
                elif playcard[1][1] == 8:
                    self.player2up8.insert(0,8)
                    print("Hold On")
                elif playcard[1][1] == 14:
                    self.player2up14.insert(0,14)
                    print("General Market")
                elif playcard[1][1] == 20:
                    self.player2up20.insert(0,20)
                    print('Ask for a card...')
                self.PlayedCards().append(playcard)
                self.cards().remove(playcard)
                self.check_requested = None
                self._request = None
                if len(self.cards()) == 1:
                    print("Last Card")
                elif len(self.cards()) == 0:
                    print("Checkmate.....!")
                return True
            else:
                raise WhotException("Error: Invalid Move!")
        else:
            raise WhotException("Error: Playcard is not in your cardstack!")

    def cards(self):
        "returns Player2's cards"
        return card2

    def gomart(self):
        "Sends player2 to market"
        self.LoopDepot()
        self.cards().append(Whot.Cards[13])
        Whot.Cards.remove(Whot.Cards[13])

    def gogenmart(self):
        "Gen market"
        self.LoopDepot()
        self.cards().append(Whot.Cards[14])
        Whot.Cards.remove(Whot.Cards[14])

class WhotException(Exception):
    "Exception for the Whot class"
    def __init__(self, message):
        self.message = message
        self.run()
    def run(self):
        'Return the message'
        return self.message

if __name__ == '__main__':
    yap = tk.Tk()
    app = Whot()
    #app.Init()
    app.InitDepot()
    app.InitPlayerCards()
    app.InitComputerCards()
    app.InitPlayer2Cards()
    app.NormCards()
    p1 = Computer()
    p2 = Player2()
    pc1 = p1.ComputerCards
    pc2 = p2.Player2Cards
    
    #WG(yap)
