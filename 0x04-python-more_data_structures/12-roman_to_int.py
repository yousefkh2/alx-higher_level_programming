#!/usr/bin/python3
def roman_to_int(roman_string):
    """Roman to Int

    Args:
        roman_string: the roman string

    Returns:
        the arabic numeral or 0 if the string is invalid
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_to_arabic = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    
    i, total = 0, 0
    while i < len(roman_string):
        # Try to match two character strings first, then one character
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_to_arabic:
            total += roman_to_arabic[roman_string[i:i+2]]
            i += 2
        elif roman_string[i] in roman_to_arabic:
            total += roman_to_arabic[roman_string[i]]
            i += 1
        else:
            return 0    # invalid roman numeral
    return total
