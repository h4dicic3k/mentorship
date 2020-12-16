
def fakt(n):
    if n>=0:
        if (n==1 or n==0):
            return 1
        else:
            return n*fakt(n-1)
    else:
        return "Lütfen negatif sayı girmeyiniz!"
a = int(input("Faktöryel hesaplaması için bir sayı gir: "))
print(fakt(a))