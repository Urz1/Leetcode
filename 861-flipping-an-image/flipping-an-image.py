class Solution(object):
    def flipAndInvertImage(self, image):
        for element in image:
            element = element.reverse()
        for elem in image:
            for j in range(len(image)):
                if elem[j] == 0:
                    elem[j] =1
                else:
                    elem[j] = 0
        return image