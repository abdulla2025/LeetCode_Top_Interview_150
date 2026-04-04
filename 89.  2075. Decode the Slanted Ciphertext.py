class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        number_of_cols = len(encodedText) // rows
        step_size = number_of_cols + 1

        decoded_chars = []

        for starting_col in range(number_of_cols):
            row = 0
            while row < rows:
                flat_index = row * number_of_cols + starting_col
                if flat_index < len(encodedText):
                    decoded_chars.append(encodedText[flat_index])
                row += 1
                starting_col += 1

        return "".join(decoded_chars).rstrip()
