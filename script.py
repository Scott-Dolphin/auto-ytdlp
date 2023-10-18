

songs = []
with open('songs.txt') as f:
    for line in f:
       songs.append(line)

for song in songs:
    song
    print(song.strip())
