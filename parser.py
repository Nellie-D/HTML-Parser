#This python project was built as a personal project. 
# As a student and hobbyist writer, I frequently write documents
# on the cloud using the Notion app, which syncs across my devices.
# However, I discovered that copy/paste from Notion to Word or Google Docs
# would cause unwanted formatting changes.
# This code handles a Notion HTML import and parses the code for text contents.
# Once parsed, the handler saves the data to a .doc or .txt file based on user choice.


from encodings import utf_8
from html.parser import HTMLParser
import codecs
import os
coding: utf_8

newfilename = input("Enter the desired name of your document: ")
print("What file type do you wish to create?")
concat = input("Please choose .txt or .doc: ")

textType = ".txt"
docType = ".doc"

if concat != textType:
    if concat != docType:
        print("Invalid filetype.")
        concat = input("Please choose .txt or .doc")
    else:
        concat = docType
else: 
    concat = textType

class parseHTMLDataiOS(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        #print("Encountered a tag:", tag)

        if (tag) == 'p':
            (line1, column) = self.getpos()
           

    def handle_data(self, data):

        newFilePath = os.path.abspath(newfilename)
        #newSave = open(newFilePath + ".docx", "a")
        newSave = open(newFilePath + concat, "a", encoding="utf-8")
        (line, column) = self.getpos()
        newlineType = '\n'
        tabType = "\t"
        myDataList = []
        
        if line > 668:
             
            for n in data:
            
                myDataList.append(n)
                if n == newlineType:
                    myDataList.append("\t")
              
            
            if newlineType in myDataList and tabType not in myDataList:
                #returns true
                newLineIndex = myDataList.index(newlineType)
                #print(newLineIndex)
                paragraphStartIndex = newLineIndex + 1
                myDataList.insert(paragraphStartIndex, "\t")
              
           
            else:
                #this helps to break up blocks of text that are formatted differenlty based 
                #on how the document was written (ex. if document was written both pc and ios)
                #myDataList.insert(0, "\n")
                
                if tabType not in myDataList:

                    myDataList.insert(0, "\t")
                    myDataList.append("\n")
                else: 
                    myDataList.append("\n")
                #print(False)

            #print(myDataList)
            newSave.writelines(myDataList)
                      
            
        newSave.flush()
        newSave.close()

def main(): 

    downloadedFile = input("Enter the name of the exported file: ")
    
    myStore = downloadedFile
    downloadPath = os.path.abspath(myStore)
    f = codecs.open(downloadPath, encoding="utf8")

    parserprint = parseHTMLDataiOS()
    parserprint.feed(f.read())
    parserprint.close()
    f.close()
    

   


main()