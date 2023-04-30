import logging
import threading
import time
# import webbrowser
import random
# import math
import concurrent.futures
import traceback


class Military:
    def __init__(self, id, type, rank, city_name):
        self.id = id
        self.type = type
        self.rank = rank
        self.city_name = city_name
        self.infected = False
        self.alive = True
        self.job = "Military"
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()
        print("Military", id, "was created in", city_name.name)

    def zombie_destruction(self):
        try:
            while True:
                if self.alive == False:
                    print(f"Thread Soldier {self.id}, is dead, thread stopping.")
                    break
                self.city_name.zombie_queue_lock.acquire()
                if len(self.city_name.zombie_queue) <= 45:
                    self.city_name.zombie_queue_lock.release()
                    print("Military disactivated!")
                    time.sleep(5)
                elif len(self.city_name.zombie_queue) > 45:
                    self.city_name.zombie_queue_lock.release()
                    if self.type == "Soldier":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 5)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 10)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 15)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                    elif self.type == "Soldier Armoured":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 10)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 15)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 20)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                    elif self.type == "Tank":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 15)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 25)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 35)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                    elif self.type == "Plane":
                        if self.rank == 1:
                            num_zombies = random.randrange(1, 20)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 2:
                            num_zombies = random.randrange(1, 30)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                        elif self.rank == 3:
                            num_zombies = random.randrange(1, 40)
                            for i in range(num_zombies):
                                self.city_name.zombie_queue_lock.acquire()
                                moving = random.choice(self.city_name.zombie_queue)
                                self.city_name.zombie_queue_lock.release()
                                print("Military", self.id, self.type, "killed", moving.job, moving.id)
                                moving.alive = False
                                self.city_name.dead_queue_lock.acquire()
                                self.city_name.dead_queue.append(moving)
                                self.city_name.dead_queue_lock.release()
                                time.sleep(2)
                if self.infected:
                    print("Military personnel", self.id, "has been infected! ")
                    self.city_name.healthy_queue_lock.acquire()
                    citizen = random.choice(self.city_name.healthy_queue)
                    self.city_name.healthy_queue_lock.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(2)

        except Exception as e:
            print("There was an error: MILITARY")
            logging.error(traceback.format_exc())
            print(e)

# Medics class
class Medic:
    def __init__(self, id, type, city_name):
        self.id = id
        self.type = type
        self.city_name = city_name
        self.infected = False
        self.alive = True
        self.job = "Medic"
        self.city_name.healthy_queue_lock.acquire()
        self.city_name.healthy_queue.append(self)
        self.city_name.healthy_queue_lock.release()
        print("Medic", id, "was created in", city_name.name)

    def zombie_cure(self):
        try:
            while True:
                if self.alive == False:
                    print(f"Thread Medic {self.id}, is dead, thread stopping.")
                    break
                if self.type == "Medic":
                    self.city_name.zombie_queue_lock.acquire()
                    if len(self.city_name.zombie_queue) / (len(self.city_name.zombie_queue) + len(self.city_name.healthy_queue)) >= 0.75:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(7, 25)
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = random.choice(self.city_name.zombie_queue)
                            self.city_name.zombie_queue_lock.release()
                            print(moving.job, moving.id, "has been cured! ")
                            moving.alive = True
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    elif 0.75 > len(self.city_name.zombie_queue) / (len(self.city_name.zombie_queue) + len(self.city_name.healthy_queue)) >= 0.5:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(5, 20)
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = random.choice(self.city_name.zombie_queue)
                            self.city_name.zombie_queue_lock.release()
                            print(moving.job, moving.id, "has been cured! ")
                            moving.alive = True
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    elif 0.5 > len(self.city_name.zombie_queue) / (len(self.city_name.zombie_queue) + len(self.city_name.healthy_queue)) >= 0.25:
                        self.city_name.zombie_queue_lock.release()
                        num_infected = random.randrange(3, 15)
                        for i in range(num_infected):
                            self.city_name.zombie_queue_lock.acquire()
                            moving = random.choice(self.city_name.zombie_queue)
                            self.city_name.zombie_queue_lock.release()
                            print(moving.job, moving.id, "has been cured! ")
                            moving.alive = True
                            self.city_name.healthy_queue_lock.acquire()
                            self.city_name.healthy_queue.append(moving)
                            self.city_name.healthy_queue_lock.release()
                            time.sleep(2)
                    else:
                        self.city_name.zombie_queue_lock.release()
                        print("No need for medics yet!")
                        time.sleep(5)
                if self.infected:
                    print("Medic", self.id, "has been infected! ")
                    self.city_name.healthy_queue_lock.acquire()
                    citizen = random.choice(self.city_name.healthy_queue)
                    self.city_name.healthy_queue_lock.release()
                    citizen.infected = True
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(2)

        except Exception as e:
            print("There was an error: MEDIC")
            logging.error(traceback.format_exc())
            print(e)


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
        self.job = "Civil"

    def zombify(self):
        try:
            while True:
                choice1 = random.choices(["healthy", "infected"], [18, 2])[0]
                if choice1 == "healthy":
                    self.city_name.healthy_queue_lock.acquire()
                    self.city_name.healthy_queue.append(self)
                    self.city_name.healthy_queue_lock.release()
                elif choice1 == "infected":
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(self)
                    self.city_name.zombie_queue_lock.release()
                    self.infected = True
                print("Citizen", self.id, "was created in", self.city_name.name)
                if self.alive == False:
                    break
                if self.infected:
                    print("Citizen", self.id, "has been infected in", self.city_name.name)
                    # print(self.city_name.name, "is in danger.")
                    self.city_name.healthy_queue_lock.acquire()
                    citizen = random.choice(self.city_name.healthy_queue)
                    self.city_name.healthy_queue_lock.release()
                    citizen.infected = True
                    print("Citizen", self.id, "INFECTED", citizen.job, citizen.id)
                    self.city_name.zombie_queue_lock.acquire()
                    self.city_name.zombie_queue.append(citizen)
                    self.city_name.zombie_queue_lock.release()
                    time.sleep(2)

        except Exception as e:
            print("There was an error: CITIZEN")
            print(e)
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



with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for medic in medic_queue_init:
        executor.submit(medic.zombie_cure)
        print(f"{medic.job, medic.id}, is now WORKING!")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for personnel in military_queue_init:
            executor.submit(personnel.zombie_destruction)
            print(f"{personnel.job, personnel.id}, is now WORKING!")

        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
            for citizen in citizen_queue_init:
                executor.submit(citizen.zombify)
                print(f"{citizen.job, citizen.id}, is now WORKING!")

# with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
#     for citizen in citizen_queue_init:
#         executor.submit(citizen.zombify)
#         print(f"{citizen.job, citizen.id}, is now WORKING!")
#     with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
#         for personnel in military_queue_init:
#             executor.submit(personnel.zombie_destruction)
#             print(f"{personnel.job, personnel.id}, is now WORKING!")
#         with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#             for medic in medic_queue_init:
#                 executor.submit(medic.zombie_cure)
#                 print(f"{medic.job, medic.id}, is now WORKING!")
