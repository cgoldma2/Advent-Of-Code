#!/usr/bin/env python3

import sys


def mark_num(boards, number):
    for board in range(len(boards)):
        for row in range(5):
            for col in range(5):
                if boards[board][row][col] == number:
                    boards[board][row][col] = None
                    boards[board][row][5] += 1
                    boards[board][5][col] += 1
    return boards

def check_win(boards, wins):
    winners = []
    for board in range(len(boards)):
        for pos in range(5):
            if boards[board][pos][5] == 5 or boards[board][5][pos] == 5:
                if board not in wins:
                    winners.append(board)
    return winners

def calc_num(board, number):
    board = board[0:5]
    s = 0
    for row in board:
        new_row = []
        for n in row[0:5]:
            if n:
                s += n
    return s*number

def main():
    numbers = list(map(int,sys.stdin.readline().split(",")))

    boards = []
    board = 0
    while _ := sys.stdin.readline():
        boards.append([])
        for _ in range(5):
            boards[board].append(list(map(int,sys.stdin.readline().split())) + [0])
        boards[board].append([0]*6)
        board += 1

    wins = set()

    for number in numbers:
        boards = mark_num(boards, number)
        winners = check_win(boards, wins)
        for winner in winners:
            wins.add(winner)
        if len(wins) == board:
            print(calc_num(boards[winners[0]], number))
            break


if __name__ == "__main__":
    main()

