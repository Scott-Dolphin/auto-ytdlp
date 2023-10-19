import subprocess

                                    # using subprocess, invoke yt-dlp to download audio from a youtube video and save in ./output 
def archiveVideo(video_link):
    subprocess.run(['powershell', '-command', f'yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" -P "./output" {video_link}'])

                # Just to make invoking powershell easier.
def run(x):
    subprocess.run(['powershell', '-command', f'{x}'])


    

songs = []
with open('songs.txt') as f:
    for line in f:
       songs.append(line)

for song in songs:
    print("current URL: " + song.strip() + "\n")
    archiveVideo(song.strip())

