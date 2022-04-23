def run(self):
    a = 0 #dummy variable to count the number of simulations the program runs
    l = {'x': 0, 'o': 0, 'tie': 0} #list to count the winner
    turns_made_list = []
    while a < self:
        o = simulation() #runs simulation
        winner = o[0] #first output gives winner
        turns = o[1] #second output gives length of game
        l[winner] += 1 #places result in dictionary
        a += 1 #while loop ends after a=self
        if turns != 0:
            turns_made_list.append(turns)
    turns_made_list_length = len(turns_made_list)
    sum_of_turns = 0
    for n in turns_made_list:
        sum_of_turns = sum_of_turns + n
    if turns_made_list_length != 0:
        turns_made_average=sum_of_turns / turns_made_list_length
    else:
        turns_made_average = 0
    return l, turns_made_average
def simulation():
    board0 = [[[],[],[]],[[],[],[]],[[],[],[]]] #3x3 tic tac toe board (bottom)
    board1 = [[[],[],[]],[[],[],[]],[[],[],[]]] #3x3 tic tac toe board (middle)
    board2 = [[[],[],[]],[[],[],[]],[[],[],[]]] #3x3 tic tac toe board (top)
    import random
    turns = 0 #variable to determine how many moves it takes before the game finishes
    p = 0 #p is the sister variable to o; used to determine whose turn it is
    y = 1 #y is the sister variable to x; used to determine whose turn it is; x goes first (y==1)
    while turns >= 0: #condition that is always satisfied so it always loops until the end, also counts length of gameplay
        if y == 1: #if it is 'x' turn
            y = 0
            p = 1 #it will be 'o' turn next
            move = 'x' #when the move is made, an x will be placed on the spot
        elif p == 1: #if it is 'o' turn
            y = 1 #it will be 'x' turn next
            p = 0
            move = 'o' #when the move is made, an o will be placed on the spot
        random_row = random.randint(0, 2) #random number generator to determine row
        random_col = random.randint(0, 2) #random number generator to determine column
        random_hei = random.randint(0, 2) #random number generator to determine height
        discard0 = {} #stores unique coordinate values that are unavaliable; if length is 9, all board spots are taken
        discard1 = {}
        discard2 = {}
        if random_hei == 0:
            board = board0
            discard = discard0
        if random_hei == 1:
            board = board1
            discard = discard1
        if random_hei == 2:
            board = board2
            discard = discard2
        while board[random_row][random_col] == 'x' or board[random_row][random_col] == 'o':
            discard[(random_row,random_col)] = 1 #1 is a placeholder to show coordinate value is stored in discard pile
            if len(discard0) + len(discard1) + len(discard2) == 27:
                print(board0, board1, board2)
                return 'tie', 0
            else:
                random_row = random.randint(0, 2) #program continues to produce random values
                random_col = random.randint(0, 2)
                random_hei = random.randint(0, 2)
                if random_hei == 0:
                    board = board0
                    discard = discard0
                if random_hei == 1:
                    board = board1
                    discard = discard1
                if random_hei == 2:
                    board = board2
                    discard = discard2
        board[random_row][random_col] = move #places the move at a specific location
        turns += 1 #turns increase by 1 after move is made
        #checks all possible winning combinations
        board = board0 #checks bottom board for three in a row
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[0][1] == 'x' or board[0][1] == 'o') and (board[0][2] == 'x' or board[0][2] == 'o'):
            if board[0][0] == board[0][1] and board[0][0] == board[0][2]: #top row
                return board[0][0], turns
        if (board[1][0] == 'x' or board[1][0] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[1][2] == 'x' or board[1][2] == 'o'):
            if board[1][0] == board[1][1] and board[1][0] == board[1][2]: #middle row
                return board[1][0], turns
        if (board[2][0] == 'x' or board[2][0] == 'o') and (board[2][1] == 'x' or board[2][1] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[2][0] == board[2][1] and board[2][0] == board[2][2]: #bottom row
                return board[2][0], turns
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[1][0] == 'x' or board[1][0] == 'o') and (board[2][0] == 'x' or board[2][0] == 'o'):
            if board[0][0] == board[1][0] and board[0][0] == board[2][0]: #left column
                return board[0][0], turns
        if (board[0][1] == 'x' or board[0][1] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][1] == 'x' or board[2][1] == 'o'):
            if board[0][1] == board[1][1] and board[0][1] == board[2][1]: #middle column
                return board[0][1], turns
        if (board[0][2] == 'x' or board[0][2] == 'o') and (board[1][2] == 'x' or board[1][2] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[0][2] == board[1][2] and board[0][2] == board[2][2]: #right column
                return board[0][2], turns
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]: #diagonal top left to bottom right
                return board[0][0], turns
        if (board[0][2] == 'x' or board[0][2] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][0] == 'x' or board[2][0] == 'o'):
            if board[0][2] == board[1][1] and board[0][2] == board[2][0]: #diagonal top right to bottom left
                return board[0][2], turns
        ###
        board = board1 #checks middle board for three in a row
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[0][1] == 'x' or board[0][1] == 'o') and (board[0][2] == 'x' or board[0][2] == 'o'):
            if board[0][0] == board[0][1] and board[0][0] == board[0][2]: #top row
                return board[0][0], turns
        if (board[1][0] == 'x' or board[1][0] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[1][2] == 'x' or board[1][2] == 'o'):
            if board[1][0] == board[1][1] and board[1][0] == board[1][2]: #middle row
                return board[1][0], turns
        if (board[2][0] == 'x' or board[2][0] == 'o') and (board[2][1] == 'x' or board[2][1] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[2][0] == board[2][1] and board[2][0] == board[2][2]: #bottom row
                return board[2][0], turns
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[1][0] == 'x' or board[1][0] == 'o') and (board[2][0] == 'x' or board[2][0] == 'o'):
            if board[0][0] == board[1][0] and board[0][0] == board[2][0]: #left column
                return board[0][0], turns
        if (board[0][1] == 'x' or board[0][1] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][1] == 'x' or board[2][1] == 'o'):
            if board[0][1] == board[1][1] and board[0][1] == board[2][1]: #middle column
                return board[0][1], turns
        if (board[0][2] == 'x' or board[0][2] == 'o') and (board[1][2] == 'x' or board[1][2] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[0][2] == board[1][2] and board[0][2] == board[2][2]: #right column
                return board[0][2], turns
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]: #diagonal top left to bottom right
                return board[0][0], turns
        if (board[0][2] == 'x' or board[0][2] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][0] == 'x' or board[2][0] == 'o'):
            if board[0][2] == board[1][1] and board[0][2] == board[2][0]: #diagonal top right to bottom left
                return board[0][2], turns
        ###
        board = board2 #checks top board for three in a row
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[0][1] == 'x' or board[0][1] == 'o') and (board[0][2] == 'x' or board[0][2] == 'o'):
            if board[0][0] == board[0][1] and board[0][0] == board[0][2]: #top row
                return board[0][0], turns
        if (board[1][0] == 'x' or board[1][0] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[1][2] == 'x' or board[1][2] == 'o'):
            if board[1][0] == board[1][1] and board[1][0] == board[1][2]: #middle row
                return board[1][0], turns
        if (board[2][0] == 'x' or board[2][0] == 'o') and (board[2][1] == 'x' or board[2][1] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[2][0] == board[2][1] and board[2][0] == board[2][2]: #bottom row
                return board[2][0], turns
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[1][0] == 'x' or board[1][0] == 'o') and (board[2][0] == 'x' or board[2][0] == 'o'):
            if board[0][0] == board[1][0] and board[0][0] == board[2][0]: #left column
                return board[0][0], turns
        if (board[0][1] == 'x' or board[0][1] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][1] == 'x' or board[2][1] == 'o'):
            if board[0][1] == board[1][1] and board[0][1] == board[2][1]: #middle column
                return board[0][1], turns
        if (board[0][2] == 'x' or board[0][2] == 'o') and (board[1][2] == 'x' or board[1][2] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[0][2] == board[1][2] and board[0][2] == board[2][2]: #right column
                return board[0][2], turns
        if (board[0][0] == 'x' or board[0][0] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][2] == 'x' or board[2][2] == 'o'):
            if board[0][0] == board[1][1] and board[0][0] == board[2][2]: #diagonal top left to bottom right
                return board[0][0], turns
        if (board[0][2] == 'x' or board[0][2] == 'o') and (board[1][1] == 'x' or board[1][1] == 'o') and (board[2][0] == 'x' or board[2][0] == 'o'):
            if board[0][2] == board[1][1] and board[0][2] == board[2][0]: #diagonal top right to bottom left
                return board[0][2], turns
        ###
        #checks columns down all boards for three in a row
        if (board0[0][0] == 'x' or board0[0][0] == 'o') and (board1[0][0] == 'x' or board1[0][0] == 'o') and (board2[0][0] == 'x' or board2[0][0] == 'o'):
            if board0[0][0] == board1[0][0] and board0[0][0] == board2[0][0]: #top left
                return board0[0][0], turns
        if (board0[1][0] == 'x' or board0[1][0] == 'o') and (board1[1][0] == 'x' or board1[1][0] == 'o') and (board2[1][0] == 'x' or board2[1][0] == 'o'):
            if board0[1][0] == board1[1][0] and board0[1][0] == board2[1][0]: #middle left
                return board0[1][0], turns
        if (board0[2][0] == 'x' or board0[2][0] == 'o') and (board1[2][0] == 'x' or board1[2][0] == 'o') and (board2[2][0] == 'x' or board2[2][0] == 'o'):
            if board0[2][0] == board1[2][0] and board0[2][0] == board2[2][0]: #bottom left
                return board0[2][0], turns
        if (board0[0][1] == 'x' or board[0][1] == 'o') and (board1[0][1] == 'x' or board1[0][1] == 'o') and (board2[0][1] == 'x' or board2[0][1] == 'o'):
            if board0[0][1] == board1[0][1] and board0[0][1] == board2[0][1]: #top middle
                return board0[0][1], turns
        if (board0[1][1] == 'x' or board0[1][1] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[1][0] == 'x' or board2[1][0] == 'o'):
            if board0[1][1] == board1[1][1] and board0[1][1] == board2[1][1]: #middle middle
                return board0[1][1], turns
        if (board0[2][1] == 'x' or board0[2][1] == 'o') and (board1[2][1] == 'x' or board1[2][1] == 'o') and (board2[2][1] == 'x' or board2[2][1] == 'o'):
            if board0[2][1] == board1[2][1] and board0[2][1] == board2[2][1]: #bottom middle
                return board0[2][1], turns
        if (board0[0][2] == 'x' or board0[0][2] == 'o') and (board1[0][2] == 'x' or board1[0][2] == 'o') and (board2[0][2] == 'x' or board2[0][2] == 'o'):
            if board0[0][2] == board1[0][2] and board0[0][2] == board2[0][2]: #top right
                return board0[0][2], turns
        if (board0[1][2] == 'x' or board0[1][2] == 'o') and (board1[1][2] == 'x' or board1[1][2] == 'o') and (board2[1][2] == 'x' or board2[1][2] == 'o'):
            if board0[1][2] == board1[1][2] and board0[1][2] == board2[1][2]: #middle right
                return board0[1][2], turns
        if (board0[2][2] == 'x' or board0[2][2] == 'o') and (board1[2][2] == 'x' or board1[2][2] == 'o') and (board2[2][2] == 'x' or board2[2][2] == 'o'):
            if board0[2][2] == board1[2][2] and board0[2][2] == board2[2][2]: #bottom right
                return board0[2][2], turns
        ###
        #checks diagonals across all boards for three in a row
        if (board0[0][0] == 'x' or board0[0][0] == 'o') and (board1[0][1] == 'x' or board1[0][1] == 'o') and (board2[0][2] == 'x' or board2[0][2] == 'o'):
            if board0[0][0] == board1[0][1] and board0[0][0] == board2[0][2]: #back diagonal top right to bottom left
                return board0[0][0], turns
        if (board0[1][0] == 'x' or board0[1][0] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[1][2] == 'x' or board2[1][2] == 'o'):
            if board0[1][0] == board1[1][1] and board0[1][0] == board2[1][2]: #middle diagonal top right to bottom left
                return board0[1][0], turns
        if (board0[2][0] == 'x' or board0[2][0] == 'o') and (board1[2][1] == 'x' or board1[2][1] == 'o') and (board2[2][2] == 'x' or board2[2][2] == 'o'):
            if board0[2][0] == board1[2][1] and board0[2][0] == board2[2][2]: #front diagonal top right to bottom left
                return board0[2][0], turns
            
        if (board0[0][2] == 'x' or board0[0][2] == 'o') and (board1[0][1] == 'x' or board1[0][1] == 'o') and (board2[0][0] == 'x' or board2[0][0] == 'o'):
            if board0[0][2] == board1[0][1] and board0[0][2] == board2[0][0]: #back diagonal top left to bottom right
                return board0[0][2], turns
        if (board0[1][2] == 'x' or board0[1][2] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[1][0] == 'x' or board2[1][0] == 'o'):
            if board0[1][2] == board1[1][1] and board0[1][2] == board2[1][0]: #middle diagonal top left to bottom right
                return board0[1][2], turns
        if (board0[2][2] == 'x' or board0[2][2] == 'o') and (board1[2][1] == 'x' or board1[2][1] == 'o') and (board2[2][0] == 'x' or board2[2][0] == 'o'):
            if board0[2][2] == board1[2][1] and board0[2][2] == board2[2][0]: #front diagonal top left to bottom right
                return board0[2][2], turns
            
        if (board0[0][0] == 'x' or board0[0][0] == 'o') and (board1[1][0] == 'x' or board1[1][0] == 'o') and (board2[2][0] == 'x' or board2[2][0] == 'o'):
            if board0[0][0] == board1[1][0] and board0[0][0] == board2[2][0]: #left diagonal bottom back to front top
                return board0[0][0], turns
        if (board0[0][1] == 'x' or board0[0][1] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[2][1] == 'x' or board2[2][1] == 'o'):
            if board[0][1] == board[1][1] and board[0][1] == board[2][1]: #middle diagonal bottom back to front top
                return board0[0][1], turns
        if (board0[0][2] == 'x' or board0[0][2] == 'o') and (board1[1][2] == 'x' or board1[1][2] == 'o') and (board2[2][2] == 'x' or board2[2][2] == 'o'):
            if board0[0][2] == board1[1][2] and board0[0][2] == board2[2][2]: #right diagonal bottom back to front top 
                return board0[0][2], turns
            
        if (board0[2][0] == 'x' or board0[2][0] == 'o') and (board1[1][0] == 'x' or board1[1][0] == 'o') and (board2[0][0] == 'x' or board2[0][0] == 'o'):
            if board0[2][0] == board1[1][0] and board0[2][0] == board2[0][0]: #left diagonal bottom front to top back
                return board0[2][0], turns
        if (board0[2][1] == 'x' or board0[2][1] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[0][1] == 'x' or board2[0][1] == 'o'):
            if board0[2][1] == board1[1][1] and board0[2][1] == board2[0][1]: #middle diagonal bottom front to top back
                return board0[2][1], turns
        if (board0[2][2] == 'x' or board0[2][2] == 'o') and (board1[1][2] == 'x' or board1[1][2] == 'o') and (board2[0][2] == 'x' or board2[0][2] == 'o'):
            if board0[2][2] == board1[1][2] and board0[2][2] == board2[0][2]: #right diagonal bottom front to top back
                return board0[2][2], turns
            
        if (board0[0][0] == 'x' or board0[0][0] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[2][2] == 'x' or board2[2][2] == 'o'):
            if board0[0][0] == board1[1][1] and board0[0][0] == board2[2][2]: #diagonal back bottom left to front top right
                return board0[0][0], turns
        if (board0[0][2] == 'x' or board0[0][2] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[2][0] == 'x' or board2[2][0] == 'o'):
            if board0[0][2] == board1[1][1] and board0[0][2] == board2[2][0]: #diagonal back bottom right to front top left
                return board0[0][2], turns
        if (board0[2][2] == 'x' or board0[2][2] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[0][0] == 'x' or board2[0][0] == 'o'):
            if board0[2][2] == board1[1][1] and board0[2][2] == board2[0][0]: #diagonal back top left to front bottom right
                return board0[2][2], turns
        if (board0[2][0] == 'x' or board0[2][0] == 'o') and (board1[1][1] == 'x' or board1[1][1] == 'o') and (board2[0][2] == 'x' or board2[0][2] == 'o'):
            if board0[2][0] == board1[1][1] and board0[2][0] == board2[0][2]: #diagonal back top right to front bottom left
                return board0[2][0], turns

#the value inside parentesis is the number of times the program is to run
print(run(100))