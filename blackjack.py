import random
#import copy
#original_deck=['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
class Deck:
	def __init__(self):
		#self.cards=original_deck
		self.cards=['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
		random.shuffle(self.cards)
	def deal(self):
		return self.cards.pop()
	#def collect(self):
	#	self.cards=original_deck
	#	random.shuffle(self.cards)

class Player:
	def __init__(self,name,deck):
		self.name=name
		self.hand=[deck.deal(),deck.deal()]
		self.money=100
		#self.hand_value=self.get_hand_value()
	def get_hand_value(self):
		val=0
		for card in self.hand:
			if card=='A':
				continue
			elif card=='J' or card=='Q' or card=='K':
				val+=10
			else:
				val+=int(card)
		for card in self.hand:
			if card=='A':
				if val<=10:
					val+=11
				else:
					val+=1
		return val
	def hit(self):
		self.hand.append(deck.deal())
		print(self)
	def __str__(self):
		return f'{self.name}:\n {self.hand}\n value : {self.get_hand_value()}'
	

class Dealer:
	def __init__(self,name,deck):
		self.name=name
		self.hand=[deck.deal(),deck.deal()]
		#self.hand_value=self.get_hand_value()
	def get_hand_value(self):
		val=0
		for card in self.hand:
			if card=='A':
				continue
			elif card=='J' or card=='Q' or card=='K':
				val+=10
			else:
				val+=int(card)
		for card in self.hand:
			if card=='A':
				if val<=10:
					val+=11
				else:
					val+=1
		return val
	def hit(self):
		self.hand.append(deck.deal())
		print(self)
	def show(self):
		print(f'{self.name}:\n {self.hand[0]}')

	def __str__(self):
		return f'{self.name}:\n {self.hand}\n value : {self.get_hand_value()}'
def bust(player):
	return player.get_hand_value()>21
def check_blackjack(player):
	return 'A' in  player.hand and ('10' in player.hand or 'J' in player.hand or 'Q' in player.hand or 'K' in player.hand)


if __name__ == '__main__':
	name=input("what's your name? ")
	while True:
		deck=Deck()
		player=Player(name,deck)
		print(player)
		dealer=Dealer('dealer',deck)
		dealer.show()
		choice=''
		if check_blackjack(player):
			print(f"Wow {player.name} you've got a Blackjack...!!!")
			print(dealer)
			if check_blackjack(dealer):
				print("Dealer also has a Blackjack !\nIt's a push")
			else:
				print('You win !')
		else:

			while bust(player)==False:
				choice=input('press h for hit or s for stand: ')
				if choice.lower()=='s':
					break
				player.hit()
			if bust(player):
				print(f'{player.name} you are busted !\ndealer wins !')
			else:
				print(dealer)
				while dealer.get_hand_value()<17:
					dealer.hit()
				if bust(dealer):
					print('dealer busted !\nYou win !')
				elif player.get_hand_value()>dealer.get_hand_value():
					print('You win !')
				elif player.get_hand_value()==dealer.get_hand_value():
					print("It's a push !")
				else:
					print("dealer wins")
		quit=input('Press q to quit : ')
		if quit=='q':
			break
		#deck.collect()
		#print(len(deck.cards))
		#print(len(original_deck))
