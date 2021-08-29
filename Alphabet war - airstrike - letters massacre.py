"""
Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension
between left side letters and right side letters was
too high and the war began. The letters called
airstrike to help them in war - dashes and dots
are spreaded everywhere on the battlefield.

Task
Write a function that accepts fight string consists
of only small letters and * which means a bomb drop
place. Return who wins the fight after bombs are
exploded. When the left side wins return Left side
wins!, when the right side wins return Right side
wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3 
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3 
 d - 2
 z - 1
The other letters don't have power and are only
victims.
The * bombs kills the adjacent letters
( i.e. aa*aa => a___a, **aa** => ______ );

Example
AlphabetWar("s*zz");           //=> Right side wins!
AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
AlphabetWar("zzzz*s*");       //=> Right side wins!
AlphabetWar("www*www****z");  //=> Left side wins!
"""

def alphabet_war(fight):
    letters = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    score = 0
    tempList = []
    
    for f in fight:
        tempList.append(f)

    for r in range(len(tempList)-1):
        if r != '*' and tempList[r+1] == '*':
            tempList[r] = ''
        elif r != '*' and tempList[r-1] == '*':
            tempList[r] = ''
        elif r == len(tempList)-2 and tempList[r] == '*':
            tempList[r+1] = ''
    
    for t in tempList:
        if t in letters.keys():
            score += letters[t]
    
    if score > 0:
        return 'Left side wins!'
    if score < 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"

print("Tests:")
print(alphabet_war("z"))
print(alphabet_war("****"))
print(alphabet_war("z*dq*mw*pb*s"))
print(alphabet_war("zdqmwpbs"))
print(alphabet_war("zz*zzs"))
print(alphabet_war("sz**z**zs"))
print(alphabet_war("z*z*z*zs"))
print(alphabet_war("*wwwwww*z*"))
print(alphabet_war("w****z"))
print(alphabet_war("mb**qwwp**dm"))