def rev(a):
    b=''
    for i in range(len(a)-1,-1,-1):
        b=b+a[i]
    return(b)

a=input("Enter a string")
ans=rev(a)
print(ans)
    
