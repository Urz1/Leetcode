class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        tracker = {list1[i]:[i] for i in range(len(list1))}
        minIndex = float('inf')
        Cstring = []
        for key in range(len(list2)):
            if list2[key] in tracker:
                if minIndex >= sum(tracker[list2[key]]) + key:
                    minIndex = sum(tracker[list2[key]]) + key
                tracker[list2[key]].append(key)
        for keys in tracker:
            if len(tracker[keys]) > 1 and tracker[keys][0] + tracker[keys][1] == minIndex:
                Cstring.append(keys)
        return Cstring
        