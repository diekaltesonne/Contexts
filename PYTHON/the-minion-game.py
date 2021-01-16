# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(word):
    dictionary = {"A","E","I","O","U"}
    stut = {}
    kev = {}
    a = stuart_algo(word,dictionary)
    b = kevin_algo(word,dictionary)

    if(a>b):
        return "Stuart {}".format(a)
    if(a<b):
        return "Kevin {}".format(b)
    return "Something goes wrong"

def sub_algo(word,stut,substr):
    stut[substr]=word.count(substr)
    new_substr = substr+word[word.find(substr)+len(substr)]
    if  word.find(substr)+len(substr)<(len(word)-1):
        new_substr = substr+word[word.find(substr)+len(substr)]
        return sub_algo(word,stut,new_substr)
    else:
        return stut

def stuart_algo(word,dictionary):
    stut = {}
    for letter in word:
        if letter not in dictionary:
            if letter in stut:
                stut[letter] = stut[letter]  + 1
            else:
                stut[letter] = 1
                sub_algo(word,stut,letter)
    return sum(list(stut.values()))
    
def kevin_algo(word,dictionary):
    # Vowels are only defined as AEIOU . In this problem, Y is not considered a vowel.
    kevin = {}
    for letter in word:
        if letter in dictionary:
            if letter in kevin:
                kevin[letter] = kevin[letter]  + 1
            else:
                kevin[letter] = 1
                sub_algo(word,kevin,letter)
    return sum(list(kevin.values()))

if __name__ == '__main__':
    s = input()
    print(minion_game(s))