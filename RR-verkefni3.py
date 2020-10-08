from time import time

# Dæmi 1
# A) Algrím sem þarf að fara í gegnum lista einu sinni t.d. min eða max föllin
# B) Algrím sem hafa lykkju inn í lykkju t.d. bubblesort
# C) Algrím sem getur sparað sér tíma


# Dæmi 2
"""
def bubbleSort(listi):
    for num in range(len(listi)-1,0,-1):
        for i in range(num):
            if listi[i]>listi[i+1]:
                temp = listi[i]
                listi[i] = listi[i+1]
                listi[i+1] = temp

mill = list(range(1,10000))
mill.reverse()
mill2 = list(range(1,10000))
mill2.reverse()

t0 = time()
bubbleSort(mill)
t1 = time()
mill2.sort()
t2 = time()
"""
#print("Mitt reiknirit:", t1 - t0, "sek")
#print("list.sort():", t2 - t1, "sek")

#Mitt fall hefur flækjustigið O(n^2)
#Samkvæmt mínum rannsóknum notar innbyggða fallið Timsort sem hefur flækjustigið O(n log n)


#Dæmi 3 --------------EKKI Búið



def stafrof(string):
    array = list(string)
    if not array:
        return []

    p, *xs = array
    lesser = [x for x in xs if p>x]
    greater = [x for x in xs if p<=x]

    return stafrof(lesser) + [p] + stafrof(greater)
#Reyndi í 3 tíma og gat ekki náð að breyta aftur í streng
#Það kom alltaf "TypeError: can only concatenate list (not "str") to list"
#á endanum gafst ég upp og sætti mig við að þetta skilar lista

strengur = "dcab"
print(stafrof(strengur))


#Dæmi 4
# A) fyrsta for lykkjan telur hvað hver tala kemur oft fyrir og setur það í countL
# næsta lykkja plúsar saman tölurnar í countL
# síðasta lykkjan notar countL til að raða listanum rétt
# B) Countingsort
# C) O(n+k)


#Dæmi 5
"""
def insert(listi, n): 
    for i in range(len(listi)): 
        if listi[i] > n:
            index = i 
            break
    listi = listi[:i] + [n] + listi[i:]
    print(listi) 
    return listi
# flækjustig er O(n) í versta tilviki
listi = [2,3,3,5,6,7,9,10]
n = 9
insert(listi, n)
"""
