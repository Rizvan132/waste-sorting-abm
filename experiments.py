
import random
from collections import deque

def run_simulation(accuracy, capacity, seed):
    rng = random.Random(seed)

    materials = ["plastic", "paper", "metal"]
    waste_items = [
        rng.choice(materials)
        for _ in range(50)
    ]

    queues = [deque(), deque()]

    # Distribute waste between two stations
    for i, material in enumerate(waste_items):
        queues[i % 2].append(material)

    correct = 0
    processed = 0
    steps = 0

    while any(queues):
        steps += 1

        for queue in queues:
            for _ in range(min(capacity, len(queue))):
                material = queue.popleft()

                if rng.random() < accuracy:
                    correct += 1

                processed += 1

    return {
        "accuracy": correct / processed * 100,
        "steps": steps
    }


# Test different scenarios
accuracies = [0.70, 0.85, 0.95]
capacities = [2, 5, 10]

print("Accuracy | Capacity | Avg Correct % | Avg Steps")
print("-" * 50)

for accuracy in accuracies:
    for capacity in capacities:

        results = [
            run_simulation(accuracy, capacity, seed)
            for seed in range(100)
        ]

        avg_correct = sum(
            result["accuracy"] for result in results
        ) / len(results)

        avg_steps = sum(
            result["steps"] for result in results
        ) / len(results)

        print(
            f"{accuracy*100:6.0f}% | "
            f"{capacity:8d} | "
            f"{avg_correct:12.1f}% | "
            f"{avg_steps:9.1f}"
        )
