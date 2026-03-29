class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = sorted(zip(position, speed))

        fleets = 0
        time_for_fleet = -1

        while len(pair) > 0:
            p, s = pair.pop()
            time_for_car = (target - p) / s

            if time_for_car > time_for_fleet:
                fleets += 1
                time_for_fleet = time_for_car
        
        return fleets