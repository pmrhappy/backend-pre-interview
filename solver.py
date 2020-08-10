def read_data(file_name='sudoku.txt' ):
    question_data = {}
    puzzle_row_amount = 9
    with open(file_name, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            puzzle_name = line.strip('\n')
            if line.startswith('Grid'):
                question_data[puzzle_name] = []
                for _r in range(puzzle_row_amount):
                    row = fp.readline().strip('\n')
                    question_data[puzzle_name].append([int(num) for num in row])
    return question_data


def is_candidate(puzzle, row, col, num):
    col_data = [puzzle[r][col] for r in range(9)]
    square_row_start = row - (row % 3)
    square_col_start = col - (col % 3)
    square_data = []
    for r in range(3):
        square_data.extend(puzzle[square_row_start+r][square_col_start:square_col_start+3])
    return num not in puzzle[row] and num not in col_data and num not in square_data


def solve_puzzle(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1,10):
                    if is_candidate(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve_puzzle(puzzle):
                            break
                        else:
                            puzzle[row][col] = 0
                else:
                    return False
    return True


def main():
    data = read_data()
    for name, puzzle in data.items():
        solve_puzzle(puzzle)
    
    answer = 0
    for sol in data.values():
        answer += sum(sol[0][:3])
    print("answer: ", answer)


if __name__ == '__main__':
    main()
