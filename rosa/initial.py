stream = open('data_LGIS.txt', 'r').read().splitlines()

maxnum = int(stream[0])
perm   = [int(x) for x in stream[1].split()]

def lgis(maxnum, perm):
  #
  levels = []
  graph  = {}
  for i in perm:
    if len(levels) == 0:
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
        lower_lev = levels[lev-1]
        lt = [x for x in lower_lev if x < i]
        if len(lt) > 0:
          if len(levels) == lev:
            levels.append([i])
          else:
            levels[lev].append(i)
            # drop entries in this level if they are greater than i
            lev_gt = [x for x in levels[lev] if x > i]
            levels[lev] = list(set(levels[lev]).difference(set(lev_gt)))
          graph[i] = lt[0]
  # returnable data
  res = []
  i = levels[-1][0]
  while(i != 0):
    res.append(i)
    i = graph[i]
  res = list(reversed(res))
  return res

print(" ".join([str(x) for x in lgis(maxnum, perm)]))
print(" ".join(
  list(reversed([str(x) for x in lgis(maxnum, list(reversed(perm)))]))))