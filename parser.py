#This python project is a learning experience 

from asyncio.windows_events import NULL
from fileinput import lineno
from html.parser import HTMLParser
import unicodedata
import codecs
import os
from xml.dom.pulldom import CHARACTERS



newfilename = input("Enter the desired name of your Word document: ")


class parseHTMLDataPC(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
      #  print("Encountered a tag:", tag)
        
        if (tag) == 'p':

            (line1, column) = self.getpos()
            


    def handle_data(self, data):

       
        newFilePath = os.path.abspath(newfilename)

        newSave = open(newFilePath + ".doc", "a")
        
        (line, column) = self.getpos()
        
       
        if line > 668:
            
            newSave.writelines("\t" + data + "\n")

            
        newSave.close()



class parseHTMLDataiOS(HTMLParser):
    
    #def handle_starttag(self, tag, attrs):
      #  print("Encountered a tag:", tag)
        #if (tag) == 'p':
            #(line1, column) = self.getpos()
           
    def handle_data(self, data):

        newFilePath = os.path.abspath(newfilename)

        newSave = open(newFilePath + ".doc", "a")
        
        (line, column) = self.getpos()
        newlineType = '\n'
        myDataList = []
        #handlerType = self.handle_starttag(tag="p", attrs 
        if line > 668:
            
            ## my current issue is the intermitent and somewhat random paragraphs found in
            # occasional pieces of ios data
            # #fixme    
            for n in data:
                #if n != CHARACTERS:
                    #if n == newlineType:
                        #print("a newline")
                    
                        #newSave.write("\n")   
            
                myDataList.append(n)
                #print(myDataList)
                
            if newlineType in myDataList:
                #returns true
                newLineIndex = myDataList.index(newlineType)

                print(newLineIndex)

                paragraphStartIndex = newLineIndex + 1
                myDataList.insert(paragraphStartIndex, "\t")
                
                #print(True)
                
            else:
                
                print(False)
                    
            
            
           
            newSave.writelines(myDataList)
                    
                        
            #newSave.writelines("\t" + data + "\n")
        newSave.flush()
        newSave.close()

def main(): 

    importType = float(input("Was your document written on PC(1) or on iOS(2) device?"))
    downloadedFile = input("Enter the name of the exported file: ")
    
    myStore = downloadedFile
    downloadPath = os.path.abspath(myStore)
    f = codecs.open(downloadPath, encoding="utf8")


    if importType == 1:
        parserprint = parseHTMLDataPC()
        parserprint.feed(f.read())
    elif importType == 2:
        parserprint = parseHTMLDataiOS()
        parserprint.feed(f.read())
    else:
        print("Invalid entry: " + importType)
        

    
    parserprint.close()
    f.close()
    

   


main()