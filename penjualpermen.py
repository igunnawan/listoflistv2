import ast
from moduleLoL import*

list_of_list = ast.literal_eval(input())

def penjumlahanlist(L) :
    if IsEmpty(L) :
        return 0
    else :
        if IsAtom(FirstElmt(L)) :
            return FirstElmt(L) + penjumlahanlist(Tail(L))
        else :
            return penjumlahanlist(FirstElmt(L)) + penjumlahanlist(Tail(L))

def penjualpermen(L) :
    if IsEmpty(L) :
        return 0
    else :
        if isinstance(FirstElmt(L),int) :
            if FirstElmt(L) % 2 == 0 :
                # print("elemen ke", L)
                return (FirstElmt(L))*4000 + penjualpermen(Tail(L))
            else :
                # print("elemen ke", L)
                return (FirstElmt(L))*3000 + penjualpermen(Tail(L))
        else :
            if penjumlahanlist(FirstElmt(L)) % 2 == 0 :
                # print("elemen ke", L)
                return penjumlahanlist(FirstElmt(L))*2000 + penjualpermen(Tail(L))
            elif penjumlahanlist(FirstElmt(L)) % 2 != 0 :
                # print("elemen ke", L)
                return penjumlahanlist(FirstElmt(L))*1000 + penjualpermen(Tail(L))

# def penjualpermen(L) :
#     if IsEmpty(L) :
#         return 0
#     else :
#         if isinstance(FirstElmt(L),int) :
#             if IsAtom(FirstElmt(L)) :
#                 return atomisasi(L) + penjualpermen(Tail(L))
#             elif IsList(FirstElmt(L)) :
#                 return listan(L) + penjualpermen(Tail(L))
#             else :
#                 return penjualpermen(FirstElmt(L)) + penjualpermen(Tail(L))
#         else :
#             return penjualpermen(FirstElmt(L)) + penjualpermen(Tail(L))
            
# def atomisasi(L) :
#     if FirstElmt(L) % 2 == 0 :
#         return FirstElmt(L)*4000
#     else :
#         return FirstElmt(L)*3000

# def listan(L) :
#     if penjumlahanlist(L) % 2 == 0 :
#         return penjumlahanlist(L)*2000
#     else :
#         return penjumlahanlist(L)*1000
    

x = [1,2,3,[4,5]]
y = [2,3,[1,4],[2,2],9]
print(penjualpermen(list_of_list))

# print(penjumlahanlist(x))