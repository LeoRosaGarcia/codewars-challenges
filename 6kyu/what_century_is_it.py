"""
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
"""
import math as m

def suffix(i):
    return {1:"st", 2:"nd", 3:"rd"}.get(i%10*(i%100 not in [11,12,13]), "th")

def what_century(year):
    cen = int(year)/100 
    print(cen)
    if str(cen)[-1] == "0":
        return f"{m.floor(cen)}{suffix(cen)}"
    else:
        return f"{m.floor(cen)+1}{suffix(cen)}"

print(what_century('2259'))