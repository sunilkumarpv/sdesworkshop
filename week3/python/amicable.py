def aliquot(n):
  alq = 0
  for i in range(1,n/2 + 1):
    if n % i == 0:
      alq = alq + i
  return(alq)

def ami(a,b):
  if aliquot(a) == b and aliquot(b) == a:
    return True
  else:
    return False
def amicable():
  l = []
  for i in range(200,300):
    for j in range(200,300):
      if ami(j,i) == True:
	if ami(i,j) == True:
	  if [i,j] in l == False and [i,j].reverse() in l == False 
            l.append[i,j]
  print l 
	  

    
