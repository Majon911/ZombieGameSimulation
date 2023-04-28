# zombie_simulation.py
import random
import time
import webbrowser

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

    def __init__(self, id, type, rank):
        self.id = id
        self.type = type
        self.rank = rank

    def zombie_destruction(self, city_name):
        if self.type == "Solider":
            if self.rank == 1:
                num_zombies = random.randrange(1, 5)
                queue_positions = random.randrange(1, len(map[city_name].zombie_queue))
                for i in range(num_zombies):
                    moving = map[city_name].zombie_queue.pop(queue_positions)
                    map[city_name].dead_queue.append(moving)
            elif self.rank == 2:
                num_zombies = random.randrange(1, 5)
                queue_positions = random.randrange(1, len(map[city_name].zombie_queue))
                for i in range(num_zombies):
                    moving = map[city_name].zombie_queue.pop(queue_positions)
                    map[city_name].dead_queue.append(moving)
            elif self.rank == 3:
                num_zombies = random.randrange(1, 5)
                queue_positions = random.randrange(1, len(map[city_name].zombie_queue))
                for i in range(num_zombies):
                    moving = map[city_name].zombie_queue.pop(queue_positions)
                    map[city_name].dead_queue.append(moving)
        elif self.type == "Solider Armoured":
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
    def __init__(self, total_infected, time_elapsed, total_deaths, total_military_alive):
        self.total_infected = total_infected
        self.time_elapsed = time_elapsed
        self.total_deaths = total_deaths
        self.total_military_alive = total_military_alive

    def report(self):
        print()
        print("\nSCOREBOARD: ")
        print("\tTime Elapsed: ", self.time_elapsed)
        print("\tTotal Infected: ", self.total_infected)
        print("\tTotal Deaths: ", self.total_deaths)
        print('\tTotal military alive: ', self.total_military_alive)


class city:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.healthy_queue = []
        self.zombie_queue = []
        self.dead_queue = []


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
            self.alive = False

import random
class plague_inc:
    def __init__(self, city_instance):
        self.name = city_instance.name
        self.zombie_queue = city_instance.zombie_queue
        self.prompts_healthy = [f"Business as Usual in {self.name}", "Scientists discover a bacteria that eats plastic", "Juice WRLD hologram performs at sold-out concert", "AI development accelerating at an alarming rate", "Summer 2023 hottest on record"]
        self.prompts_low_concern = ["Odd disease spotted", "Epidemiologists concerned", "FOX news claims hoax, blames progressives", "Local governments consider lockdown", "Parents pull children out of schools"]
        self.prompts_high_concern = ["Schools close down", "Widespread chaos", "Shops looted", "Widespread power outages", "FOX news advocates for reopening of schools"]
        self.prompts_defeat = ["Few humans remain", "Government has ceased to function", "Zombies begin to starve", "FOX news blames Obama", f"Nuclear Reactor in {self.name} breaks down"]

    def prompts(self):
        i = random.randrange(0,4)
        if len(self.zombie_queue) < 5:
            print(self.prompts_healthy[i])
        elif len(self.zombie_queue) < 50:
            print(self.prompts_low_concern[i])
        elif len(self.zombie_queue) < 100:
            print(self.prompts_high_concern[i])
        else:
            print(self.prompts_defeat[i])
import math
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
        print("A", choice_of_disaster,  f"has started in {self.name}!")
        if len(self.healthy_queue) > 5:
            for x in range(0,math.floor((len(self.healthy_queue) / 2))):
                i = self.healthy_queue.pop(0)
                self.dead_queue.append(i)
                self.casualties = x
        if len(self.zombie_queue) > 5:
            for x in range(0,math.floor(len(self.zombie_queue) / 2)):
                i = self.zombie_queue.pop(0)
                self.dead_queue.append(i)
                self.casualties = x
        print(self.casualties, "casualties", "in ", f"{self.name}")
        self.casualties = 0


# Creating the map / cities
MackersCity = city("Mackers City", 1000)
GulansTown = city("Gulans Town", 500)
NogalesVillage = city("Nogales Village", 500)
AlbonoHills = city("Albono Hills", 500)
ZeidelBorough = city("Zeidel Borough", 500)
map = [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]



# The simulation per day
def day_sim(day_number):
    print("\n--Today is day number", day_number, "--")
    city_list = [MackersCity, GulansTown, NogalesVillage, AlbonoHills, ZeidelBorough]
    z = random.randint(0, len(city_list) - 1)
    city_instance = city_list[z]# or any other city instance you want to use
    plague_instance = plague_inc(city_instance)
    plague_instance.prompts()
    disaster_instance = natural_disaster(city_instance)
    chances = random.randint(0,3)
    if chances == 2:
        disaster_instance.disaster_function()

    city = random.randint(0, 2)
    city = map[city]

    if city.name == 'Mackers City':
        lower = 0
        upper = 999
    else:
        lower = 0
        upper = 499


    infected = random.randint(lower, upper)
    c = city.healthy_queue[infected]
    c.zombify()



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
        death_count = len(MackersCity.death_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
        city_checker()
    elif y == 'N':
        print("\nNOGALES VILLAGE: ")
        healthy_count = len(NogalesVillage.healthy_queue)
        zombie_count = len(NogalesVillage.zombie_queue)
        death_count = len(NogalesVillage.death_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
        city_checker()
    elif y == 'G':
        print("\nGULANS TOWN: ")
        healthy_count = len(GulansTown.healthy_queue)
        zombie_count = len(GulansTown.zombie_queue)
        death_count = len(GulansTown.death_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
        city_checker()
    elif y == 'A':
        print("\nALBONO HILLS: ")
        healthy_count = len(AlbonoHills.healthy_queue)
        zombie_count = len(AlbonoHills.zombie_queue)
        death_count = len(AlbonoHills.death_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
    elif y == 'Z':
        print("\nZEIDEL BOROUGH: ")
        healthy_count = len(ZeidelBorough.healthy_queue)
        zombie_count = len(ZeidelBorough.zombie_queue)
        death_count = len(ZeidelBorough.death_queue)
        print("Uninfected Citizens:", healthy_count)
        print("Zombies:", zombie_count)
        print("Non-zombie Fatalities:", death_count)
    elif y == '':
        pass
    else:
        print("Invalid Input. ")
        city_checker()




def simulation():
    try:
        ### SETUP
        global total_population
        global total_zombies

        # For each city, add their population to the total population
        for city in map:
            total_population += city.population

        # Instantiating the citizens
        for i in range(1, 1001):
            c = citizen(i, MackersCity)

        for i in range(1001, 1501):
            c = citizen(i, GulansTown)

        for i in range(1501, 2001):
            c = citizen(i, NogalesVillage)

        for i in range(2001, 2501):
            c = citizen(i, AlbonoHills)

        for i in range(2501, 3001):
            c = citizen(i, ZeidelBorough)





        # Instantiating the military
        # for i in range(1, 51):
        #     m = mc.Military(i, "Solider", random.randrange(1, 6))
        #     city.active_military_personnel.append(m)
        # for i in range(1, 11):
        #     m = mc.Military(i, "Tank", random.randrange(1, 4))
        #     city.active_military_personnel.append(m)
        # for i in range(1, 6):
        #     m = mc.Military(i, "Bomber", random.randrange(1, 3))
        #     city.active_military_personnel.append(m)
        # for i in range(1, 21):
        #     m = mc.Military(i, "Solider Armoured", random.randrange(1, 6))
        #     city.active_military_personnel.append(m)
        # for i in range(1):
        #     m = mc.Military(i, "Tactical Nuke", 1)
        #     city.active_military_personnel.append(m)


        ### STARTING SIMULATION
        print("Welcome to our zombie simulation. ")
        print("GUIDE: ")
        print("\t1. Read the events of the zombie apocalypse. ")
        print("\t2. Make choices to stop the spread of zombies. ")
        print("\t3. Everyday you will be notified of the current situation. ")
        print("\t   Enter any key to continue the simulation when prompted. ")
        print("\t4. At any moment, press <ENTER> to leave simulation. ")

        print("\nBACKGROUND: ")
        print("\t* Your map is composed of 3 cities. ")
        print("\t1.", MackersCity.name, "with population: ", MackersCity.population)
        print("\t2.", NogalesVillage.name, "with population: ", NogalesVillage.population)
        print("\t3.", GulansTown.name, "with population: ", GulansTown.population)
        print("\t4.", AlbonoHills.name, "with population:", AlbonoHills.population)
        print("\t5.", ZeidelBorough.name, "with population:", ZeidelBorough.population)
        input("\nWhen you are ready to play, enter any key. ")



        ### WHILE PLAYING / SIMULATION BODY
        enter = 0
        global days

        while enter != '':
            days += 1
            day_sim(days)
            enter = input("<ENTER> to quit simulation. ")


        ### REPORT
        for city in map:
            total_zombies += len(city.zombie_queue)

        total_military = 0
        for city in map:
            total_military += len(city.active_military_personnel)

        scoreboard = statistics(total_zombies, days, deaths, total_military)
        scoreboard.report()

        city_checker()




    except:
        if KeyboardInterrupt:
            raise
        else:
            print("\n\nThere was an error. ")


simulation()

