def calculate_levenshtein_distance(source, target):
  source = "#" + source
  target = "#" + target

  M = len(source)
  N = len(target)

  D = [[0] * N for _ in range(M)]

  for i in range(N):
    D[0][i] = i
  for j in range(1, M):
    D[j][0] = j

  for r in range(1, M):
    for c in range(1, N):
      cost_1 = D[r-1][c] + 1
      cost_2 = D[r][c-1] + 1
      sub_cost = 1 if source[r] != target[c] else 0
      cost_3 = D[r-1][c-1] + sub_cost
      D[r][c] = min(cost_1, cost_2, cost_3)

  return D[-1][-1]
