# zombie_simulation.py
import threading
import time
import webbrowser
import random
import math
import concurrent.futures

total_population = 0
total_zombies = 0
days = 0
deaths = 0


class Nuke:
    def __init__(self):
        self.deployed = False

    def check_pop(self):
        while not self.deployed:
            for cities in map:
                if (len(cities.zombie_queue)/(len(cities.zombie_queue)+len(cities.healthy_queue))) > 0.95:
                    print(f"City: {cities.name} is in a horrible situation, zombies make up more then 95% of the population.")
                    print("Military proposes operation Oppenheimer! One time choice!")
                    nuke_q = str(input("Do you want to use a tactical nuke? Y/N"))
                    if nuke_q == "Y":
                        webbrowser.open('https://www.youtube.com/watch?v=bryWiNw9Rzg')
                        print(f"NUCLEAR BOMB DEPLOYED IN {cities.name}")
                        self.deployed = True
                        # To be worked on nuke wipe out thread STOP
                        map.remove(cities)
                    elif nuke_q == "N":
                        time.sleep(15)
                    else:
                        print("Wrong input, try again!")


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

    def military_zombify(self):
        while True:
            if self.alive == False:
                break
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


# Medics class
class Medic:
    def __init__(self, id, type, city_name):
        self.id = id
        self.type = type
        self.city_name = city_name
        self.infected = False
        self.alive = True

    def zombie_cure(self):
        while True:
            if self.alive == False:
                print(f"Thread Medic {self.id}, is dead, thread stopping.")
                break
            if self.type == "Medic":
                if self.city_name.zombie_queue / (self.city_name.zombie_queue + self.city_name.healthy_queue) >= 0.75:
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
                elif 0.75 > self.city_name.zombie_queue / (self.city_name.zombie_queue + self.city_name.healthy_queue) >= 0.5:
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
                elif 0.5 > self.city_name.zombie_queue / (self.city_name.zombie_queue + self.city_name.healthy_queue) >= 0.25:
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
    def medic_zombify(self):
        while True:
            if self.alive == False:
                break
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

class statistics:
    def __init__(self, total_infected, time_elapsed, total_deaths):
        self.total_infected = total_infected
        self.time_elapsed = time_elapsed
        self.total_deaths = total_deaths

    def report(self):
        print()
        print("\nSCOREBOARD: ")
        print("\tTime Elapsed: ", self.time_elapsed)
        print("\tTotal Infected: ", self.total_infected)
        print("\tTotal Deaths: ", self.total_deaths)


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

    def fallen(self):
        if len(self.healthy_queue) == 0:
            print(f"{self.name} has fallen")


class Citizen:

    def __init__(self, id, city_name):
        self.id = id
        self.alive = True
        self.infected = False
        self.city_name = city_name
        # self.city.healthy_queue.append(self)

    def zombify(self):
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


class plague_inc:
    def __init__(self, city_instance):
        self.name = city_instance.name
        self.zombie_queue = city_instance.zombie_queue
        self.prompts_healthy = [f"Business as Usual in {self.name}", "New study shows that people who eat pizza every day are more immune to viruses", "Scientists discover a bacteria that eats plastic", f"Juice WRLD hologram performs at sold-out concert in {self.name}", "AI development accelerating at an alarming rate", "Summer 2023 hottest on record", "Giant mutant chickens wreak havoc on cities worldwide", f"World's largest banana cultivated in {self.name}", f"{self.name} vows to be car free by 2033", "Government issues warning after mysterious epidemic causes people to speak in pirate language", "Government advises citizens to stop licking doorknobs to prevent spread of virus", f"Cultural tensions on the rise in {self.name} "]
        self.prompts_low_concern = ["World's largest pillow fight cancelled","Odd disease spotted", "Epidemiologists concerned", "FOX news claims hoax, blames progressives", "Local governments consider lockdown", "Parents pull children out of schools", "New study shows that infection rates are highest among people who use Comic Sans", "Global toilet paper shortage as people panic-buy in response to new virus"]
        self.prompts_high_concern = ["Desperate civials eat pizza in hopes to boost immunity","Experts warn of impending doom as cute and cuddly zombies begin attacking humans", f"Schools in {self.name} close down", "Widespread chaos", "Shops looted", "Widespread power outages", "FOX news advocates for reopening of schools"]
        self.prompts_defeat = ["Few humans remain", f"Woman tries to marry zombie in {self.name}, becomes infected ", "Government has ceased to function", "Zombies begin to starve", "FOX news blames Obama", f"Nuclear Reactor in {self.name} breaks down"]

    def prompts(self):
        if len(self.zombie_queue) < 5:
            print(random.choice(self.prompts_healthy))
        elif len(self.zombie_queue) < 50:
            print(random.choice(self.prompts_low_concern))
        elif len(self.zombie_queue) < 100:
            print(random.choice(self.prompts_high_concern))
        else:
            print(random.choice(self.prompts_defeat))


class zombie_swarm:
    def __init__(self, city_instance):
        self.name = city_instance.name
        self.zombie_queue = city_instance.zombie_queue
        self.healthy_queue = city_instance.healthy_queue
        self.dead_queue = city_instance.dead_queue
        self.chances = random.randint(0, 10)
        self.people_dead = random.randint(1, 30)
    def swarm(self):
        if len(self.zombie_queue) > 50:
            if self.chances == 0:
                print("There is a zombie swarm in ", {self.name}, "!")
                for x in range(0, self.people_dead):
                    i = self.healthy_queue.pop(0)
                    self.zombie_queue.lock_aquire()
                    self.zombie_queue.append(i)
                    self.zomie_queue.lock_release()
                print(self.people_dead, "people have become zombies!")


class natural_disaster:
    def __init__(self, city_instance):
        self.name = city_instance.name
        self.zombie_queue = city_instance.zombie_queue
        self.healthy_queue = city_instance.healthy_queue
        self.dead_queue = city_instance.dead_queue
        self.disaster = ['fire', 'flood', 'tornado', 'earthquake', 'epidemic']
        self.casualties = 0


    def disaster_function(self):
        choice_of_disaster = random.choice(self.disaster)
        print("A", choice_of_disaster,  f"has occured in {self.name}!")
        if len(self.healthy_queue) > 5:
            for x in range(0,math.floor(len(self.healthy_queue) / 2)):
                i = self.healthy_queue.pop(0)
                self.dead_queue.lock_append()
                self.dead_queue.append(i)
                self.dead_queue.lock_release()
                self.casualties = x
        if len(self.zombie_queue) > 5:
            for x in range(0,math.floor(len(self.zombie_queue) / 2)):
                i = self.zombie_queue.pop(0)
                self.dead_queue.lock_append()
                self.dead_queue.append(i)
                self.dead_queue.lock_release()
                self.casualties = x
        print(self.casualties, "casualties", "in ", f"{self.name}")
        self.casualties = 0





# Creating the map / cities
MackersCity = city("Mackers City", random.randrange(500, 1001))
GulansTown = city("Gulans Town", random.randrange(20, 201))
NogalesVillage = city("Nogales Village", random.randrange(50, 451))
AlbonoHills = city("Albono Hills", random.randrange(250, 701))
ZeidelBorough = city("Zeidel Borough", random.randrange(400, 951))
map = [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]

# The simulation per day
def day_sim(day_number):
    print("\n--Today is day number", day_number, "--")
    global map
    z = random.randint(0, len(map) - 1)
    city_instance = map[z]
    plague_instance = plague_inc(city_instance)
    plague_instance.prompts()
    disaster_instance = natural_disaster(city_instance)
    chances = random.randint(0,3)
    if chances == 2:
        disaster_instance.disaster_function()


#def non_zombie_fatalities

def non_zombie_fatalities():
    deaths = ["starvation"] * 1 + ["food poisoning"] * 2 + ["dehydration"] * 5 + ["suicide"] * 5 + ["unknown causes"] * 5
    return random.choice(deaths)

def death(city_population):
    death_citizens = 0

    while death_citizens < 1:

        probability = random.random()

        if probability < 0.01:
            death_citizens = 1
            death_type = "starvation"
        elif probability < 0.02:
            death_citizens = 1
            death_type = "food poisoning"
        elif probability < 0.05:
            death_citizens = 1
            death_type = "dehydration"
        elif probability < 0.03:
            death_citizens = 1
            death_type = "suicide"
        elif probability < 0.02:
            death_citizens = 1
            death_type = "unknown causes"

    for i in range(death_citizens):
        citizen = random.randint(1, city_population)
        print("Citizen {} in this city has died of {}.".format(citizen, death_type))
    
    
    
    
    # city_checker() "I modified it adding a new variable (death_count) however it has to be changed in the future because there will be 2 (1 for zombies and 1 for humans) and added the function (non_zombie_fatalities)" "Sergio" 13-4-23

def city_checker():
    y = input("\n'M' to check Mackers City \n'N' to check Nogales Village \n'G' to check Gulans Town \n<ENTER> to leave \n").upper()
    if y == 'M':
        print("\nMACKERS CITY: ")
        healthy_count = len(MackersCity.healthy_queue)
        zombie_count = len(MackersCity.zombie_queue)
        death_count = len(MackersCity.dead_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
        city_checker()
    elif y == 'N':
        print("\nNOGALES VILLAGE: ")
        healthy_count = len(NogalesVillage.healthy_queue)
        zombie_count = len(NogalesVillage.zombie_queue)
        death_count = len(NogalesVillage.dead_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
        city_checker()
    elif y == 'G':
        print("\nGULANS TOWN: ")
        healthy_count = len(GulansTown.healthy_queue)
        zombie_count = len(GulansTown.zombie_queue)
        death_count = len(GulansTown.dead_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
        city_checker()
    elif y == 'A':
        print("\nALBONO HILLS: ")
        healthy_count = len(AlbonoHills.healthy_queue)
        zombie_count = len(AlbonoHills.zombie_queue)
        death_count = len(AlbonoHills.dead_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
    elif y == 'Z':
        print("\nZEIDEL BOROUGH: ")
        healthy_count = len(ZeidelBorough.healthy_queue)
        zombie_count = len(ZeidelBorough.zombie_queue)
        death_count = len(ZeidelBorough.dead_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
    elif y == '':
        pass
    else:
        print("Invalid Input. ")
        city_checker()

#######################################################################
## MECHANICS ##

citizen_queue_init = []
citizen_id = 0
for i in range(1000):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])
    citizen_queue_init.append(Citizen(citizen_id, city_prob))
    citizen_id = citizen_id + 1

military_queue_init = []
military_id = 0
for i in range(100):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])
    mtype = random.choices(["Soldier", "Soldier Armoured", "Tank", "Plane"], [5, 4, 2, 1])
    mrank = random.choices([1, 2, 3], [6, 3, 1])
    military_queue_init.append(Military(military_id, mtype, mrank, city_prob))
    military_id = military_id + 1

medic_queue_init = []
medic_id = 0
for i in range(50):
    city_prob = random.choices([MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough],
                               [3, 2, 2, 1, 2])
    medic_queue_init.append(Medic(medic_id, "Medic", city_prob))
    medic_id = medic_id + 1

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
    for citizen in citizen_queue_init:
        executor.submit(citizen.zombify)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for personnel in military_queue_init:
        executor.submit(personnel.zombie_destruction)
        executor.submit(personnel.military_zombify)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for medic in medic_queue_init:
        executor.submit(medic.zombie_cure)
        executor.submit(medic.medic_zombify)


# def simulation():
#     try:
#         ### SETUP
#         global total_population
#         global total_zombies
#
#         # For each city, add their population to the total population
#         for city in map:
#             total_population += city.population
#
#         # Instantiating the citizens (TO BE THREADED)
#         for i in range(1, 1001):
#             c = citizen(i, MackersCity)
#
#         for i in range(1001, 1501):
#             c = citizen(i, GulansTown)
#
#         for i in range(1501, 2001):
#             c = citizen(i, NogalesVillage)
#
#         for i in range(2001, 2501):
#             c = citizen(i, AlbonoHills)
#
#         for i in range(2501, 3001):
#             c = citizen(i, ZeidelBorough)
#
#         # Instantiating the military (TO BE THREADED)
#         # for i in range(1, 51):
#         #     m = mc.Military(i, "Solider", random.randrange(1, 6))
#         #     city.active_military_personnel.append(m)
#         # for i in range(1, 11):
#         #     m = mc.Military(i, "Tank", random.randrange(1, 4))
#         #     city.active_military_personnel.append(m)
#         # for i in range(1, 6):
#         #     m = mc.Military(i, "Bomber", random.randrange(1, 3))
#         #     city.active_military_personnel.append(m)
#         # for i in range(1, 21):
#         #     m = mc.Military(i, "Solider Armoured", random.randrange(1, 6))
#         #     city.active_military_personnel.append(m)
#         # for i in range(1):
#         #     m = mc.Military(i, "Tactical Nuke", 1)
#         #     city.active_military_personnel.append(m)
#
#
#         ### STARTING SIMULATION
#         print("Welcome to our zombie simulation. ")
#         print("GUIDE: ")
#         print("\t1. Read the events of the zombie apocalypse. ")
#         print("\t2. Make choices to stop the spread of zombies. ")
#         print("\t3. Everyday you will be notified of the current situation. ")
#         print("\t   Enter any key to continue the simulation when prompted. ")
#         print("\t4. At any moment, press <ENTER> to leave simulation. ")
#
#         print("\nBACKGROUND: ")
#         print("\t* Your map is composed of 3 cities. ")
#         print("\t1.", MackersCity.name, "with population: ", MackersCity.population)
#         print("\t2.", NogalesVillage.name, "with population: ", NogalesVillage.population)
#         print("\t3.", GulansTown.name, "with population: ", GulansTown.population)
#         print("\t4.", AlbonoHills.name, "with population:", AlbonoHills.population)
#         print("\t5.", ZeidelBorough.name, "with population:", ZeidelBorough.population)
#         input("\nWhen you are ready to play, enter any key. ")
#
#
#         ### REPORT
#         for city in map:
#             total_zombies += len(city.zombie_queue)
#
#         scoreboard = statistics(total_zombies, days, deaths)
#         scoreboard.report()
#
#         city_checker()
#
#
#     except:
#         if KeyboardInterrupt:
#             raise
#         else:
#             print("\n\nThere was an error. ")


# simulation()

