txt =str(input())
def rs(txt):
  transTable = txt.maketrans("aeiouAEIOU", "eiouaEIOUA", "xyz")
  txt = txt.translate(transTable)
  print(txt)
  
rs(txt)