# list every object oriented programming in Python
# python can create abstract class via abc module
from abc import abstractmethod, ABCMeta
from random import choice
import collections


# Python class
class Student:
    pass


# object
student = Student()


# Abstract class
class Pet(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_some_noise(self):
        print("pet pet wowo!")


# child class of Abstract class
class Dog(Pet):
    def make_some_noise(self):
        print("Dog Dog woof woof")


class Teacher:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print("Teacher's ID is :" + self.id + " and Name is " + self.name)


class WhoSay:
    def say(self, who):
        who.say()


# Single Inheritance
class MathTeacher(Teacher):
    def __init__(self, name, id, height):
        super().__init__(name, id)
        self.height = height

    def say(self):
        print("I teach math")


# Hierarchical Inheritance
class EnglishTeacher(Teacher):
    def say(self):
        print("I teach english")
    # child class code


# Multiple Inheritance
class SuperTeacher(EnglishTeacher, MathTeacher):
    pass
    # child class code


# Multi Level Inheritance
class MaleMathTeacher(MathTeacher):
    def __init__(self, name, id, height, phone):
        super().__init__(name, id, height)
        self.phone = phone


Card = collections.namedtuple('Card', ['rank', 'suit'])


# Interface
class Poker:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self, ):
        self.cards = [Card(rank=rank, suit=suit) for rank in self.ranks
                      for suit in self.suits]

    # Interface
    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


suit_value = dict(spades=3, hearts=2, diamonds=1,clubs=0)


def spades_high(card):
    rank_value = Poker.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]


def test_poker():
    deck = Poker()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(choice(deck))
    print(choice(deck))
    print(deck[:3])
    # for card in deck:
    #     print(card)
    for card in sorted(deck, key=spades_high):
        print(card)


def test_class():
    # Abstract class
    dog = Dog("roger")
    dog.make_some_noise()
    # Default Constructor
    student_b = Student()
    # Parameterized Constructor
    teacher = Teacher("Miss Wang", "1001")
    teacher.info()
    # Inheritance object
    math_teacher = MathTeacher("Mr Simon", "1002", "183cm")
    math_teacher.info()
    english_teacher = EnglishTeacher("Miss Wing", "1007")
    # Polymorphism
    a = WhoSay()
    a.say(english_teacher)
    a.say(math_teacher)
    # Multi Level Inheritance object
    male_math_teacher = MaleMathTeacher("Mr Lee", "1003", "161cm", "13333333")
    male_math_teacher.info()


if __name__ == '__main__':
    test_poker()
    # test_class()
