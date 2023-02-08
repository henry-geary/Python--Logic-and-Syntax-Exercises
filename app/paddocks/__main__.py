from .paddock_exercises.exercise_2 import two
from .paddock_exercises.exercise_3 import three
from .paddock_exercises.exercise_4 import four
from .paddock_exercises.exercise_5 import five
from .paddock_exercises.exercise_6 import six
from .paddock_exercises.exercise_7 import seven
from .paddock_exercises.exercise_8 import eight
from .paddock_exercises.exercise_9 import nine


class Exercise_case:
    def select(self, exercise):
        return getattr(self, "exercise_" + str(exercise))()

    @staticmethod
    def exercise_2():
        return two()

    @staticmethod
    def exercise_3():
        return three()

    @staticmethod
    def exercise_4():
        return four()

    @staticmethod
    def exercise_5():
        return five()

    @staticmethod
    def exercise_6():
        return six()

    @staticmethod
    def exercise_7():
        return seven()

    @staticmethod
    def exercise_8():
        return eight()

    @staticmethod
    def exercise_9():
        return nine()


def menu():
    print("Exercise 2")
    print("Exercise 3")
    print("Exercise 4")
    print("Exercise 5")
    print("Exercise 6")
    print("Exercise 7")
    print("Exercise 8")
    print("Exercise 9")


def main():
    while True:
        while True:
            menu()
            try:
                selected = int(input("Write exercise number: "))
            except TypeError:
                raise TypeError('Error: invalid input, must be a Exercise number')

            if 2 > selected or selected > 9:
                raise Exception("The number must be between 2 and 9")

            my_case = Exercise_case()

            print(f"|------| Exercise {selected} start |------|")

            print(my_case.select(selected))

            print(f"|------| Exercise {selected} end |------|")


if __name__ == '__main__':
    main()
