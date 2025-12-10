'Spezifikation'
'Vor: S ist eine Liste aus Integern'
'Eff:'
'Erg: Ein Tupel bestehend aus entweder (x,y) mit x + y = k oder (-1, k) falls es keine x, y mit x + y = k gibt'

#Aufgabe 1a)
def twoSumList(S: list[int], k: int) -> tuple[int]:
  n = len(S)
  for i in range(0, n):
    for j in range(i+1, n):
      if S[i] + S[j] == k:
        return (S[i], S[j])
      else:
        continue
  return (-1, k)

#Tests 1a)
print('TwoSumList Tests: ',
      twoSumList([1,6,3,2],3),
      twoSumList([1,6,3,2],-5),
      twoSumList([],-5),
      #twoSumList(['a', 'b'], 3), #gibt aus, dass es nicht gefunden werden kann (-1, 3)
      twoSumList([1, 2, 3, 4], 0),
      twoSumList([0, 0, 0, 0], 0),
      twoSumList([1], 2), #hier wird (1, 1) zurückgegeben
      twoSumList([-1, -2], -3))

#Aufgabe 1b)
def twoSumSList(S: list, k: int) -> tuple[int]:
  klein = 0
  groß = len(S)-1 
  while klein < groß:
    if S[klein] + S[groß] == k:
      return (S[klein], S[groß])
    elif S[klein] + S[groß] < k:
      klein += 1
    else:             #S[klein] + S[groß] > k
      groß -= 1
  return (-1, k) 

#Tests 1b)
print('TwoSumSList Tests: ',
      twoSumList([1,6,3,2],3),
      twoSumList([1,6,3,2],-5),
      twoSumList([],-5),
      #twoSumList(['a', 'b'], 3), #gibt aus, dass es nicht gefunden werden kann (-1, 3)
      twoSumList([1, 2, 3, 4], 0),
      twoSumList([0, 0, 0, 0], 0),
      twoSumList([1], 2), #hier wird (-1, 2) zurückgegeben
      twoSumList([-1, -2], -3))

  
#Aufgabe 1c)
def twoSumSet(S: set, k: int) -> tuple[int]:
  for i in S:
    if k - i in S - {i}: #Damit man nicht i + i = k hat 
      return (i, k - i)
    else:
      continue
  return (-1, k)

#Tests 1c)
print('TwoSumSet Tests: ',
      twoSumSet({1,6,3,2},3),
      twoSumSet({1,6,3,2},-5),
      twoSumSet(set(),-5),
      twoSumSet({1, 2, 3, 4}, 0),
      twoSumSet({0, 0, 0, 0}, 0),
      twoSumSet({1}, 2), #hier wird (1, 1) zurückgegeben
      twoSumSet({-1, -2}, -3))


