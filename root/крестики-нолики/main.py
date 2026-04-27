def manual():
    print(''
          '0 | 1 | 2'
          '3 | 4 | 5'
          '6 | 7 | 8')

def start(question):
    answer = None
    while answer not in ('Yes', 'No'):
        answer = input(question).lower()
    return answer

def chips():
    first_step = start('Do you want yo be first?(cross)')
    if first_step == 'Yes':
        print('Okay, ypu play a crosses!')
        human = 'X'
        pc = 'O'
    else:
        human = 'O'
        pc = 'X'

def move_number(low,high):
    answer = None
    while answer not in range(low, high):
        answer = int(input('Make your move, write down the field number(0-8)'))
    return answer

def new_field():
    field = []
    for i in range(size_field):
        field.append(go_ahead)
    return field

def show_field(field):
    print(f"\n\t {field[0]} | {field[1]} | {field[2]}")
    print('\t--------------------------------')
    print(f"\n\t {field[3]} | {field[4]} | {field[5]}")
    print('\t--------------------------------')
    print(f"\n\t {field[6]} | {field[7]} | {field[8]}")
    print('\t--------------------------------')

def available_moves(field):
    available_moves = []
    for i in range(size_field):
        if field[i] == go_ahead:
            available_moves.append((i))
    return available_moves

def winner(field):
    var_win = ((0, 1, 2),
               (3, 4, 5),
               (6, 7, 8),
               (0, 3, 6),
               (1, 4, 7),
               (2, 5, 8),
               (0, 4, 8),
               (2, 4, 6))
    for i in var_win:
        if field[i[0]] == field[i[1]] == field [i[2]] != go_ahead:
            winner = field[i[0]]
        return winner

def pc_move(field, pc, human):
    field = field[:]
    best_move = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('My move: ')
    for i in available_moves(field):
        field[i] = pc
        if winner(field) == pc:
            print(i)
            return i
        field[i] = go_ahead
    for j in available_moves(field):
        field[i] = human
        if winner(field) == human:
            print(j)
            return j
    for k in available_moves(field):
        if k in available_moves(field):
            print(k)
            return k

def numan_move(field, human):
    move = None
    while move not in available_moves(field):
        move = move_number(low: 0, size_field):
        if move not in available_moves(field):
            print('the field is occupied, select the available moves')
        print('Okay')
        return move

def next_queue(queue):
    if queue == X:
        return O
    elsec:
        return X

def congrat_winner(winner, pc, human):
    if winner != draw:
        print(f'The line has been assembled {winner}')
    else:
        print(draw)
    if winner == pc:
        print('PC is winner')
    elif winner == numan:
        print('You winner!')
    elif winner == draw:
        print('Draw!')

X = 'X'
o = 'C'
size_field = 9
go_ahead = ' '
draw = 'draw'

def main():
    manual()
    pc, human = chips()
    queue = X
    field = new_field()
    show_field(field)
    while not winner(field):
        if queue == human:
            move = human_move(field, numan)
            field[move] = human
        else:
            move = pc_move(fieldc, pc, human)
            field[move] = pc
        show_field(field)
        queue = next_queue(queue)
    winner_player = winner(field)
    congrat_winner(winner_player, pc, human)

main()
input('\n Enter,')







