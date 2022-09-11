#This python project is a learning experience 

from fileinput import lineno
from html.parser import HTMLParser
import unicodedata
import codecs
import os



newfilename = input("Enter the name of your file: ")

class parseHTMLData(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
      #  print("Encountered a tag:", tag)
        
        if (tag) == 'p':

            (line1, column) = self.getpos()
            


    def handle_data(self, data):

        #myBookCh = open("C:/Users/danie/myParses/myBookCh.txt", "a", encoding='utf-8')
        newFilePath = os.path.abspath(newfilename)

        newSave = open(newFilePath + ".doc", "a")
        
        (line, column) = self.getpos()
        
        if line > 668:
           # print(data + "\n")
            if data.endswith("\n"):
                print("I'm a newline")
                newSave.writelines("\t" + data + "\n")
            
        newSave.close()



def main(): 
    folder = input("Enter the folder name: ") + chr(92) + chr(92)
     
    downloadedFile = input("Enter the name of the exported file: ")
    myStore = folder + downloadedFile
    downloadPath = os.path.abspath(myStore)

    #f = codecs.open("C:/Users/danie/myParses/chapter8.html", encoding="utf8")

    f = codecs.open(downloadPath, encoding="utf8")

    parserprint = parseHTMLData()

    parserprint.feed(f.read())

    parserprint.close()
    f.close()
    

   


main()