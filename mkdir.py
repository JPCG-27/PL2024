import os

def main():
    i = 1
    while i <= 8:
        os.makedirs(("TPC"+str(i)))
        open("TPC"+str(i)+"/README.md", 'w')
        i += 1

main()