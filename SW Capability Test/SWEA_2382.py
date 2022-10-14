def init():
    n, m, k = tuple(map(int, input().split()))
    input_grid = [
        [list() for _ in range(n)]
        for _ in range(n)
    ]
    for _ in range(k):
        r, c, microbe_cnt, move_dir = tuple(map(int, input().split()))
        input_grid[r][c].append((microbe_cnt, move_dir - 1))
    return n, m, k, input_grid


def initialize_grid():
    for i in range(N):
        for j in range(N):
            grid[i][j] = list()


def initialize_next_grid():
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = list()


def is_in_red(r, c):
    return r == 0 or r == N - 1 or c == 0 or c == N - 1


def change_dir(move_dir):
    if move_dir == 0:
        return 1
    elif move_dir == 1:
        return 0
    elif move_dir == 2:
        return 3
    elif move_dir == 3:
        return 2


def move_microbe(r, c, microbe_cnt, move_dir):
    drs = [-1, 1, 0, 0]
    dcs = [0, 0, -1, 1]

    next_r, next_c = r + drs[move_dir], c + dcs[move_dir]
    if is_in_red(next_r, next_c):
        move_dir = change_dir(move_dir)
        microbe_cnt = microbe_cnt // 2

    if microbe_cnt != 0:
        next_grid[next_r][next_c].append((microbe_cnt, move_dir))


def move():
    initialize_next_grid()

    for i in range(N):
        for j in range(N):
            for microbe in grid[i][j]:
                microbe_cnt, move_dir = microbe
                move_microbe(i, j, microbe_cnt, move_dir)


def combine():
    initialize_grid()

    for i in range(N):
        for j in range(N):
            if len(next_grid[i][j]) >= 1:
                next_grid[i][j].sort(key=lambda x: -x[0])
                final_microbe_cnt = 0
                for idx, element in enumerate(next_grid[i][j]):
                    microbe_cnt, move_dir = element
                    if idx == 0:
                        final_move_dir = move_dir
                    final_microbe_cnt += microbe_cnt
                grid[i][j].append((final_microbe_cnt, final_move_dir))


def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()
    print()


def print_next_grid():
    for i in range(N):
        for j in range(N):
            print(next_grid[i][j], end=" ")
        print()
    print()


def pro():
    for t in range(1, time + 1):
        # print("turn", t)
        move()
        # print_next_grid()
        combine()
        # print_grid()


def get_answer():
    answer = 0
    for i in range(N):
        for j in range(N):
            for microbe_cnt, move_dir in grid[i][j]:
                answer += microbe_cnt

    return answer


T = int(input())
for test_case in range(1, T + 1):
    N, time, K, grid = init()
    next_grid = [
        [list() for _ in range(N)]
        for _ in range(N)
    ]
    pro()
    print(f'#{test_case} {get_answer()}')

'''
1
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1
'''
'''
10
7 2 9
1 1 7 1
2 1 7 1
5 1 5 4
3 2 8 4
4 3 14 1
3 4 3 3
1 5 8 2
3 5 100 1
5 5 1 1
10 17 46
7 5 724 2
7 7 464 3
2 2 827 2
2 4 942 4
4 5 604 4
7 2 382 1
6 5 895 3
8 7 538 4
6 1 299 4
4 7 811 4
3 6 664 2
6 8 868 2
7 6 859 2
4 6 778 2
5 4 842 3
1 3 942 1
1 1 805 3
3 2 350 3
2 5 623 2
5 3 840 1
7 1 308 4
1 8 323 3
2 3 82 3
2 6 115 2
8 3 930 1
6 2 72 1
2 1 290 3
4 8 574 4
8 5 150 3
8 2 287 2
2 8 909 2
2 7 588 2
7 3 30 3
5 8 655 3
3 8 537 1
4 2 350 3
5 6 199 1
5 5 734 2
3 3 788 1
8 4 893 1
1 4 421 4
6 3 616 2
1 2 556 4
7 8 8 1
5 2 702 2
4 4 503 3
10 5 28
3 3 796 1
7 2 798 2
2 6 622 1
3 5 179 3
7 8 888 4
5 8 634 3
1 8 646 1
3 7 433 4
6 7 416 1
2 7 651 3
6 4 476 2
5 6 712 4
1 7 869 4
6 1 789 2
8 8 585 3
7 6 426 1
1 5 154 2
1 2 692 1
2 4 549 3
2 1 60 2
4 8 996 4
8 2 437 2
3 6 195 2
1 3 734 4
3 8 355 2
1 1 945 1
2 5 558 2
7 7 144 2
10 22 26
2 2 450 4
6 3 659 1
5 8 24 2
3 7 649 2
3 2 22 3
1 3 905 4
7 8 625 3
6 7 824 3
7 3 159 1
2 7 297 4
7 2 270 2
4 5 985 1
7 1 627 2
3 4 625 4
8 5 972 4
6 6 432 4
6 8 142 1
7 7 900 1
4 1 974 2
4 2 760 4
1 4 550 2
5 7 624 4
4 6 694 1
4 3 593 3
3 1 152 4
1 8 926 1
10 7 15
3 4 227 1
4 7 109 1
3 7 487 2
2 3 627 2
6 1 520 4
7 3 596 4
2 6 525 4
1 5 116 3
7 7 771 4
4 4 520 2
7 5 763 1
5 4 829 3
5 2 578 3
6 8 200 2
3 8 760 4
10 24 12
6 5 887 2
2 3 428 1
2 1 540 2
8 1 356 4
1 7 485 4
5 1 357 3
7 6 271 2
6 2 22 1
6 1 41 2
8 2 565 2
8 5 855 1
6 3 734 1
10 22 44
2 2 963 1
8 4 635 4
4 1 938 4
8 7 511 3
6 8 825 4
6 7 934 3
3 7 701 4
2 7 534 2
5 2 705 1
3 5 300 2
6 2 855 4
7 7 877 4
1 7 443 1
1 2 313 1
3 3 932 2
1 8 831 2
1 1 90 2
2 6 145 3
2 3 740 4
5 3 759 4
1 6 181 1
8 6 608 4
5 6 556 2
2 4 541 4
2 1 174 2
6 1 601 1
7 5 84 4
4 3 970 3
8 8 503 1
3 4 171 3
5 7 913 4
8 1 232 3
7 6 539 4
3 8 648 1
8 2 944 2
2 5 508 2
5 1 87 1
5 8 88 4
2 8 681 2
1 5 758 2
3 1 690 3
6 4 620 3
5 4 783 1
6 6 748 1
10 9 38
2 7 955 1
7 7 25 4
4 2 496 2
1 4 342 1
7 5 72 1
3 7 429 2
5 2 812 3
8 6 36 2
1 6 994 3
1 5 838 1
3 4 131 4
7 2 11 2
6 3 650 3
7 3 353 2
1 7 454 2
8 3 256 4
5 5 213 2
6 5 80 1
2 1 676 4
4 6 561 3
2 5 653 3
3 5 923 3
8 2 259 3
4 4 781 2
1 1 313 2
3 6 938 3
2 6 700 3
4 1 215 2
4 8 39 3
5 1 954 3
6 7 774 1
5 8 541 4
3 1 885 4
7 8 867 2
2 8 825 1
5 6 598 3
6 6 80 3
8 1 405 2
10 16 11
5 7 87 3
2 5 686 1
6 7 64 2
6 8 873 3
5 6 762 2
8 4 268 3
7 3 307 4
1 7 809 3
5 5 293 3
5 1 345 3
4 1 114 4
10 8 19
3 1 52 4
6 8 423 3
7 3 498 4
7 5 633 3
7 7 392 3
6 6 458 4
3 8 830 3
5 1 799 3
1 1 540 3
4 8 567 3
1 6 897 3
5 4 230 1
2 6 229 3
1 5 147 1
4 1 754 2
3 3 569 1
7 8 515 4
2 4 528 4
2 1 962 2
'''
