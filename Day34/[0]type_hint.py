age : int   #This is adding hint for clear documentation

#But if you assign string to age it dosent break code because python is dynamically typed

def over_eighteen(age : int) -> bool:  #This is hinting that the function accepts age as int
                                       #and return type is bool but it dosent enforce it
    if age >= 18:
        return True
    else:
        return False

print(over_eighteen(18))

