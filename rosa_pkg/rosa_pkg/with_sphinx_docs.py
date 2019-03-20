"""
Script to compute the `longest increasing subsequence`
"""


def lgis(perm):
    """
    Obtain the longest increasing subsequence from a list of integers

    :param perm: A list of integers within which the longest increasing
    subsequence is to be found.
    :type perm: List of integers
    """
    #
    if not perm:
        return []

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
    # Only runs when rosa/testable.py is called as a script ...
    STREAM = open("data_LGIS.txt", "r").read().splitlines()
    MAXNUM = int(STREAM[0])
    PERM = [int(x) for x in STREAM[1].split()]
    print(" ".join([str(x) for x in lgis(PERM)]))
    print(" ".join(list(reversed([str(x) for x in lgis(list(reversed(PERM)))]))))
