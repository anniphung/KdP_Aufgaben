linsenUnsortiert = ['s','s','g','s','g','g','g']

'''
Pre: Liste "unsortiert" besteht auschließlich aus den Elementen 'g' und 's'
Effekt: keiner
Ergebnis: Eine neue Liste, in welcher Kopien der Elemente von "unsortiert" alphabetisch sortiert wurden
'''


def linsenSortieren(unsortiert: list[str]) -> list[str]:
  sortiert = [linse for linse in unsortiert if linse == 'g']+[linse for linse in unsortiert if linse == 's']
  return sortiert 

linsenSortiert = linsenSortieren(linsenUnsortiert)

'''def linsenSortieren(unsortiert: list) -> list:
  sortiert = []
  guteLinsen = 0
  for linse in unsortiert:
    if linse == 'g':
      guteLinsen += 1
  i = 0
  while i < len(unsortiert):
    if i < guteLinsen:
      sortiert.append('g')
    else:
      sortiert.append('s')
  return sortiert '''