import sys
import re
from urllib.request import urlopen


def wcount(lines, topn=10):
    d = {}
    doc = urlopen(lines)
    docstr = doc.read().decode('GBK')
    doc.close()
    s = docstr.lower()
    words = re.findall(r'[a-zA-Z]+', s)
    set1 = set(words)
    list2 = list(set1)
    for x in range(len(list2)):
        d[list2[x]] = 0
        for y in range(len(words)):
            if list2[x] == words[y]:
                d[list2[x]] += 1
    d = sorted(d.items(), key=lambda d:d[1], reverse=True)
    for i in d[:topn]:
        i = list(i)
        print(i[0], i[1])

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
