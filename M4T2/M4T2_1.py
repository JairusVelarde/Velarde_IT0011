#define the sets
A = {'a','b','c','d','f','g'}
B = {'b','c','h','l','m','o'}
C = {'c','d','f','h','i','j','k'}

#elements in A and B

ab = A.intersection(B)
print("Elements in A and B: ", sorted(ab))
print("Count: ", len(ab))
print()

#element only in B
onlyB = B - (A.union(C))
print("Elements only in B: ", sorted(onlyB))
print("Count: ", len(onlyB))
print()

#HIJK
onlyHIJK = (C - A) | (C.intersection(B)-A)
print("Element: ", sorted(onlyHIJK))
print("Count: ", len(onlyHIJK))
print()

#CDF
onlyCDF = A.intersection(B).intersection(C)|{'d','f'}
print("Element:", sorted(onlyCDF))
print("Count: ", len(onlyCDF))
print()

#BCH
onlyBCH = B.intersection(C)|{'b'}
print("Element: ", onlyBCH)
print()

#DF
onlyDF = A.intersection(C) - {'c'}
print("Element:" ,sorted(onlyDF))
print()

#C
onlyC = A.intersection(B,C)
print("Common in All: ", onlyC)
print()

#LMO
onlyLMO = B - (A.union(C))
print("Only in B: ", sorted(onlyLMO))

