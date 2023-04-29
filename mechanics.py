import random
import zombie_simulation_2 as zs
import concurrent.futures

citizen_queue_init = []
citizen_id = 0
for i in range(1000):
    city_prob = random.choices([zs.MackersCity, zs.GulansTown, zs.NogalesVillage, zs.AlbonoHills, zs.ZeidelBorough], [3, 2, 2, 1, 2])
    citizen_queue_init.append(zs.Citizen(citizen_id, city_prob))
    citizen_id = citizen_id + 1

military_queue_init = []
military_id = 0
for i in range(100):
    city_prob = random.choices([zs.MackersCity, zs.GulansTown, zs.NogalesVillage, zs.AlbonoHills, zs.ZeidelBorough], [3, 2, 2, 1, 2])
    mtype = random.choices(["Soldier", "Soldier Armoured", "Tank", "Plane"], [5, 4, 2, 1])
    mrank = random.choices([1, 2, 3], [6, 3, 1])
    military_queue_init.append(zs.Military(military_id, mtype, mrank, city_prob))
    military_id = military_id + 1

medic_queue_init = []
medic_id = 0
for i in range(50):
    city_prob = random.choices([zs.MackersCity, zs.GulansTown, zs.NogalesVillage, zs.AlbonoHills, zs.ZeidelBorough], [3, 2, 2, 1, 2])
    medic_queue_init.append(zs.Medic(medic_id, "Medic", city_prob))
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
