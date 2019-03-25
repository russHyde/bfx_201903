"""Script and functions to find the `longest increasing subsequence` in
a sequence (as defined at rosalind.info/problems/lgis).

Searches the working directory for a file called "data_LGIS.txt". The
data file should contain two lines - the first containing the length of
a sequence of integers and the second containing the sequence of
integers.

The integer sequence should consist of positive integers only
(repetitions are allowed).

Prints out both the longest increasing sequence, and the longest
decreasing sequence to stdout.
"""

def lgis(perm):
    """Obtain the longest increasing subsequence from a list of
    positive integers

    Args:
        perm (list(int)): A list of integers within which the longest
        increasing subsequence is to be found.

    Returns: A list of integers, a subsequence of the input list of
        integers.
    """
    #
    levels = []
    graph = {}
    for i in perm:
        if not levels:
            levels.append([i])
            graph[i] = 0
        else:
            # append to the highest level where i is greater than some
            # value in the next lowest level
            for lev in reversed(range(len(levels) + 1)):
                if i in graph.keys():
                    break
                if lev == 0:
                    levels[0].append(i)
                    graph[i] = 0
                    break
                lower_lev = levels[lev - 1]
                parents = [x for x in lower_lev if x < i]
                if parents:
                    if len(levels) == lev:
                        levels.append([i])
                    else:
                        levels[lev].append(i)
                        # drop entries in this level if they are greater than i
                        lev_gt = [x for x in levels[lev] if x > i]
                        levels[lev] = list(set(levels[lev]).difference(set(lev_gt)))
                    graph[i] = parents[0]
    # returnable data
    res = []
    i = levels[-1][0]
    while i != 0:
        res.append(i)
        i = graph[i]
    res = list(reversed(res))
    return res


if __name__ == "__main__":
    # This block only runs when this file is called as a script ...
    STREAM = open("data_LGIS.txt", "r").read().splitlines()
    MAXNUM = int(STREAM[0])
    PERM = [int(x) for x in STREAM[1].split()]
    print(" ".join([str(x) for x in lgis(PERM)]))
    print(" ".join(list(reversed([str(x) for x in lgis(list(reversed(PERM)))]))))
