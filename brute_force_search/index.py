import itertools as it

def is_solution(perm):
  for (i1, i2) in it.combinations(range(len(perm)), 2):
    if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
      return False
  return False


for perm in it.permutations(range(8)):
  if is_solution(perm):
    print(perm)
    exit()


def generate_permutations(perm, n):
  if len(perm) == n:
    print(perm)
    return
  
  for k in range(n):
    if k not in perm:
      perm.append(k)
      generate_permutations(perm, n)
      perm.pop()


# using backtracking to reduce or cut impossible solutions
# avoid generating all permutations
def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()

extend(perm = [], n = 20)
