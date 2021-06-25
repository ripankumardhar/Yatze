"""
Yatze!
"""

import operator
import pprint
from collections import namedtuple
from random import randint, shuffle
from collections import Counter

"""
Defining necessary functions
"""


def roll_die():
    """
    Dice rolling function using generator
    """
    for _ in iter(int, 1):  # Infinite generator loop
        yield randint(1, 6)


def count_element(i, dices):
    """
    Counts apperence of an score in rolled dices
    """
    counter = Counter(dices)
    return counter.get(i, 0)


def aces(dices):
    """
    Counts apperence of one's
    """
    return 1 * count_element(1, dices)


def twos(dices):
    """
    Counts apperence of two's
    """
    return 2 * count_element(2, dices)


def threes(dices):
    """
    Counts apperence of three's
    """
    return 3 * count_element(3, dices)


def fours(dices):
    """
    Counts apperence of four's
    """
    return 4 * count_element(4, dices)


def fives(dices):
    """
    Counts apperence of five's
    """
    return 5 * count_element(5, dices)


def sixes(dices):
    """
    Counts apperence of six's
    """
    return 6 * count_element(6, dices)


def pair(dices):
    """
    Counts scores of highest pair
    """
    ce = Counter(dices)
    pairs = sorted([index for index, value in ce.items() if value >= 2])

    if pairs:
        return pairs[-1] * 2

    return 0


def two_pairs(dices):
    """
    Counts scores of two pairs
    """
    ce = Counter(dices)
    total = 0

    for index, value in ce.items():
        if value >= 4:
            total = 4 * index
            break

        if value >= 2:
            total += index * 2

    return total


def three_of_a_kind(dices):
    """
    Counts scores of three of a kind
    """
    ce = Counter(dices)
    indexes = [index for index, value in ce.items() if value >= 3]

    if indexes:
        return indexes[0] * 3

    return 0


def four_of_a_kind(dices):
    """
    Counts scores of four of a kind
    """
    ce = Counter(dices)
    indexes = [index for index, value in ce.items() if value >= 4]

    if indexes:
        return indexes[0] * 4

    return 0


def full_house(dices):
    """
    Counts scores of full house
    """
    ce = Counter(dices)
    pair = None
    triple = None

    for index, value in ce.items():
        if value == 2:
            pair = index

        if value == 3:
            triple = index

    if pair and triple:
        return (pair * 2) + (triple * 3)

    return 0


def low_straight(dices):
    """
    Counts scores of lower stright
    """
    if sorted(dices) == [1, 2, 3, 4, 5]:
        return 15

    return 0


def high_straight(dices):
    """
    Counts scores of higher stright
    """
    if sorted(dices) == [2, 3, 4, 5, 6]:
        return 20

    return 0


def chance(dices):
    """
    Counts scores of chances
    """
    return sum(dices)


def yahtzee(dices):
    """
    Counts scores of a yahtzee
    """
    if len(list(set(dices))) == 1:
        return 50

    return 0


"""
Defining necessary variable and creating players
"""

total_number_of_turns = 15

# Blank scoring pad
scoring_pad = {
    'aces': None,
    'twos': None,
    'threes': None,
    'fours': None,
    'fives': None,
    'sixes': None,
    'pair': None,
    'two_pairs': None,
    'three_of_a_kind': None,
    'four_of_a_kind': None,
    'full_house': None,
    'low_straight': None,
    'high_straight': None,
    'chance': None,
    'yahtzee': None
}

labels = {
    'aces': "Try to get one's as much as possible.",
    'twos': "Try to get two's as much as possible.",
    'threes': "Try to get three's as much as possible.",
    'fours': "Try to get four's as much as possible.",
    'fives': "Try to get five's as much as possible.",
    'sixes': "Try to get six's as much as possible.",
    'pair': "Try to get a pair.",
    'two_pairs': "Try to get two pair.",
    'three_of_a_kind': "Try to get a three of a kind.",
    'four_of_a_kind': "Try to ge a four of a kind.",
    'full_house': "Try to get a full house.",
    'low_straight': "Try to get a low straight",
    'high_straight': "Try to get a high straight",
    'chance': "This is a chance!",
    'yahtzee': "Try to get yahtzee"
}


# Player blueprint
player = namedtuple(
    'Player',
    ['name', 'scoring_pad', 'dices'],
    defaults=[[roll_die() for i in range(5)]]
)

# List of all the player inserted
player_list = []


# Take player name and creates player using blueprint
print("Enter player name before starting game. If you enter `start` as a player's name, the game will be started.\n")
while True:
    name = input("Enter a player name:\n")

    if name == 'start' or name == 'Start':
        if len(player_list) == 0:
            print("You have to provide atleast one user. \n")
            continue
        else:
            break

    player_list.append(player(name, scoring_pad.copy()))


# Shuffling players randomly
shuffle(player_list)
print("\nGame Started!\n")


"""
Started Playing
"""

for cat in scoring_pad.keys():  # For each category
    for player_index, player in enumerate(player_list):  # For each player
        turn = 0
        keep = []  # Array to store decided dice scores
        scores = player.scoring_pad
        array_of_user_dices = [roll for roll in player.dices]
        poped_dices = []
        print(labels.get(cat, None))
        print("Player: ", player.name, "\n")
        print("\n")
        print("Rolling dices...\n")

        while turn < 3:
            # Using geneator to throw dice
            dice_rolls = [next(roll) for roll in array_of_user_dices]
            turn = turn + 1
            print("\n", dice_rolls, "\n")

            if turn == 3:  # Checks if 3 turn is completed
                keep = keep + dice_rolls
                break

            while True:
                try:
                    if len(keep) > 0:
                        print("Options: \n", "1. I'm happy with this \n", "2. I want to choose \n", "3. Re-roll all\n", "4. Keep this roll and re-roll previously kept dices\n")
                    else:
                        print("Options: \n", "1. I'm happy with this \n", "2. I want to choose \n", "3. Re-roll all\n")
                    
                    choice = int(input("Select Options: "))
                    break
                except Exception as e:
                    print("Error: ", str(e))
                    print("Try again with valid input.")
                    continue

            if choice == 1:  # Keeps all scores after throwing dice
                keep = keep + dice_rolls
                break
            elif choice == 2:  # Keeps selected scores after throwing dice, re-throw others
                while True:
                    try:
                        print("Select the index of dices you want to choose seperated by spaces: \n")
                        indexes = list(map(int, input().split()))

                        for i in indexes:
                            # Keeping selected scores
                            keep.append(dice_rolls[i])
                            # Removing dices whose scores are taken in keep
                            poped_dices.append(array_of_user_dices.pop())

                        print("Selected dices:", keep, "\n")
                        print("Re-rolling remaining dices \n")
                        break
                    except Exception as e:
                        print("Error : ", str(e))
                        print("Try again with valid input.")
                        continue
            elif choice == 3:  # Re-throw all dices
                print("Re-rolling remaining dices \n")
                continue
            elif choice == 4:
                keep = dice_rolls
                array_of_user_dices = poped_dices
            else:
                print("Invalid option Choose option between 1 - 3 \n")

        print("\nFinal result", keep, "\n")
        res = globals()[cat](keep)
        scores[cat] = res
        player_list[player_index] = player_list[player_index]._replace(scoring_pad=scores)  # Replacing old scorepad with updated one
        
        print(player.scoring_pad)
        print("\n")

"""
Show Result
"""
results = {}

for player in player_list:
    total = 0
    for value in player.scoring_pad.values():
        if value:
            total += value

    # Storing player name and total score
    results[player.name + ' ' + str(total)] = total


sorted_result = list(
    dict(sorted(results.items(), key=operator.itemgetter(1), reverse=True)))  # Sorting player by score
[print(_) for _ in sorted_result]
