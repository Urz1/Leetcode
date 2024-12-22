class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        tracker = {list1[i]: [i] for i in range(len(list1))}
        minIndex = float('inf')
        commonRestaurants = []

        # Iterate through list2 to find common restaurants and calculate index sums
        for i in range(len(list2)):
            if list2[i] in tracker:
                indexSum = tracker[list2[i]][0] + i
                if indexSum <= minIndex:
                    minIndex = indexSum
                tracker[list2[i]].append(i)

       # Collect restaurants with the smallest index sum
        for restaurant in tracker:
            if len(tracker[restaurant]) > 1 and sum(tracker[restaurant]) == minIndex:
                commonRestaurants.append(restaurant)

        return commonRestaurants