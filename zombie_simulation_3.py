import threading
import time
# import webbrowser
import random
# import math
import concurrent.futures


class Military:
    def __init__(self, id, type, rank, city_name):
        self.id = id
        self.type = type
        self.rank = rank
        self.city_name = city_name
        self.infected = False
        self.alive = True
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()

    def zombie_destruction(self):
        try:
            while True:
                if self.alive == False:
                    print(f"Thread Soldier {self.id}, is dead, thread stopping.")
                    break
                if self.type == "Soldier":
                    if self.rank == 1:
                        num_zombies = random.randrange(1, 5)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 2:
                        num_zombies = random.randrange(1, 10)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 3:
                        num_zombies = random.randrange(1, 15)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                elif self.type == "Soldier Armoured":
                    if self.rank == 1:
                        num_zombies = random.randrange(1, 10)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 2:
                        num_zombies = random.randrange(1, 15)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 3:
                        num_zombies = random.randrange(1, 20)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                elif self.type == "Tank":
                    if self.rank == 1:
                        num_zombies = random.randrange(1, 15)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 2:
                        num_zombies = random.randrange(1, 25)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 3:
                        num_zombies = random.randrange(1, 35)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                elif self.type == "Plane":
                    if self.rank == 1:
                        num_zombies = random.randrange(1, 20)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 2:
                        num_zombies = random.randrange(1, 30)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                    elif self.rank == 3:
                        num_zombies = random.randrange(1, 40)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_zombies):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = False
                            self.city_name.dead_queue_lock.acquire()
                            self.city_name.dead_queue.append(moving)
                            self.city_name.dead_queue_lock.release()
                            time.sleep(2)
                if self.infected:
                    print("Military personnel", self.id, "has been infected! ")
                    # print(self.city_name.name, "is in danger.")
                    self.city_name.healthy_queue.acquire()
                    citizen = self.city_name.healthy_queue.pop(random.randrange(len(self.city_name.healthy_queue)))
                    self.city_name.healthy_queue.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(2)

        except Exception as e:
            print("There was an error")
            logging.error(traceback.format_exc())

# Medics class
class Medic:
    def __init__(self, id, type, city_name):
        self.id = id
        self.type = type
        self.city_name = city_name
        self.infected = False
        self.alive = True
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()

    def zombie_cure(self):
        try:
            while True:
                if self.alive == False:
                    print(f"Thread Medic {self.id}, is dead, thread stopping.")
                    break
                if self.type == "Medic":
                    self.city_name.zombie_queue_lock.acquire()
                    if self.city_name.zombie_queue / (self.city_name.zombie_queue + self.city_name.healthy_queue) >= 0.75:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(7, 25)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = True
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    elif 0.75 > self.city_name.zombie_queue / (self.city_name.zombie_queue + self.city_name.healthy_queue) >= 0.5:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(5, 20)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = True
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    elif 0.5 > self.city_name.zombie_queue / (self.city_name.zombie_queue + self.city_name.healthy_queue) >= 0.25:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(3, 15)
                        self.city_name.zombie_queue_lock.acquire()
                        queue_positions = random.randrange(len(self.city_name.zombie_queue))
                        self.city_name.zombie_queue_lock.release()
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = self.city_name.zombie_queue.pop(queue_positions)
                            self.city_name.zombie_queue_lock.release()
                            moving.alive = True
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                if self.infected:
                    print("Medic", self.id, "has been infected! ")
                    # print(self.city_name.name, "is in danger.")
                    self.city_name.healthy_queue.acquire()
                    citizen = self.city_name.healthy_queue.pop(random.randrange(len(self.city_name.healthy_queue)))
                    self.city_name.healthy_queue.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(2)

        except Exception as e:
            print("There was an error")
            logging.error(traceback.format_exc())


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.healthy_queue = []
        self.zombie_queue = []
        self.dead_queue = []
        self.healthy_queue_lock = threading.Lock()
        self.zombie_queue_lock = threading.Lock()
        self.dead_queue_lock = threading.Lock()


class Citizen:
    def __init__(self, id, city_name):
        self.id = id
        self.alive = True
        self.infected = False
        self.city_name = city_name
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()

    def zombify(self):
        try:
            choice1 = random.choices(["healthy", "infected"], [18, 2])[0]
            if choice1 == "healthy":
                self.city_name.healthy_queue_lock.acquire()
                self.city_name.healthy_queue.append(self)
                self.city_name.healthy_queue_lock.release()
            else:
                self.city_name.zombie_queue_lock.acquire()
                self.city_name.zombie_queue.append(self)
                self.city_name.zombie_queue_lock.release()
            while True:
                if self.alive == False:
                    break
                if self.infected:
                    print("Citizen", self.id, "has been infected! ")
                    # print(self.city_name.name, "is in danger.")
                    self.city_name.healthy_queue.acquire()
                    citizen = self.city_name.healthy_queue.pop(random.randrange(len(self.city_name.healthy_queue)))
                    self.city_name.healthy_queue.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(2)

        except Exception as e:
            print("There was an error")
            logging.error(traceback.format_exc())


# Creating the map / cities
MackersCity = City("Mackers City", random.randrange(500, 1001))
GulansTown = City("Gulans Town", random.randrange(20, 201))
NogalesVillage = City("Nogales Village", random.randrange(50, 451))
AlbonoHills = City("Albono Hills", random.randrange(250, 701))
ZeidelBorough = City("Zeidel Borough", random.randrange(400, 951))


#######################################################################
## MECHANICS ##

citizen_queue_init = []
citizen_id = 0
for i in range(1000):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])[0]
    citizen_queue_init.append(Citizen(citizen_id, city_prob))
    citizen_id = citizen_id + 1

military_queue_init = []
military_id = 0
for i in range(100):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])[0]
    mtype = random.choices(["Soldier", "Soldier Armoured", "Tank", "Plane"], [5, 4, 2, 1])[0]
    mrank = random.choices([1, 2, 3], [6, 3, 1])[0]
    military_queue_init.append(Military(military_id, mtype, mrank, city_prob))
    military_id = military_id + 1

medic_queue_init = []
medic_id = 0
for i in range(50):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])[0]
    medic_queue_init.append(Medic(medic_id, "Medic", city_prob))
    medic_id = medic_id + 1

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    for citizen in citizen_queue_init:
        executor.submit(citizen.zombify)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for personnel in military_queue_init:
        executor.submit(personnel.zombie_destruction)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for medic in medic_queue_init:
        executor.submit(medic.zombie_cure)
