import ast
from moduleLoL import*

list_of_list = ast.literal_eval(input()) 

# def maximum(L) :
#     if IsEmpty(L) :
#         return 0
#     else :
#         return ((max(FirstElmt(L)) * 1000000) + maximum(Tail(L)))
    
def maximum(L) :
    if IsEmpty(L) :
        return 0
    if IsOneElmt(L) :
        if IsAtom(FirstElmt(L)) :
            print("elemen ke",L)
            return FirstElmt(L)*1000000
        else :
            # print("elemen ke",L)
            return maximum(FirstElmt(L))
    else :
        if IsAtom(FirstElmt(L)) :
            # print("elemen ke",L)
            return FirstElmt(max2(FirstElmt(L),max(Tail(L))))*1000000 + maximum(Tail(L))
        
        # elif IsList(FirstElmt(L)) :
        #     if IsAtom(FirstElmt(L)) :
        #         return FirstElmt(FirstElmt(L))*1000000 + maximum(Tail(L))
        else :
            return FirstElmt(max2(maximum(FirstElmt(L)),maximum(Tail(L))))*1000000 + maximum(Tail(L))
        
        # else :
        #     # print("elemen ke",FirstElmt(L))
        #     return (max2(maximum(FirstElmt(L)),maximum(Tail(L)))) + maximum(Tail(L))
    # else:
    #     return maximum(FirstElmt(L)) + maximum(Tail(L))
        
    # if isinstance(FirstElmt(L), int) :
        # if IsOneElmt(L) :
        #     print('pertama', L)
        #     if IsAtom(FirstElmt(L)) :
        #         return FirstElmt(L)
        #     else :
        #         return maximum(FirstElmt(L))
            
        # elif IsList(FirstElmt(L)) :
        #     print('kedua', FirstElmt(L))
        #     if IsAtom(FirstElmt(L)) :
        #         print("elemen ke satu",L)
        #         return max2(FirstElmt(L),maximum(Tail(L))) + maximum(Tail(L))
        #     else :
        #         print("elemen ke dua", FirstElmt(L))
        #         return max2(maximum(FirstElmt(L)),maximum(Tail(L))) + maximum(Tail(L))
        
        # else :
        #     print('ketiga', FirstElmt(L))
        #     if IsAtom(FirstElmt(L)) :
        #         return FirstElmt(L) + maximum(Tail(L))
        #     else :
        #         return maximum(FirstElmt(L)) + maximum(Tail(L))
              
        # else :
        #     if IsAtom(FirstElmt(L)) :
        #         return max2(FirstElmt(L),maximum(Tail(L))) + maximum(Tail(L))
        #     else :
        #         return maximum(FirstElmt(L)) + maximum(max2(Tail(L)))
    # else :
    #     return maximum(FirstElmt(L)) + maximum(Tail(L)) 
        

# def maxim(L) :
#     return max(FirstElmt(L)) + maxim(Tail(L))

# print(maxim(list_of_list))
print(maximum(list_of_list))