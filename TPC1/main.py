import math
import sys

def main():
    sports = []
    ageGroups = []
    able = 0
    disabled = 0
    skip = True
    for line in sys.stdin:
        if skip :
            skip = False
        else :
            words = line.split(',')
            ageGroup = math.floor(int(words[5]) / 5) 
            while ageGroup >= len(ageGroups):
                ageGroups.append(0)
            ageGroups[ageGroup] += 1
            if words[8] not in sports:
                sports.append(words[8])
            if words[12] == "true\n":
                able +=1
            else :
                disabled +=1
    sports.sort()
    print("Modalidades desportivas: ")
    for sport in sports:
        print(sport)
    print("\n")
    print("Atletas aptos : " + str(able) + "             Atletas inaptos :" + str(disabled) + "\n")
    i = 0
    for ageGroup in ageGroups:
        if ageGroup > 0 :
            print("[" + str(i*5) + "-" + str(i*5+4) + "]:" + str(ageGroup))
        i += 1
    
main()