def findmissingno(x):
  numbers=set(x)
  length=len(x)
  out=[]
  for i in range (1,x[-1]):
    if i not in numbers:
      out.append(i)
  return out
L=eval(input('enter the list:'))
IN=findmissingno(L)
print('Missing number:',IN)
