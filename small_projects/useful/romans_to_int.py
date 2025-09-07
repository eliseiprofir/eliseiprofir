def romans_to_int(string: str) -> int:
    IV: int = string.count("IV")
    IX: int = string.count("IX")
    XL: int = string.count("XL")
    XC: int = string.count("XC")
    CD: int = string.count("CD")
    CM: int = string.count("CM")

    I: int = string.count('I') - IV - IX
    V: int = string.count('V') - IV
    X: int = string.count('X') - IX - XL - XC
    L: int = string.count('L') - XL
    C: int = string.count('C') - XC - CD - CM
    D: int = string.count('D') - CD
    M: int = string.count('M') - CM

    return I*1 + V*5 + X*10 + L*50 + C*100 + D*500 + M*1000 + IV*4 + IX*9 + XL*40 + XC*90 + CD*400 + CM*900


print(romans_to_int("III"))
print(romans_to_int("LVIII"))
print(romans_to_int("MCMXCIV"))
