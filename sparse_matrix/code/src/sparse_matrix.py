#! /usr/bin/python3


class SparseMatrix:
    def __init__(self, matrix_file_path=None, num_rows=None, num_cols=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = {}
        if matrix_file_path:
            self.load_matrix(matrix_file_path)

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for addition")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        result.elements = self.elements.copy()

        for (row, col), value in other.elements.items():
            new_value = result.get_element(row, col) + value
            result.set_element(row, col, new_value)

        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match for subtraction")


        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)

        result.elements = self.elements.copy()
        for (row, col), value in other.elements.items():
            new_value = result.get_element(row, col) - value
            result.set_element(row, col, new_value)
        return result

    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrices dimensions do not match for multiplication")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)

        for (row1, col1), value1 in self.elements.items():
            for (row2, col2), value2 in other.elements.items():
                if col1 == row2:
                    result.set_element(row1, col2, result.get_element(row1, col2) + value1 * value2)
        return result

    def load_matrix(self, matrix_file_path):
 
        try:
            with open(matrix_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                self.num_rows = int(lines[0].split('=')[1].strip())
                self.num_cols = int(lines[1].split('=')[1].strip())

                for line in lines[2:]:
                    line = line.strip()
                    if line:
                        row, col, value = map(int, line.strip('()').split(','))
                        self.elements[(row, col)] = value
                return self.elements
        except ValueError as e:
            raise ValueError("Input file has wrong format") from e

    def save_result(self, result_file_path):
        with open(result_file_path, 'w', encoding='utf-8') as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")
            for (row, col), value in self.elements.items():
                file.write(f"({row}, {col}, {value})\n")

    def get_element(self, curr_row, curr_col):
        return self.elements.get((curr_row, curr_col), 0)

    def set_element(self, curr_row, curr_col, value):
        if value != 0:
            self.elements[(curr_row, curr_col)] = value
        elif (curr_row, curr_col) in self.elements:
            del self.elements[(curr_row, curr_col)]

    def __str__(self):
        return f"rows={self.num_rows}\ncols={self.num_cols}\n(elements={self.elements})"
