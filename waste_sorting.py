from dataclasses import dataclass
import random


# Define a waste item
@dataclass
class WasteItem:
	item_id: int
	material: str
	sorted: bool = False


# Our waste categories
materials = ["plastic", "paper", "metal"]

# Create 50 waste items
random.seed(42)
waste_items = []

for i in range(50):
	item = WasteItem(
		item_id=i + 1,
		material=random.choice(materials)
	)
	waste_items.append(item)

# Display results
print("Total waste items:", len(waste_items))

for item in waste_items[:5]:
	print(item)




# Stage 2: Create sorting stations

@dataclass
class SortingStation:
    station_id: int
    name: str
    capacity: int

station1 = SortingStation(
    station_id=1,
    name="Station A",
    capacity=5
)

station2 = SortingStation(
    station_id=2,
    name="Station B",
    capacity=5
)

stations = [station1, station2]

print("\nSorting stations created:")

for station in stations:
    print(station)





# Stage 3: Simulate computer vision classification

classification_accuracy = 0.85

def classify_waste(item):
    # Decide whether the prediction is correct
    if random.random() < classification_accuracy:
        return item.material

    # If incorrect, choose a different material
    wrong_materials = [
        material for material in materials
        if material != item.material
    ]

    return random.choice(wrong_materials)


# Test classification for all 50 waste items
correct_predictions = 0

for item in waste_items:
    predicted_material = classify_waste(item)

    if predicted_material == item.material:
        correct_predictions += 1

accuracy = correct_predictions / len(waste_items) * 100

print("\nComputer Vision Classification Results")
print("Total items:", len(waste_items))
print("Correct predictions:", correct_predictions)
print("Incorrect predictions:", len(waste_items) - correct_predictions)
print(f"Observed accuracy: {accuracy:.1f}%")




# Stage 4: Sorting stations and queues

from collections import deque

# Reset processing status
for item in waste_items:
    item.sorted = False

# Assign waste items alternately to two stations
queues = {
    station.station_id: deque()
    for station in stations
}

for index, item in enumerate(waste_items):
    station = stations[index % len(stations)]
    queues[station.station_id].append(item)

# Process the waste items
step = 0
total_processed = 0
correctly_sorted = 0

print("\nSorting Simulation")

while any(queues.values()):
    step += 1

    for station in stations:
        queue = queues[station.station_id]

        for _ in range(min(station.capacity, len(queue))):
            item = queue.popleft()

            predicted_material = classify_waste(item)
            item.sorted = True

            total_processed += 1

            if predicted_material == item.material:
                correctly_sorted += 1

    remaining = sum(len(queue) for queue in queues.values())

    print(
        f"Step {step}: "
        f"Processed = {total_processed}, "
        f"Waiting = {remaining}"
    )

print("\nFinal Results")
print("Total processed:", total_processed)
print("Correctly sorted:", correctly_sorted)
print("Incorrectly sorted:", total_processed - correctly_sorted)
print("Simulation steps:", step)



