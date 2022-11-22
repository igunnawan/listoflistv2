import ast
from moduleLoL import*

list_of_list = ast.literal_eval(input())

def IsPrima(n, i = 2) :
    if isinstance(n,int) :
        if (n < 2) :
            return False
        elif (n == 2) :
            return True
        elif (n % i == 0) :
            return False
        elif (i * i > n) :
            return True
        else :
            return IsPrima(n, i+1)

def prima(L) :
    if IsEmpty(L) :
        return 0
    else :
        if isinstance(FirstElmt(L),int) :
            if not (IsPrima(FirstElmt(L))) :
                return prima(Tail(L))
            else :
                return FirstElmt(FirstElmt(L)) + prima(Tail(L))
        else :
            return prima(FirstElmt(L)) + prima(Tail(L))
            
            
print(prima(list_of_list))
# print(IsPrima(5))