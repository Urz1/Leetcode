class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        smoothed_img = [[0] * cols for _ in range(rows)]  

        for i in range(rows):
            for j in range(cols):
                count = 0
                summ = 0
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        summ += img[x][y]
                        count += 1
                smoothed_img[i][j] = summ // count  

        return smoothed_img

