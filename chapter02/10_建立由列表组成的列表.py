# ex2-12 一个包含3个列表的列表
board = [['#'] * 3 for _ in range(3)]
print(board)
board[1][2] = 'x'
print(board)    # [['#', '#', '#'], ['#', '#', 'x'], ['#', '#', '#']]

# ex2-13 含有3个指向同一个对象的引用的列表
werid_board = [['#'] * 3] * 3
print(werid_board)
werid_board[1][2] = 'X'
print(werid_board)  # [['#', '#', 'X'], ['#', '#', 'X'], ['#', '#', 'X']]
