import os
import time
#methodes from assigment 05
fileList=[] ## saves possisition of all files in the folder structure

#the dictionary variable that stores all the strings. The strings are stored in arrays inside the directory with the strings length as key.
dictionary={}

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




def readfile(fileName):
    # this array can be changes to remove problems with words like "car" and "car," not beeing recognises as the same words
    unnecessaryCharacters=[".",",","'","1","2","3","4","5","6","7","8","9","0","*","!","¤","%","&","?","*","\ufeff","--"," ",":","\n"]
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

        # setting the wordcount and placing the value back
    return loadedFile






# putter input inn i diksjobary
def insertIntoDictionary(input):
    global dictionary
    for oneWord in input:
        #fetching the array with the same key(length) as the input string
        tempArray = (dictionary.get(len(oneWord),[]))
        if len(tempArray) >= 1:
            tempArray = insertAndSort(tempArray,oneWord)
            dictionary[len(oneWord)] = tempArray
        else:
            dictionary[len(oneWord)] = insertAndSort(tempArray,oneWord)




# assigment 07

# metode for Inserting an value into a specific place in the array. If there is a entry in the target position the value is pushed one to the right
def spliceArray(array, endpossition, valiue):
    temp = []
    temp.append(valiue)
    #all valiues before endpossition + new valiue + the rest for the array
    return array[:endpossition]+temp+array[endpossition:]


# Takes the arrays with already sorted inputs and inserts the new word into the arrays
# the algorithm finds the position in the array where the string equal or bigger and insert the string.
# This way we are sorting the array.
def insertAndSort(array,input):
    plassert = False
    for i in range(len(array)):
        if array[i] == input:
            plassert = True
            array=spliceArray(array, i, input)
            break
        elif array[i] > input:
            plassert = True
            array=spliceArray(array, i, input)
            break
    if len(array) == 0:
        array.append(input)
        return array
    if not plassert:
        array.append(input)
    return array




def main():
    #reading multiple files can be time consuming and is therefore commented out
    #code from assignment 5 fore finding all tekst files and store there location in an array
    #folderWalker("books")

    #Reading all the files and inserting the data into the directory variabl
   # for onebok in fileList:
   #     timenow=time.time()
   #     print(onebok)
   #     words = readfile(onebok)
   #     insertIntoDictionary(words)
   #     print(time.time()-timenow)

    #you can also insert words like this
    insertIntoDictionary(["first string","secound string","third String","four","etc","a","aa","b","bb"])


    # Printing all entries in directory
    for i in range(0,max(dictionary.keys())):
        print("nr:",i,dictionary.get(i,"Ingen ord med denne lengden"))


if __name__ == '__main__':
    start =time.time()
    main()
    print("programet er ferdig",time.time()-start)
