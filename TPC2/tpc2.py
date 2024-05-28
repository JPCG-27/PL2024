import sys
import re

def replaceTitle(match):
    i = str(len(match.group(1)))
    return "<h" + i + match.group(2) + "/h" + i + ">"

def main():
    inList = False
    for line in sys.stdin:
        line = re.sub(r'^(#+)(.*)', replaceTitle,line)
        line = re.sub(r'\s\*\*(.+)\*\*', r'<b>\1<\/b>', line)
        line = re.sub(r'\s\*(.+)\*', r'<i>\1<\/i>', line)
        line = re.sub(r'\s\[(.+)\]\((.+)\)', r'<a href="\2">\1</a>', line)
        line = re.sub(r'\s!\[(.+)\]\((.+)\)', r'<img src="\2" alt="\1"/>', line)
        if re.match(r'[1-9]\d*\.(.+)', line) is not None:
            if not inList:
                inList = True
                print("<ol>")
            line =  re.sub(r'^[1-9]\d*\.(.+)', r'<li>\1</li>' ,line)
        elif inList :
            inList = False
            print("</ol>")
        print(line, end="")
main()