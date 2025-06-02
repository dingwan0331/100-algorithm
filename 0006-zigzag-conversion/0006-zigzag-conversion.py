class Solution:
    def convert(self,s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        row_index = 0
        direction = 1  # 1 for down, -1 for up

        for char in s:
            rows[row_index] += char

            row_index += direction
            if row_index == numRows - 1 or row_index == 0:
                direction *= -1

        return ''.join(rows)
