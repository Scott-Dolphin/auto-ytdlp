def file_read(fileName):
    songs = []
    with open(fileName) as f:
        for line in f:
            url = line
            if url[len(url) - 2:] == r'\n':
                songs.append(url)


            
    
    return songs


myWord = 'Hello World!'
lastTwo = myWord[len(myWord) -2:]
print(myWord)
print(lastTwo)
print(myWord[:len(myWord) -2])

# mySongs = file_read("songs.txt")
# print(mySongs)