import itertools

if __name__ == "__main__":
    perms = [x for x in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
    print(len(perms))
    sol = 0
    for perm in perms:
        if perm[0] + perm[1] == perm[5] + perm[6] \
                and perm[1] + perm[2] == perm[6] + perm[7] \
                and perm[2] + perm[3] == perm[7] + perm[8] \
                and perm[3] + perm[4] == perm[8] + perm[9] \
                and perm[9] + perm[0] == perm[4] + perm[5]:
            sol += 1
            print('Solution: {s} = {p}'.format(s=sol, p=perm))
