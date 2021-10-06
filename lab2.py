'''
Determina daca un numar este prim
:param x: numar intreg
:return: True, daca x este prim sau False in caz contrar
'''

def isPrime(x):
    if x<2:
        return False
    if x == 2:
        return True
    if x % 2 ==0:
        return False
    for i in range (3, x//2+1, 2):
        if x % i == 0:
            return False
    return True

'''
Gaseste ultimul numar prim mai mic decat numarul dat
:param x: numar natural
:return: numarul cu proprietatea ceruta
'''
def get_largest_prime_below(n):
    gasit = False
    n = n - 1
    while gasit == False:
        if isPrime(n)== True:
            return n
        else:
            n = n - 1


'''
Functia test
'''

def test_get_largest_prime_below():
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(9) == 7

'''
Determina varsta unei persoane in zile
:param: birthday - string 
:return: varsta in zile
'''

'''
Functie test
'''

def get_age_in_days(birthday):
    calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = int (birthday[0:2])
    month = int (birthday [3:5])
    year = int (birthday [6:10])
    total = calendar[month] - day
    for i in range (month + 1 , 13):
        total = total + calendar[i]
    aniTotal = 2021 - year -1
    total = total + aniTotal * 365
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month <= 2:
            total = total +1   # am verificat daca anul nasterii a fost bisect
    for i in range (year + 1, 2021):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            total = total + 1 #am adaugat anii bisecti
    # consideram data curenta 5 octombrie 2021
    for i in range (1, 10):
        total = total + calendar [i]
    total = total + 5

    return total

def test_get_age_in_days():
    assert get_age_in_days("09/06/2003") == 6693
    assert get_age_in_days("09/01/2000") == 7940
    assert get_age_in_days("31/10/2002") == 6914
    assert get_age_in_days("01/10/2021") == 4
    assert get_age_in_days("29/02/2004") == 6428

#Am ales problema 5
def is_palindrome(n):
    '''
    Determina daca un numar este palindrom
    :param n: numar intreg
    :return: True, daca n este palindrom, False, in caz contrar
    '''
    ncopy = n
    palindrom = 0
    while ncopy:
        palindrom = palindrom * 10 + ncopy %10
        ncopy = ncopy // 10
    if palindrom == n:
        return True
    else:
        return False

def test_is_palindrome():
    '''
    Functia test
    '''
    assert is_palindrome(123) == False
    assert is_palindrome(123585321) == True
    assert is_palindrome(45846) == False
    assert is_palindrome(5) == True


def main():
    test_get_age_in_days()
    test_get_largest_prime_below()
    test_is_palindrome()
    shouldRun = True
    while shouldRun:
        print("1. Determinati ultimul numar prim mai mic decat un numar dat")
        print("2. Determinati varsta unei persoane in zile")
        print("5.Determinati daca un numar dat este palindrom")
        print("x. Oprire program")

        optiune = input("Alegeti optiunea ")
        if optiune == "1":
            n = int(input("Introduceti numarul "))
            if n > 2:
                print(get_largest_prime_below(n))
            else:
                print("Nu exista")
        elif optiune =="2":
            dataNasterii = input("Introduceti data nasterii DD/MM/YYYY: ")
            print(get_age_in_days(dataNasterii))
        elif optiune == "5":
            numar = int (input ("Introduceti numarul "))
            if is_palindrome(numar) == True:
                print("Numarul dat este palindrom")
            else:
                print("Numarul dat nu este palindrom")
        elif optiune == "x":
            shouldRun = False
        else:
            print("Optiune inexistenta. Reincercati!")



if __name__ == '__main__':
    main()
