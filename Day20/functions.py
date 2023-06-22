def CalculateGmean(a, b):
    mean = (a*b)/(a+b)
    print("Using function ",mean)

def isGreater(a, b):
    if(a>b):
        print("First is Greater")
    elif(a<b):
        print("Second is Greater")
    else:
        print("Both equal")

def isLesser(a,b):
    pass
# pass is to stop half function to execute
# so no error accur

def function(a,b):
    CalculateGmean(a,b)
    isGreater(a,b)

a=9
b=8
gmean = (a*b)/(a+b)
print(gmean)
# CalculateGmean(a,b)
# isGreater(a,b)
function(a,b)

c=8
d=12
gmean1 = (c*d)/(c+d)
print(gmean1)
# CalculateGmean(c,d)
# isGreater(c,d)
function(c,d)