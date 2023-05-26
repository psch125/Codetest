import collections
import itertools
import random
from random import choice
from typing import Any
from collections import Counter

def quick_sort(array):
    array = [int(i) for i in array]
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def find_duplicates(list1):
    counter = Counter(list1)
    element = 0
    for key, value in counter.items():
        if value > 1:
            element += 1
    
    return element

def get_connected_numbers(numbers):
    numbers = [int(i) for i in numbers]
    sorted_numbers = sorted(numbers)  # 숫자를 정렬하여 연속성을 확인하기 위함
    
    count = 0
    number_list = []
    for i in range(len(sorted_numbers)-1):
        if sorted_numbers[i]+1 == sorted_numbers[i+1]:
            number_list.append(sorted_numbers[i])
            count += 1
        else:
            if 0 < i < 4:
                return None
               
    if count == 5:
        return sorted_numbers[1:]     
    
    if count == 4:
        number_list.append(number_list[-1]+1)
        return number_list  
   
Card = collections.namedtuple('Card',['rank','suit']) 


class FrenchDeck :
    # ranks = [str(n) for n in range(2,11)] + list('JQKA')
    ranks = [str(n) for n in range(1, 14)]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) :
        self._cards = [Card(rank ,suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self) :
        return len(self._cards)

    def __getitem__(self,position) :
        return self._cards[position]

methodName = ['_isRoyalStraightFlush', '_isStraightFlush', '_isFourCard', '_isFullHouse', '_isMountain',
                    '_isBackStraight','_isStraight','_isTriple','_isTwoPair','_isOnePair','_isTop']

class SixPOKER:
    def __init__(self, card_list):
        self.card_list = card_list
        self.status = False
        self.suit_value = [card.suit for card in self.card_list]
        self.rank_value = [card.rank for card in self.card_list]
        # print('rank_value :', self.rank_value)
        # print('suit_value :', self.suit_value)
        
    def check(self):
        for method_name in methodName:
            method = getattr(self, method_name)
            answer = method()
            if self.status == True:
                return answer
    
    def _isTop(self):
        self.status = True
        # print('Your Card is Top')
        return 'Top'
        
    def _isOnePair(self):
        value = set(self.rank_value)
        if len(value) == 5:
            self.status = True
            return 'OnePair'
    
    def _isTwoPair(self):
        value = set(self.rank_value)
        duplicate = find_duplicates(self.rank_value)
        if len(value) == 4 and duplicate == 2:
            self.status = True
            # print('Your Card is TwoPair')
            return 'TwoPair'
    
    def _isTriple(self):
        value = set(self.rank_value)
        duplicate = find_duplicates(self.rank_value)
        if len(value) == 4 and duplicate == 1:
            self.status = True
            # print('Your Card is Triple')
            return 'Triple'
            
    def _isStraight(self):
        connected_number = get_connected_numbers(self.rank_value)
        if connected_number is not None:
            self.status = True
            # print('Your Card is Straight')
            return 'Straight'
          
    def _isBackStraight(self):
        if '1' in self.rank_value and '2' in self.rank_value and '3' in self.rank_value and '4' in self.rank_value and '5' in self.rank_value:
            self.status = True
            # print('Your Card is BackStraight')
            return 'BackStraight'
            
    def _isMountain(self):
        if '1' in self.rank_value and '10' in self.rank_value and '11' in self.rank_value and '12' in self.rank_value and '13' in self.rank_value:
            self.status = True
            # print('Your Card is Mountain')
            return 'Mountain'
                  
    def _isFlush(self):
        value = set(self.suit_value)
        duplicate = find_duplicates(self.suit_value)
        if len(value) == 1 or (len(value) == 2 and duplicate == 1):
            self.status = True
            # print('Your Card is Flush')
            return 'Flush'
        
    def _isFullHouse(self):
        value = set(self.rank_value)
        duplicate = find_duplicates(self.rank_value)
        if len(value) == 2 or (len(value) == 3 and duplicate == 2):
            self.status = True
            # print('Your Card is FullHouse')   
            return 'FullHouse'               
            
    def _isFourCard(self):
        counter = Counter(self.rank_value)
        for key, value in counter.items():
            if value == 4:
                self.status = True
                # print('Your Card is FourCard')
                return 'FourCard'

          
    def _isStraightFlush(self):
        connected_number = get_connected_numbers(self.rank_value)
        if connected_number is not None:
            index_list = [self.rank_value.index(str(i)) for i in connected_number]
            suit = set([self.suit_value[i] for i in index_list])
            if len(suit) == 1:
                self.status = True
                # print('Your Card is StraightFlush')
                return 'StraightFlush'
        
    def _isRoyalStraightFlush(self):
        if '1' in self.rank_value and '2' in self.rank_value and '3' in self.rank_value and '4' in self.rank_value and '5' in self.rank_value:
            get_index = [self.rank_value.index(i) for i in self.rank_value if i == '1' or 
                                                        i == '2' or
                                                        i == '3' or
                                                        i == '4' or
                                                        i == '5']
            
            suit = set([self.suit_value[i] for i in get_index])
            if len(suit) == 1:
                self.status = True
                # print('Your Card is RoyalStraightFlush')         
                return 'RoyalStraightFlush'

methodName = ['_isRoyalStraightFlush', '_isStraightFlush', '_isFourCard', '_isFullHouse', '_isMountain',
                    '_isBackStraight','_isStraight','_isTriple','_isTwoPair','_isOnePair','_isTop']

result_dict = {'Top' :  0,
            'OnePair' : 0,
            'TwoPair' : 0,
            'Triple' : 0,
            'Straight' : 0,
            'BackStraight' : 0,
            'Mountain' : 0,
            'FullHouse' : 0,
            'FourCard' : 0,
            'StraightFlush' : 0,
            'RoyalStraightFlush' : 0}


def print_combinations(cards, combination, start):
    if len(combination) == num_combinations:
        result = SixPOKER(combination).check()
        # print(result)
        if result in result_dict:
            result_dict[result] += 1
        return
    for i in range(start, num_cards):
        print_combinations(cards, combination + [cards[i]], i + 1)

if __name__ == '__main__':
    
    deck = FrenchDeck()
    cards = deck._cards
    
    num_cards = len(cards)
    num_combinations = 6
    print_combinations(cards, [], 0)
    
    print(result_dict)
    
    '''
    {'Top': 6799696, 
    'OnePair': 9844224, 
    'TwoPair': 2471040, 
    'Triple': 732160, '
    Straight': 248880, 
    'BackStraight': 40278, 
    'Mountain': 40432, 
    'FullHouse': 165984, 
    'FourCard': 14664, 
    'StraightFlush': 1004, 
    'RoyalStraightFlush': 158}
    '''



        
    

