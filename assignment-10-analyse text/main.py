# Sentence length in words
def sentencelength(sentence):
    return len(sentence.replace("\n","").replace(" ", ""))

def sentencefinder(wordfile):

     return wordfile.split('.')

def filereader(filename):
    file = open(filename,"r")
    return file.read()

def dictionary(file):
    # copied from assigment 05
    # this array can be changes to remove problems with words like "car" and "car," not beeing recognises as the same words
    unnecessaryCharacters=[".",",","'","1","2","3","4","5","6","7","8","9","0","*","!","¤","%","&","?","*","\ufeff","--"," ",":","\n"]
    wordList={} # wordlist directory
    for oneWord in file.split():
        oneWord = oneWord.lower()
        # for removing characters from the unnecessaryCharacters list
        for character in unnecessaryCharacters:
            oneWord=oneWord.replace(character,"")
        #finds the word if it's alreddy in the deictonery,
        # if not the default valiue is 0
        tempCount=wordList.get(oneWord,0)
        # setting the wordcount and placing the value back
        tempCount += 1
        wordList[oneWord] = tempCount
    return wordList




# Percentage of easy words: easy words are those used frequently: they have high frequency in documents
# Threshold-length is the minimum frequency we defines as a easy number
def getwordffrequencyeasy(file,thresholdlength):
    wordList = dictionary(file) # wordlist directory
    wordoverthethreasold = 0
    sumtotal = 0

    for oneWord in wordList.keys():
        if len(oneWord) >= thresholdlength:
            wordoverthethreasold += wordList.get(oneWord,0)
            #print("Word:",oneWord,"Times:",wordList.get(oneWord,0))
        sumtotal += wordList.get(oneWord,0)
    return wordoverthethreasold/sumtotal*100



# Percentage of difficult words: difficult words are those that are seldom used and have low frequency in documents
def getwordfrequensydifficult(file,thresholdlength):
    wordList=dictionary(file) # wordlist directory
    wordoverthethreasold=0
    sumtotal=0

    for oneWord in wordList.keys():
        frequency = wordList.get(oneWord)
        if frequency <= thresholdlength:
            wordoverthethreasold += wordList.get(oneWord,0)
            #print("Word Low:",oneWord,"Times:",wordList.get(oneWord,0))
        sumtotal += wordList.get(oneWord,0)
    return wordoverthethreasold/sumtotal*100

# Percentage of different words: A count of the unique words in the document divide by the total number of words
def getpercentageuniquewords(file):

    wordList=dictionary(file)  # wordlist directory
    uniquecount = 0
    sumtotal = 0

    for oneWord in wordList.keys():
        wordcount = wordList.get(oneWord,0)
        if wordcount == 1: # unique
            uniquecount += 1
            #print("Word unique:",oneWord,"Times:",wordList.get(oneWord,0))
        sumtotal += wordcount
    return uniquecount/sumtotal*100


# Number of sentences per paragraph
# i have defined a paragraph as 2 line-brakes
def numberofsentencesinparagraph(file):
    paragraphlist=[]

    for paragraph in file.split("\n\n"):
        try:
            list = len(sentencefinder(paragraph))-1
            paragraphlist.append(list)
            paragraphlist.remove(0)
        except:
            pass

    return paragraphlist

if __name__ == '__main__':


    length = []
    file = filereader("test2")
    for sentence in sentencefinder(file):
        length.append(sentencelength(sentence))
    print("lenth of all sentences inn a file",length)
    print("easy words:",getwordffrequencyeasy(file,3))
    print("difficult words:",getwordfrequensydifficult(file,5))
    print("unique words",getpercentageuniquewords(file))
    print("number of sentenes in paragrapfe", numberofsentencesinparagraph(file))