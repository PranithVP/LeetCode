from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    cars = sorted([(position[i], speed[i]) for i in range(len(position))], reverse=True)
    curr, fleets = 0, 0

    for i in range(len(cars)):
        if i == 0:
            fleets += 1
            curr = (target - cars[i][0]) / cars[i][1]
        else:
            arrival = (target - cars[i][0]) / cars[i][1]
            if arrival <= curr:
                continue
            else:
                fleets += 1
                curr = arrival
    return fleets