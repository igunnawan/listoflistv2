def KonsLo(L,S):
    return [L] + S
    
def KonsL(S,L):
    return S + [L]
    
def FirstElmt(L):
    if isinstance(L,list) :
        return L[0]
    else :
        return L
   
def Tail(L):
    if not(IsEmpty(L)) :
        return L[1:]
       
def Head(L):
    if not(IsEmpty(L)) :
        return L[:-1]
        
def LastElmt(L):
    if isinstance(L,list) :
        return L[0]
    else :
        return L

def IsEmpty(L):
    return L==[]

def IsAtom(e):
    return not(IsEmpty(e)) and Jumlah(e) == 1

def IsList(e):
    if not(IsAtom(e)) :
        return True
    else :
        return False
    
def IsOneElmt(L) :
    if not(IsEmpty(L)) :
        return NbElmt(L) == 1
    else :
        return False
        
def IsMember(X,L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L)==X:
        return True
    else:
        return IsMember(X,Tail(L))
    
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        print(L)
        return 1 + NbElmt(Tail(L))
    
def Jumlah(L):
    if isinstance(L,int) :
        return len([L])
    else :
        return len(L)

def IsEqS(S1,S2):
    if (IsEmpty(S1) and IsEmpty(S2)):
        return True
    elif (not IsEmpty(S1) and IsEmpty(S2)):
        return False
    elif (IsEmpty(S1) and not IsEmpty(S2)):
        return False
    else :
        if (IsAtom(FirstElmt(S1))) and (IsAtom(FirstElmt(S2))):
            return (FirstElmt(S1) == FirstElmt(S2) and IsEqS(Tail(S1),Tail(S2)))
        elif (IsList(FirstElmt(S1)) and IsList(FirstElmt(S2))):
            return IsEqS(FirstElmt(S1),FirstElmt(S2)) and IsEqS(Tail(S1),Tail(S2))
        else:
            return False
        
def IsEqual(L1,L2):
    if (IsEmpty(L1) and IsEmpty(L2)):
        return True
    elif (not IsEmpty(L1) and IsEmpty(L2)):
        return False
    elif (IsEmpty(L1) and not IsEmpty(L2)):
        return False
    elif (not IsEmpty(L1) and not IsEmpty(L2)):
        return (FirstElmt(L1) == FirstElmt(L2)) and IsEqual(Tail(L1),Tail(L2))

def IsMemberS(A,S):
    if (IsEmpty(S)):
        return False
    elif (not IsEmpty(S)):
        if (IsAtom(S)):
            return (A == FirstElmt(S)) or (IsMemberS(A,Tail(S)))
        elif (IsList(S)):
            return (IsMember(A,FirstElmt(S))) or (IsMemberS(A,Tail(S)))

def IsMemberLS(L,S):
    if (IsEmpty(L) and IsEmpty(S)):
        return True
    elif (not IsEmpty(L) and IsEmpty(S)):
        return False
    elif (IsEmpty(L) and not IsEmpty(S)):
        return False
    elif (not IsEmpty(L) and not IsEmpty(S)):
        if (IsAtom(FirstElmt(S))):
            return IsMemberLS(L,Tail(S))
        else:
            if (IsEqual(L,FirstElmt(S))):
                return True
            else:
                return IsMemberLS(L,Tail(S))

def RemberL(A,S):
    if IsEmpty(S):
        return S
    elif IsList(FirstElmt(S)):
        return KonsLo(RemberL(A,FirstElmt(S)),RemberL(A,Tail(S)))
    else:
        if FirstElmt(S) % A == 0:
            return RemberL(A,Tail(S))
        else:
            return KonsLo(FirstElmt(S),RemberL(A,Tail(S)))
        
def max2(a,b) :
    if a >= b :
        return a
    else :
        return b

def max(s) :
    if IsOneElmt(s) :
        if IsAtom(FirstElmt(s)) :
            print("1. elemen ke", s)
            return FirstElmt(s)
        else :
            print("2. elemen ke", s)
            return max(FirstElmt(s))
    else :
        if IsAtom(FirstElmt(s)) :
            print("3. elemen ke", s)
            return max2(FirstElmt(s),max(Tail(s)))
        else :
            print("4. elemen ke", s)
            return max2(max(FirstElmt(s)), max(Tail(s)))
            
    
# print(IsMemberS(1,Matrix1))
x = [1,2,3,4,[6,7]]
z = [[2,3,4,6,7],[1,1,3,2,7],[5,2,1],[4,4,6],[3,3]]
# y = [[2,3,4],[5,6,8,[1,2,3]],[4,5,10],[10,10,8]]
e = [0,1,2,3,4,5,6,7,8,9]
# print(NbElmt(x))

# print(FirstElmt(x))
# print(max(z))
print(NbElmt(e))
# print(RemberL(2,y))
