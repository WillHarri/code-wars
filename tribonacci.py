def tribonacci(signature, n):
    res = []
    res = res + signature
    for i in range(n-3):
        res.append(res[-1] + res[-2] + res[-3])
    return res[:n]


tribonacci([0, 0, 1], 10)

#Other solution
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
