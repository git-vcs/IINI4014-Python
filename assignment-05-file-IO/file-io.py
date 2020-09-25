import os
##  Task 01
#  Write a function getwordfreqs() that takes a filename as input and returns a dictionary of words and their frequencies.

fileList=[] ## saves possisition of all files in the folder structure

def getwordfreqs(fileName):

    # this array can be changes to remove problems with words like "car" and "car," not beeing recognises as the same words
    unnecessaryCharacters=[".",",","'","1","2","3","4","5","6","7","8","9","0","*","!","¤","%","&","?","*","\ufeff","--"," ",":","\n"]

    wordList={} # wordlist directory
    #reading the file
    file= open(fileName,"r")
    loadedFile = file.read()
    loadedFile=loadedFile.split() # returning an array of the file with alle words
    for oneWord in loadedFile:
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


##  Task 02
#  Write a function getwordsline() that takes as input a file name and a word (string) and returns a list of the line numbers were the word is found.

def getwordsline(fileName, word):
    foundWord=[]
    file= open(fileName,"r")
    loadedFile=file.read().split("\n")  # slipts the array on line of the boosk
    lineCounter=1
    for oneLine in loadedFile:
        if(oneLine.count(word)>0):
            foundWord.append([lineCounter,oneLine.count(word)])
        lineCounter += 1
    return foundWord


 # this is a Function for generating a table of all files in the given rootdir and sub-dirs
def folderWalker(rootDir):
    # generates a list of all files and folders
    filesAndFolders=os.listdir(rootDir)
    for oneFolderOrFile in filesAndFolders:
        # checking if it's a file or folder
        if os.path.isdir(rootDir+'/'+oneFolderOrFile):
            # recursive, sending a new directory name to the function
            folderWalker(rootDir+'/'+oneFolderOrFile)
        else:
            # files are stored in the filelist variable
            if os.path.isfile(rootDir+'/'+oneFolderOrFile):
                fileList.append(rootDir+'/'+oneFolderOrFile)







def main():
    writer=open("output","w")
    folderWalker("books")
    # setting up writer for saving the output
    writer=open("output","w")
    for oneFile in fileList:
        # writing the file filename
       writer.write(oneFile+':\n,')

       #  fetching dictionary from one book
       wordArray=getwordfreqs(oneFile)

        # writing result to file
       writer.write(str(wordArray))
       writer.write('\n')
       writer.write('\n')

       #printing result
       print(getwordsline(oneFile,"car"))
       print(wordArray)
    writer.close()














if __name__ == '__main__':
    main()