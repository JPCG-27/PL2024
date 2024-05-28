import sys
import re


def main():
    sum = 0
    state = True
    keywords = []
    for line in sys.stdin:
        keywords = re.findall(r'([+\-]?\d+)|([^a-z]on[^a-z])|([^a-z]off[^a-z])|(=)', line, re.IGNORECASE)
        for keyword in keywords:
            if keyword[0] != '':
                if state:
                    sum += int(keyword[0])
            elif keyword[1] != '':
                state = True
            elif keyword[2] != '':
                state = False
            elif keyword[3] != '':
                print(sum)
main()