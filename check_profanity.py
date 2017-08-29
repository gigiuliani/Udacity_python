import urllib

def read_text():
    quotes = open("/Users/Giorgio/Documents/Udacity Python/movie_quotes.txt")
    contents_file = quotes.read()
    print contents_file
    quotes.close()
    check_profanity(contents_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print output
    connection.close()

    if 'true' in output:
        print('Alert!')
    elif 'false' in output:
        print('This document is clean')
    else:
        print('Could not scan the doc')
    
read_text()

