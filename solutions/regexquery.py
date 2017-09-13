import re

if __name__ == '__main__':

    string = input('Please enter string')
    regexQuery = input('Please enter regex query')

    try:
        p = re.compile(regexQuery)
        if p.match(string) is not None:
            print(p.match(string))
        else:
            print('Returns nothing')

    except Exception as e:
        print(str(e))
