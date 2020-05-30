
fname=input("enter file")
if len(fname)<1:
    fname='mydata'
hand=open(fname)

for lin in hand:
    lin=lin.rstrip
    print(lin.read())
