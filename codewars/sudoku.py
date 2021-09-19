def done_or_not(board):
    numbers = [set() for _ in range(0, 9, 1)]
    for i in range(0, 9, 1):
        numbers_horinzotal = set()
        numbers_vertical = set()
        for j in range(0, 9, 1):
            numbers_horinzotal.add(board[i][j])
            numbers_vertical.add(board[j][i])
            if i < 3 and j < 3:
                numbers[0].add(board[i][j])
            elif i < 3 and j > 2 and j < 6:
                numbers[1].add(board[i][j])
            elif i < 3 and j > 5 and j < 9:
                numbers[2].add(board[i][j])
            elif i < 6 and j < 3:
                numbers[3].add(board[i][j])
            elif i < 6 and j > 2 and j < 6:
                numbers[4].add(board[i][j])
            elif i < 6 and j > 5 and j < 9:
                numbers[5].add(board[i][j])
            elif i < 9 and j < 3:
                numbers[6].add(board[i][j])
            elif i < 9 and j > 2 and j < 6:
                numbers[7].add(board[i][j])
            elif i < 9 and j > 5 and j < 9:
                numbers[8].add(board[i][j])

        if len(numbers_horinzotal) != 9 or len(numbers_vertical) != 9:
            return 'Try again!'

    for e in numbers:
        if len(e) != 9:
            return 'Try again!'

    return 'Finished!'

