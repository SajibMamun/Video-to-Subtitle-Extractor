# Video-to-Subtitle-Extractor

Istall: 
<br/>
pip install flask whisper fpdf ffmpeg-python werkzeug

<br/><br/>

🔧 Step 1: Download FFmpeg
Go to: https://ffmpeg.org/download.html

Choose Windows builds > Click on https://www.gyan.dev/ffmpeg/builds/

Download the ZIP under "Release full" — e.g., ffmpeg-release-full.7z or .zip


🔧 Step 2: Extract and Set Path
Extract the ZIP file to a folder like:

makefile
C:\ffmpeg
Inside that folder, go to:
C:\ffmpeg\bin
There you’ll see:
ffmpeg.exe


🔧 Step 3: Add FFmpeg to System PATH
Press Windows + S, search for: "Environment Variables"
Click: Edit the system environment variables
Click the "Environment Variables…" button
Under System variables, select Path → click Edit
Click New → add:
makefile
Copy
Edit
C:\ffmpeg\bin
Click OK → OK → OK


