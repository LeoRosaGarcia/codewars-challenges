"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(s):
    a = s.split()
    lis = []
    for i in a: 
        if len(i) >= 5:
            lis.append(i[::-1])
        else:  
            lis.append(i)
    return " ".join(lis)

############################################################################

def spin_words_pythonic_way(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words("Welcome bro"))
print(spin_words_pythonic_way("Welcome bro"))