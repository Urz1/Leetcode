class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr = [0]*2
        arr[0] = celsius + 273.15
        arr[1] = celsius * 1.8 + 32
        return arr
