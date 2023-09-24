def isValidSudoku(board):
    def is_valid_row(row):
        seen = set()
        for num in row:
            if num == ".":
                continue
            if num in seen:
                return False
            seen.add(num)
        return True

    def is_valid_col(col):
        seen = set()
        for row in board:
            num = row[col]
            if num == ".":
                continue
            if num in seen:
                return False
            seen.add(num)
        return True

    def is_valid_box(row, col):
        seen = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                num = board[i][j]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        return True

    for i in range(9):
        if not is_valid_row(board[i]) or not is_valid_col(i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_box(i, j):
                return False

    return True

def read_sudoku():
    sudoku = []
    for _ in range(9):
        row = input("Enter a row (9 digits, use '.' for empty cells): ").strip()
        if len(row) != 9 or not row.isdigit() and not all(ch == '.' for ch in row):
            print("Invalid input. Please enter 9 digits or '.' for empty cells.")
            return None
        sudoku.append(list(row))
    return sudoku

def main():
    sudoku = read_sudoku()
    if sudoku is not None:
        if isValidSudoku(sudoku):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
