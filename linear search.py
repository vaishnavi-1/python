
pos = -1

def search(list,n):
    i=0
    for i in range(6):
        i<len(list)
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1;

    return False

list=[5,9,122,90,45,6]
n=6

if search(list,n):
    print("found at",pos)
else:
    print("not found")
