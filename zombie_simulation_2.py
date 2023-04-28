# zombie_simulation.py
import threading
import time
import webbrowser
import random

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

    def zombie_destruction(self):
        if self.type == "Soldier":
            if self.rank == 1:
                num_zombies = random.randrange(1, 5)
                queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                for i in range(num_zombies):
                    moving = self.city_name.zombie_queue.pop(queue_positions)
                    self.city_name.dead_queue.append(moving)
            elif self.rank == 2:
                num_zombies = random.randrange(1, 10)
                queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                for i in range(num_zombies):
                    moving = self.city_name.zombie_queue.pop(queue_positions)
                    self.city_name.dead_queue.append(moving)
            elif self.rank == 3:
                num_zombies = random.randrange(1, 15)
                queue_positions = random.randrange(1, len(self.city_name.zombie_queue))
                for i in range(num_zombies):
                    moving = self.city_name.zombie_queue.pop(queue_positions)
                    self.city_name.dead_queue.append(moving)
        elif self.type == "Soldier Armoured":
            if self.rank == 1:
                pass
            elif self.rank == 2:
                pass
            elif self.rank == 3:
                pass
        elif self.type == "Tank":
            if self.rank == 1:
                pass
            elif self.rank == 2:
                pass
            elif self.rank == 3:
                pass
        elif self.type == "Plane":
            if self.rank == 1:
                pass
            elif self.rank == 2:
                pass
            elif self.rank == 3:
                pass

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
            print(self.city.name, "is in danger." )
            self.infected = True
            self.city.zombie_queue.append(self)
            self.city.healthy_queue.remove(self)

    def death(self):
        if self.alive:
            self.city.dead_queue.append(self)
            self.alive = False
class plague_inc:
    def __init__(self, city_instance):
        self.name = city_instance.name
        self.zombie_queue = city_instance.zombie_queue
        self.prompts_healthy = [f"Business as Usual in {self.name}", "Scientists discover a bacteria that eats plastic", f"Juice WRLD hologram performs at sold-out concert in {self.name}", "AI development accelerating at an alarming rate", "Summer 2023 hottest on record"]
        self.prompts_low_concern = ["Odd disease spotted", "Epidemiologists concerned", "FOX news claims hoax, blames progressives", "Local governments consider lockdown", "Parents pull children out of schools"]
        self.prompts_high_concern = ["Schools close down", "Widespread chaos", "Shops looted", "Widespread power outages", "FOX news advocates for reopening of schools"]
        self.prompts_defeat = ["Few humans remain", "Government has ceased to function", "Zombies begin to starve", "FOX news blames Obama", f"Nuclear Reactor in {self.name} breaks down"]

    def prompts(self):
        if len(self.zombie_queue) < 5:
            print(random.choice(self.prompts_healthy))
        elif len(self.zombie_queue) < 50:
            print(random.choice(self.prompts_low_concern))
        elif len(self.zombie_queue) < 100:
            print(random.choice(self.prompts_high_concern))
        else:
            print(random.choice(self.prompts_defeat))


# class zombie_swarm:
#     def __init__(self, city_instance):
#         #ned to incorporate self.id somehow and instead of removing the id, remove the number of zombies in zombie_deaths
#         self.name = city_instance.name
#         self.zombie_queue = city_instance.zombie_queue
#
#     def swarm(self):
#         i = [1, 5, 75, 100, 175, 250, 325, 400, 475, 600, 1000]
#         #reasons_of_death = ["starvation", "by crowd crush", "by machine gun"]
#         zombie_deaths = random.randrange(10, 400)
#         #reasons_chance = random.randrange(0, len(reasons_of_death) + 1)
#         if len(self.zombie_queue) == i:
#             print(f"A zombie swarm is attacking {self.name}!")
#             self.zombie_queue.remove(zombie_deaths)
#             for i in range(zombie_deaths):
#                 moving = map[self.name].zombie_queue.pop(i)
#                 map[self.name].dead_queue.append(moving)
#             #for reasons_chance in reasons_of_death:
#             print(f"{zombie_deaths} zombies have died")

class natural_disaster:
    def __init__(self, city_instance):
        self.name = city_instance.name
        self.zombie_queue = city_instance.zombie_queue
        self.healthy_queue = city_instance.healthy_queue
        self.dead_queue = city_instance.dead_queue
        self.disaster = ['fire', 'flood', 'tornado', 'earthquake']
        self.casualties = 0


    def disaster_function(self):
        choice_of_disaster = random.choice(self.disaster)
        print("A", choice_of_disaster,  f"has occured in {self.name}!")
        if len(self.healthy_queue) > 5:
            for x in range(0,len(self.healthy_queue) - 1):
                i = self.healthy_queue.pop(0)
                self.dead_queue.append(i)
                self.casualties = x
        if len(self.zombie_queue) > 5:
            for x in range(0,len(self.healthy_queue) - 1):
                i = self.zombie_queue.pop(0)
                self.dead_queue.append(i)
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
    city_instance = map[z]# or any other city instance you want to use
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

