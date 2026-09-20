import random
from calendar import day_abbr

brand_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 10},
    "Lada": {"fuel": 100, "strength": 1, "consumption": 8},
    "volvo": {"fuel": 100, "strength": 3, "consumption": 4}
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "python developer": {"salary": 50, "gladness_less": 10},
    "c++ developer": {"salary": 50, "gladness_less": 10},
    "rust developer": {"salary": 50, "gladness_less": 10}
}
class Friend:
    def __init__(self, name="alex"):
        self.name = name
        self.gladness = 50

    def chat(self):
        self.gladness += 10

class Pet:
    def __init__(self, name="kotosty"):
        self.name = name
        self.gladness = 50
        self.satiety = 50

    def play(self):
        self.gladness += 15
        self.satiety -= 5

class Human:
    def __init__(self, name="human", job=None, home=None, car=None, pet=None, friend=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet
        self.friend = friend

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_pet(self):
        self.pet = Pet("Barsik")

    def get_friend(self):
        self.friend = Friend("Alex")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicacies")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def play_with_pet(self):
        self.gladness += 12
        self.pet.play()
        print(f"I played with my pet {self.pet.name}! So cute.")

    def invite_friend(self):
        self.gladness += 15
        self.friend.chat()
        self.home.mess += 8
        print(f"I invited my friend {self.friend.name} over. We had a great chat!")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day_number):
        day_str = f"Today is the {day_number} day of {self.name}'s life"
        print(f"{day_str:^40}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")
        if self.pet:
            print(f"Pet ({self.pet.name}) Gladness - {self.pet.gladness}")
        if self.friend:
            print(f"Friend ({self.friend.name}) Gladness - {self.friend.gladness}")
        print("-" * 40)

    def is_alive(self):
        if self.gladness < 0:
            print("Depression... Game over.")
            return False
        if self.satiety < 0:
            print("Dead from hunger... Game over.")
            return False
        if self.money < -500:
            print("Bankrupt... Game over.")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I got a job as {self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print(f"I adopted a pet named {self.pet.name}")
        if self.friend is None:
            self.get_friend()
            print(f"I made a friend named {self.friend.name}")

        self.days_indexes(day)

        dice = random.randint(1, 6)  # Додано ще один варіант для друга
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            print("Let's chill!")
            self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Chill!")
            self.chill()
        elif dice == 2:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 3:
            print("Start working!")
            self.work()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Playing with pet!")
            self.play_with_pet()
        elif dice == 6:
            print("Hanging out with friend!")
            self.invite_friend()

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list.keys()))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list.keys()))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


persona = Human(name="Nick")

for day in range(1, 7):
    if persona.live(day) is False:
        break