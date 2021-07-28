def recur_fibo(n):
  if n<=1:
    return n
  else:
    return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=20
if nterms<=0:
  print("please enter a positive number")
else:
  print("fibonnaci sequence:")
  for i in range(nterms):
    print(reccur_fibo(i))
