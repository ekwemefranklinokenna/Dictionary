import re
import urllib.request

#https://www.dictionary.com/browse/

url = "https://www.dictionary.com/browse/"
try:
    word = input("Enter the Word: ")

    url = url + word

    data = urllib.request.urlopen(url).read()

    data1 = data.decode("utf-8")
    m = re.search('meta name="description" content="',data1)
    start = m.end()
    end = start + 300

    newString = data1[start:end]

    #print(newString)

    m = re.search("See more.", newString)
    end = m.start() -1

    definition = newString[0:end]

    print(definition)
except:
    print("Sorry this word is not in the dictionary")
