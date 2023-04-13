import random

class Military:

    def __init__(self, id, type, rank):
        self.id = id
        self.type = type
        self.rank = rank

    def zombie_destruction(self):
        chance = random.randrange(1, 31)
        # if self.type == "Solider":
        #     if chance == 10 or 15 or 20:
        #         main.map.zombie_queue.pop(0)
        # if self.type == "Tank":
        #     if chance == 1 or 2 or 3 or 4 or 5 or 16 or 17 or 18 or 19 or 20:
        #         map.zombie_queue.pop(0)
        # if self.type == "Bomber":
        #     if chance == 1 or 2 or 3 or 4 or 5 or 16 or 17 or 18 or 19 or 20 or 25 or 26 or 27 or 28 or 19 or 30:
        #         map.zombie_queue.pop(0)
        # if self.type == "Solider Armoured":
        #     if chance == 1 or 5 or 10 or 15 or 20 or 25 or 30:
        #         map.zombie_queue.pop(0)
        # if self.type == "Tactical Nuke":
        #     if len(map.zombie_queue)/(len(map.zombie_queue)+len(map.healthy_queue)) > 0.95:
        #         print(f"City: {city.name}, has been TACTICAL NUKED by the MILITARY!!!")
        #         map.remove(city.name)

    def zombify(self):
        pass