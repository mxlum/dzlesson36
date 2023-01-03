def openPage(filename):
    doc = None
    with open('cgi-bin/'+filename+'.html', 'r') as file:
        doc = file.readlines()
    for line in doc:
        print(line, end='')

openPage('login')