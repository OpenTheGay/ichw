from urllib.request import urlopen
type_from = str(input())
type_to = str(input())
amt_from = str(input())


def exchange(type_from, type_to, amt_from):
    ass = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + type_from + '&to=' + type_to \
             + '&amt=' + amt_from
    doc = urlopen(ass)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr
t = exchange(type_from, type_to, amt_from).split('"')
print(t[7].split()[0])


def test_ass():
    assert exchange('USD', 'EUR', '2.5') =='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    print('Access granted')
