import subprocess

def run(x):
    subprocess.run(['powershell', '-command', f'{x}'])

run('python.exe -m pip install --upgrade pip')
run('python3 -m pip install --no-deps -U yt-dlp')