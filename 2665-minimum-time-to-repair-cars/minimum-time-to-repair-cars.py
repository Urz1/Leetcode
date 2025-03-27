class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # work on it again
        def can_repair_in_time(time):
            total_cars = 0
            for r in ranks:
                n = int((time // r) ** 0.5)
                total_cars += n
            return total_cars >= cars
        
        left = 0
        right = min(ranks) * cars * cars  
        
        while left < right:
            mid = (left + right) // 2
            if can_repair_in_time(mid):
                right = mid
            else:
                left = mid + 1
        
        return left