# zombie_simulation.py
import threading
import time
import webbrowser
import random

total_population = 0
total_infected = 0
days = 0
deaths = 0


# city class
class city:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.healthy_queue = []
        self.zombie_queue = []
        self.dead_queue = []
        self.healthy_queue_lock = threading.Lock()
        self.zombie_queue_lock = threading.Lock()
        self.dead_queue_lock = threading.Lock()


# citizen class
class citizen:
    def __init__(self, id, city):
        self.id = id
        self.alive = True
        self.infected = False
        self.city = city
        self.city.healthy_queue_lock.acquire()
        self.city.healthy_queue.append(self)
        self.city.healthy_queue_lock.release()

    def zombify(self):
        if self.infected:
            self.city.healthy_queue_lock.acquire()
            victim = random.choice(self.city.healthy_qeue)
            self.city.healthy_queue_lock.release()
            print("Citizen", victim.id, "has been infected! ")
            victim.infected = True
            victim.city.healthy_queue_lock.acquire()
            victim.city.healthy_queue.remove(victim)
            victim.city.healthy_queue_lock.release()
            victim.city.zombie_queue_lock.acquire()
            victim.city.zombie_queue.append(victim)
            victim.city.zombie_queue_lock.release()


    def death(self):
        if self.alive:
            self.city.healthy_queue_lock.acquire()
            self.city.healthy_queue.remove(self)
            self.city.healthy_queue_lock.release()
            self.city.dead_queue_lock.acquire()
            self.city.dead_queue.append(self)
            self.city.dead_queue_lock.release()
            self.alive = False


# Military class
class Military:
    def __init__(self, id, type, rank, city_name):
        self.id = id
        self.type = type
        self.rank = rank
        self.city_name = city_name
        self.infected = False
        self.alive = True

    def zombie_destruction(self):
        while True:
            if self.alive == False:
                print(f"Thread Soldier {self.id}, is dead, thread stopping.")
                break
            if self.type == "Soldier":
                if self.rank == 1:
                    num_zombies = random.randrange(1, 5)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 2:
                    num_zombies = random.randrange(1, 10)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 3:
                    num_zombies = random.randrange(1, 15)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
            elif self.type == "Soldier Armoured":
                if self.rank == 1:
                    num_zombies = random.randrange(1, 10)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 2:
                    num_zombies = random.randrange(1, 15)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 3:
                    num_zombies = random.randrange(1, 20)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
            elif self.type == "Tank":
                if self.rank == 1:
                    num_zombies = random.randrange(1, 15)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 2:
                    num_zombies = random.randrange(1, 25)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 3:
                    num_zombies = random.randrange(1, 35)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
            elif self.type == "Plane":
                if self.rank == 1:
                    num_zombies = random.randrange(1, 20)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 2:
                    num_zombies = random.randrange(1, 30)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()
                elif self.rank == 3:
                    num_zombies = random.randrange(1, 40)
                    queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                    for i in range(num_zombies):
                        self.city_name.zombie_queue_lock.acquire()
                        moving = self.city_name.zombie_queue.pop(queue_positions)
                        self.city_name.zombie_queue_lock.release()
                        moving.alive = False
                        self.city_name.dead_queue_lock.acquire()
                        self.city_name.dead_queue.append(moving)
                        self.city_name.dead_queue_lock.release()



# Creating the map / cities
MackersCity = city("Mackers City", random.randrange(500, 1001))
GulansTown = city("Gulans Town", random.randrange(20, 201))
NogalesVillage = city("Nogales Village", random.randrange(50, 451))
AlbonoHills = city("Albono Hills", random.randrange(250, 701))
ZeidelBorough = city("Zeidel Borough", random.randrange(400, 951))
map = [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]



Sergio = citizen()