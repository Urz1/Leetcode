class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for element in image:
            element = element.reverse()
        for elem in image:
            for j in range(len(image)):
                if elem[j] == 0:
                    elem[j] =1
                else:
                    elem[j] = 0
        return image