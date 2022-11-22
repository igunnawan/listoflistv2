import ast
from moduleLoL import*

list_of_list = ast.literal_eval(input())
inputan = input()

def hindarimonster(A,S) :
    if IsEmpty(S):
        # print("element ke",S)
        return S
    elif IsList(FirstElmt(S)):
        # print("element ke",S)
        return KonsLo(hindarimonster(A,FirstElmt(S)),hindarimonster(A,Tail(S)))
    else:
        if A == '' or FirstElmt(S) % int(A) == 0:
            print("element ke",S)
            return hindarimonster(A,Tail(S))
        else:
            print("element ke",S)
            return KonsLo(FirstElmt(S),hindarimonster(A,Tail(S)))

print(hindarimonster(inputan,list_of_list))