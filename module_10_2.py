from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        number_of_wars = 100
        count_day = 0
        print(f"{self.name} на нас напали!")
        while number_of_wars > 0:
            sleep(1)
            number_of_wars -= self.power
            count_day += 1
            if number_of_wars < 0:
                number_of_wars = 0
            print(f"{self.name} сражается {count_day} день (дня), осталось {number_of_wars} войнов.")

        print(f"{self.name} одержал победу спустя {count_day} дней (дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
