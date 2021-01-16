# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(word):
    a = stuart_algo(word)
    b = kevin_algo(word)

    if(a>b):
        return "Stuart {}".format(a)
    if(a<b):
        return "Kevin {}".format(b)
    return "Something goes wrong"

def stuart_algo(word):
    
    return ""
def kevin_algo(word):
    # Vowels are only defined as AEIOU . In this problem, Y is not considered a vowel.

    return ""

if __name__ == '__main__':
    s = input()
    print(minion_game(s))