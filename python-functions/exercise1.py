# def say_hello(name='World', greeting=None):
#     if greeting == None:
#         print(f'Hello {name}!')
#     else:
#         print(f'{greeting} {name}!')


# say_hello()
# say_hello('Bob')
# say_hello(greeting='Howdy')
# say_hello('Bob', 'Howdy')

# def create_deck():
#     suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
#     ranks = ["2", "3", "4", "5", "6", "7", "8",
#              "9", "10", "Jack", "Queen", "King", "Ace"]
#     deck = []

#     for suit in suits:
#         for rank in ranks:
#             deck.append(f'{rank} of {suit}')

#     return deck


# my_deck = create_deck()
# print(len(my_deck))

# value = 1


# def some_function():
#     value = 10
#     return value


# print(some_function())

def print_keyword_args(**kwargs):

    third = kwargs.get('third', None)
    if third != None:
        print('third arg =', third)


print_keyword_args(first='a')
print_keyword_args(first='b', second='c')
print_keyword_args(first='d', second='e', third='f')
