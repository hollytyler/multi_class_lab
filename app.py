from person import Person
from bus import Bus
from bus_stop import BusStop


person_1 = Person("Brandon", 26)
person_2 = Person("Ying", 34)
person_3 = Person("Holly", 27)


print("There are 3 passengers.")
print(f"Name: {person_1.name}, Age: {person_1.age}.")
print(f"Name: {person_2.name}, Age: {person_2.age}.")
print(f"Name: {person_3.name}, Age: {person_3.age}.")

bus = Bus(22, "Ocean Terminal",)
print(f"The {bus.route_number} bus is heading to {bus.destination}.")
print(f"The {bus.route_number} bus has left the station. {bus.drive()}.")

starting_passenger_count = bus.passenger_count()
print(f"There are initially {starting_passenger_count} passengers on the bus.")

bus.pick_up(person_1)
print(f"The {bus.route_number} bus picked up {bus.passengers[0].name}.")

bus.drop_off(person_1)
print(f"The {bus.route_number} bus dropped off {person_1.name}.")

bus.pick_up(person_1)
bus.pick_up(person_2)
bus.pick_up(person_3)
print(f"The {bus.route_number} bus picked up {bus.passenger_count()} passengers.")

bus.empty_bus()
print(f"The {bus.route_number} bus dropped off all of its passengers.")

bus_stop = BusStop("Buchanan Bus Station")
print(f"There are {bus_stop.queue_length()} pasengers waiting at {bus_stop.name}.")

bus_stop.add_to_queue(person_1)
bus_stop.add_to_queue(person_2)
bus_stop.add_to_queue(person_3)
print(f"{bus_stop.queue_length()} passengers have joined the queue at {bus_stop.name}.")

print(f"{bus_stop.queue_length()} passengers are leaving the queue.")
bus_stop.clear()
print(f"There are now {bus_stop.queue_length()} passengers in the queue.")

bus_stop.add_to_queue(person_1)
bus_stop.add_to_queue(person_2)
bus_stop.add_to_queue(person_3)
bus.pick_up_from_stop(bus_stop)
print(f"The {bus.route_number} bus picked up {bus.passenger_count()} passengers from {bus_stop.name}.")
