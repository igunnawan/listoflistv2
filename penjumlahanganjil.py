import ast
from moduleLoL import*

list_of_list = ast.literal_eval(input())

def ganjil(L) :
    if IsEmpty(L) :
        return 0
    else :
        if isinstance(FirstElmt(L),int) :
            if (FirstElmt(L) % 2) == 0:
                return ganjil(Tail(L))
            else:
                return FirstElmt(FirstElmt(L)) + ganjil(Tail(L))
        else :
            return ganjil(FirstElmt(L)) + ganjil(Tail(L))


# list_of_list = [1,[5,2,3],10,9,[7],[3,3]]

print(ganjil(list_of_list))