import src.simplefuncs as smfc

if __name__ == '__main__':
    idx1_start = 4
    idx2_start = 4

    board = smfc.minimal_knight_movements(idx1_start=idx1_start, idx2_start=idx2_start)
    smfc.print_as_matrix(board)

    print("***")

    move_counter = smfc.hanoi_tower_moves(disk_count=3)
    print("Needed moves: " + str(move_counter))
