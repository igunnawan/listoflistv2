import ast

from moduleLoL import*
 
list_of_list = ast.literal_eval(input())

def jumlahkartu(kartu) :
    if IsEmpty(kartu) :
        return 0
    else :
        if IsAtom(FirstElmt(kartu)):
            print("element",FirstElmt(kartu))
            return 1 + (jumlahkartu(Tail(kartu)))
        else :
            return jumlahkartu(FirstElmt(kartu)) + jumlahkartu(Tail(kartu))

print(jumlahkartu(list_of_list))
        