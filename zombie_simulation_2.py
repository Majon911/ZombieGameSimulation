# zombie_simulation.py
import random

total_population = 0
total_zombies = 0
days = 0
deaths = 0


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


class citizen:
    def __init__(self, id, city):
        self.id = id
        self.infected = None
        self.zombie_id = None
        self.city = city
        self.city.healthy_queue.append(self)


    def zombify(self):
        if not self.infected:
            print("Citizen", self.id, "has been infected! ")
            self.city.zombie_queue.append(self)
            self.city.healthy_queue.remove(self)






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
    # print(infected)
    c = city.healthy_queue[infected]
    c.zombify()






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

        scoreboard = statistics(total_zombies, days, deaths)
        scoreboard.report()

    except:
        if KeyboardInterrupt:
            raise
        else:
            print("\n\nThere was an error. ")


simulation()


