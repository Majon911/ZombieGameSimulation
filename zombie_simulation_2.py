# zombie_simulation.py
import random
import militaryclass as mc

total_population = 0
total_zombies = 0
days = 0
deaths = 0


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
        self.active_military_personnel = []
        self.dead_military_personnel = []


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



# Creating the map / cities
MackersCity = city("Mackers City", 1000)
GulansTown = city("Gulans Town", 500)
NogalesVillage = city("Nogales Village", 500)
map = [MackersCity, GulansTown, NogalesVillage]



# The simulation per day
def day_sim(day_number):
    print("\n--Today is day number", day_number, "--")
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
    deaths = ["starvation"] * 1 + ["food poisoning"] * 2 + ["dehydration"] * 3 + ["suicide"] * 5 + ["unknown causes"] * 5
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
        elif probability < 0.03:
            death_citizens = 1
            death_type = "dehydration"
        elif probability < 0.05:
            death_citizens = 1
            death_type = "suicide"
        elif probability < 0.05:
            death_citizens = 1
            death_type = "unknown causes"

    for i in range(death_citizens):
        citizen = random.randint(1, city_population)
        print("Citizen {} in this city has died of {}.".format(citizen, death_type))
    
    
    
    
    # city_checker() "I modified it adding a new variable (death_count) however it has to be changed in the future because there will be 2 (for zombies and humans) and adding the function (non_zombie_fatalities)" "Sergio"

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

        # Instantiating the military
        for i in range(1, 51):
            m = mc.Military(i, "Solider", random.randrange(1, 6))
            city.active_military_personnel.append(m)
        for i in range(1, 11):
            m = mc.Military(i, "Tank", random.randrange(1, 4))
            city.active_military_personnel.append(m)
        for i in range(1, 6):
            m = mc.Military(i, "Bomber", random.randrange(1, 3))
            city.active_military_personnel.append(m)
        for i in range(1, 21):
            m = mc.Military(i, "Solider Armoured", random.randrange(1, 6))
            city.active_military_personnel.append(m)
        for i in range(1):
            m = mc.Military(i, "Tactical Nuke", 1)
            city.active_military_personnel.append(m)


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

