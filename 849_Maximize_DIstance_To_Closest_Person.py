from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        ranges_to_left_seater, ranges_to_right_seater = [0] * len(seats), [0] * len(seats)

        flag = False
        count_to_nearest = float('inf')
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 0:
                ranges_to_right_seater[i] = count_to_nearest
                count_to_nearest += 1
            else:
                count_to_nearest = 0
                ranges_to_right_seater[i] = count_to_nearest


        count_to_nearest = float('inf')
        for i in range(len(seats)):
            if seats[i] == 0:
                count_to_nearest += 1
                ranges_to_left_seater[i] = count_to_nearest
            else:
                count_to_nearest = 0
                ranges_to_left_seater[i] = count_to_nearest

        maximum = 0
        for i in zip(ranges_to_left_seater, ranges_to_right_seater):
            cur_max = min(i)
            if maximum < cur_max:
                maximum = cur_max

        return maximum
