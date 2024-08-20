#Question 1
#La fonction va prendre en paramètre un dictionnaire et un string (chaine)
#et va retourner la traduction en anglais ou en francais de la chaine à partir du dictionnaire fourni
#Contrat type : (dict,string) => string
def transl(d,s):
    for motAnglais,motFrancais in d.items():
        if(motAnglais == s):
            s = motFrancais
            return s
        elif(motFrancais == s):
            s = motAnglais
            return s
        elif(s not in d.values() and s not in d.keys()):
            s = "Unknown"
            return s  




d = {"apple":"pomme", "banana":"banane", "pear": "poire", "plum":"prune"}

s = "pear"
print(transl(d,s))
s = "poire"
print(transl(d,s))
s = "appricot"
print(transl(d,s))


#Question 2
#La fonction va prendre en paramètre deux listes et
#va retourner tous l ensemble (set) de tous les elements des deux listes sans repetitions
#Contrat type: (list,list) => set
def setOp(list1,list2):
    Monset = set(list1 + list2)
    return Monset
    
Monset1 = setOp([1,2,2,3],[2,-6,8,7])
print(Monset1)
Monset2 = setOp([],[1,4,2,4,6])
print(Monset2)
Monset3 = setOp([1,1,1,1],[])
print(Monset3)
Monset4 = setOp([1],[2,3,2,2])
print(Monset4)

#Question 3
#La fonction va prendre en paramètre une matrice et va retourner le maximum
#et le minimum de cette dernière sous forme de tuple
#Contrat type: (list[list]) => tuple
def matrixMinMax(m):
    maximum = m[0][0]
    minimum = m[0][0]
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            if(maximum < m[i][j]):
                maximum = m[i][j]
            if(minimum > m[i][j]):
                minimum = m[i][j]
                
    
    return (minimum,maximum)

print(matrixMinMax([[1,5],[2,8]]
))
print(matrixMinMax([[1,5,10],[2,8,-1]]))
print(matrixMinMax([[2,8,-1]]))
print(matrixMinMax([[1],[1]]))
