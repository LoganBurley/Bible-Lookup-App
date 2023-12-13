#Logan Burley - 11/13/2022
#Bible Search App
#All works

#FUNCTIONS
def prettyPrint(line):
  lineLength = 80
  while line:
    if (len(line) > 80):
      toPrint = line[0:lineLength]  #get chars to print
      line = line[lineLength:]  #remove those chars from string
      splitToPrint = toPrint.split(' ')  #split string on spaces
      print(' '.join(splitToPrint[0:-1]))  #print breaking on last space
      line = splitToPrint[-1] + line  #add back the stuff that wasn't printed
    else:
      print(line)
      line = ''

def writeToVerses(line):
  with open("verses.txt", "a") as verse:
    verse.write(line)

def isBook(line):
  return line.startswith('THE BOOK OF ')

def isBookLine(line, book):
  return line.startswith('THE BOOK OF ' + book.upper())

def isChapter(line):
  return line.startswith('CHAPTER ') or line.startswith('PSALM ')


def isChapterLine(line, chapter):
  return line.startswith('CHAPTER ' + chapter) or line.startswith('PSALM ' +
                                                                  chapter)

def isVerseLine(line, verse):
  return line.startswith(verse + ' ')

#START MAIN
keepSearching = True

#get book, chapter, verse
print('Enter the reference of the verse you want to retrieve')

while (keepSearching):
  print()  #breathing room

  book = input('Enter Book: ')
  chapter = input('Enter Chapter: ')
  verse = input('Enter Verse: ')
  print()

  bookFound = False
  chapterFound = False
  verseFound = False

  #check if book is in abbreviations file, if it's in there use the 2nd value
  with open('Bible_Abbreviations.csv', 'r') as abbv:
    for line in abbv:
      if line.split(',')[0].lower() == book.lower():
        book = line.split(',')[1]
        break

  #cleaning whitespace
  book = book.strip()
  chapter = chapter.strip()
  verse = verse.strip()

  with open('Bible.txt', 'r') as bible:
    for line in bible:

      #stop searching if we get out of bounds of book
      if (bookFound and isBook(line)):
        break

      #stop seraching if we get out of bounds of chapter
      if (chapterFound and isChapter(line)):
        break

      #find book
      if not bookFound and isBookLine(line, book):
        bookFound = True

      #find chapter
      if bookFound and isChapterLine(line, chapter):
        chapterFound = True

      #find verse
      if chapterFound and isVerseLine(line, verse):
        verseFound = True
        line = line.replace(verse + ' ', '', 1)  #remove verse number
        print(book + ' ', chapter, ':', verse + ' ', sep='',
              end='')  #print verse reference
        prettyPrint(line)
        writeToVerses(line)
        break

  #print error if book, chapter, or verse not found
  if not bookFound:
    print('Book "' + book + '" does not exist')
  elif bookFound and not chapterFound:
    print('Chapter "' + chapter + '" in book "' + book + '" does not exist')
  elif bookFound and chapterFound and not verseFound:
    print('Verse "' + verse + '" in chapter "' + chapter + '" of book "' +
          book + '" does not exist')

  #ask if user wants to search again
  if input('Search again? (Y/N): ').lower() != 'y':
    keepSearching = False
    
