import random


class Pet:
    def __init__(self, name="Barsik"):
        self.name = name
        self.gladness_boost = 8
        self.money_cost = 5


class Friend:
    def __init__(self, name="Max"):
        self.name = name
        self.gladness_boost = 12
        self.money_cost = 12


class StudentSimulator:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
        self.alive = True

        # Студент володіє твариною та має друга
        self.pet = Pet(name="Barsik")
        self.friend = Friend(name="Max")

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.money -= 2

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time alone")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 4
        self.progress -= 0.02

    def to_play_with_pet(self):
        print(f"Playing with pet {self.pet.name}")
        self.gladness += self.pet.gladness_boost
        self.money -= self.pet.money_cost
        self.progress -= 0.01

    def to_meet_friend(self):
        print(f"Chilling with friend {self.friend.name}")
        self.gladness += self.friend.gladness_boost
        self.money -= self.friend.money_cost
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.money < 0:
            print("Bankrupt…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money    = {self.money}")

    def live(self, day):
        day_str = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day_str:=^50}")

        # Логіка вибору дій залежно від стану
        if self.money < 15:
            self.to_work()
        elif self.progress < 0.2:
            self.to_study()
        elif self.gladness < 30:
            # Якщо стане дуже сумно, студент грається з домашнім улюбленцем
            self.to_play_with_pet()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.to_meet_friend()

        self.end_of_day()
        self.is_alive()


nick = StudentSimulator(name="Nick")
for day in range(1, 366):
    if not nick.alive:
        break
    nick.live(day)