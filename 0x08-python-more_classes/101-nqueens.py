#!/usr/bin/python3


from sys import argv


if __name__ == "__main__":
    my_list = []

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)

    num = int(argv[1])

    if num < 4:
        print("N must be at least 4")
        exit(1)

    for n in range(num):
        my_list.append([n, None])

    def exists(y):
        """ check that a queen does not already exist in that y value """
        for x in range(num):
            if y == my_list[x][1]:
                return (True)

        return (False)

    def reject_solution(x, y):
        """determines whether or not to reject the solution"""
        if (exists(y)):
            return (False)

        n = 0

        while (n < x):
            if abs(my_list[n][1] - y) == abs(n - x):
                return (False)

            n += 1

        return (True)

    def clear_mylist(x):
        """clears the answers from the point of failure on"""
        for n in range(x, num):
            my_list[n][1] = None

    def nqueens(x):
        """ recursive backtracking function to find the solution """
        for y in range(num):
            clear_mylist(x)

            if reject_solution(x, y):
                my_list[x][1] = y

                if (x == num - 1):
                    print(my_list)
                else:
                    nqueens(x + 1)

    nqueens(0)
