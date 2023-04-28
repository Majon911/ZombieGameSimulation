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
        self.city.healthy_queue.append(self)

    def zombify(self):
        if not self.infected:
            print("Citizen", self.id, "has been infected! ")
            self.infected = True
            self.city.zombie_queue.append(self)
            self.city.healthy_queue.remove(self)

    def death(self):
        if self.alive:
            self.city.healthy_queue.remove(self)
            self.city.dead_queue.append(self)
            self.alive = False


# Creating the map / cities
MackersCity = city("Mackers City", random.randrange(500, 1001))
GulansTown = city("Gulans Town", random.randrange(20, 201))
NogalesVillage = city("Nogales Village", random.randrange(50, 451))
AlbonoHills = city("Albono Hills", random.randrange(250, 701))
ZeidelBorough = city("Zeidel Borough", random.randrange(400, 951))
map = [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]



