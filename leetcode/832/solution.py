def pretty_print(matrix):
    print()
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
        for i, row in enumerate(image):
            for j, cell in enumerate(row):
                image[i][j] = 1 - cell
        return image
