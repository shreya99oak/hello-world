def count_vowels(x):
    """
    reutrn the number of vowels in x.
    count_vowels("shweta")
    2
    count_vowels("archana")
    3
    count_vowels('bug')
    1
    """
    number_vowels=0
    for char in x:
        if char in "aeiou":
            number_vowels+=1
     
    return number_vowels    
            
