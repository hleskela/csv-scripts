import argparse
import glob
import sys

parser = argparse.ArgumentParser(description='Merge some .csv files.')
parser.add_argument("-d", "--directory", help="Path to the directory containing the .csv files to be merged", required=True)
parser.add_argument("-l", "--length", help="Number of lines in the longest document", type=int, required=True)
args = parser.parse_args()

MAXLENGTH = args.length
DIRECTORY = args.directory
fileNames = []
fileObjects = []

def getFilesToMerge():
    print("In files to merge")
    for filename in glob.glob(DIRECTORY + '*.csv'):
        fileNames.append(filename);

def readFiles():
    try:
        for f in fileNames:
            print(f)
            fileObjects.append(open(f, 'r+'))
    
        print('opening mergedFile.csv')
        mergedFile = open('mergedFile.csv', 'w+')

        for fileObject in fileObjects:
            numberOfLines = 0
            numberOfParameters = fileObject.readline() # read the first line to get number of words per line

        
            mergedFile.seek(0,0) # Set pointer to start of mergedFile
            rowLength = len(mergedFile.readline())
            print("rowLength of mergedFile: " + str(rowLength))
            mergedFile.seek(rowLength, 0)
            print("numberOfParameters: " + numberOfParameters)
            mergedFile.write(numberOfParameters)

            print(numberOfParameters, end='') # To remove newline from output
            NA = ''
            words = numberOfParameters.split(',') #Did this split the last newline to? why?
            words.pop() #To remove the newline from the end of the list
            
            for word in words:
                print(word) #Why does this create an extra printed line which is empty? Doc formatting?
                NA += 'NA,' # TODO make it with space if you want it
            NA = NA[:-1] # to remove the final comma
        
            for line in fileObject:
                numberOfLines+=1
                print("line: " +line)
                mergedFile.write(line)

            print(numberOfLines)
            print(NA)
            print("numberOfLines:" + str(numberOfLines))
            while numberOfLines < MAXLENGTH:
                print("WHY YOU HERE?")
                fileObject.seek(0,2) #go to the end
                fileObject.write('\n')
                fileObject.write(NA)
                numberOfLines+=1
    finally:
        for f in fileObjects:
            try:
                f.close()
            except IOError:
                print("Couldn't close file")


getFilesToMerge()
readFiles()
