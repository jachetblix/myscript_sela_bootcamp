def find_string(str):
    file = open('/Users/artyomegorov/Desktop/devops_try.txt', 'r')
    text = file.read()
    if str in text:
        print('String ' + str + ' exists in file ' + '"devops_try.txt"')
    else:
        print('String ' + str + " does not exist in file " + '"devops_try.txt"')

