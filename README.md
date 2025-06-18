# Video-to-Subtitle-Extractor

Istall: 
<br/>
pip install flask whisper fpdf ffmpeg-python werkzeug

<br/><br/>

🔧 Step 1: Download FFmpeg <br/>
Go to: https://ffmpeg.org/download.html <br/><br/>

Choose Windows builds > Click on https://www.gyan.dev/ffmpeg/builds/<br/>

Download the ZIP under "Release full" — e.g., ffmpeg-release-full.7z or .zip<br/><br/><br/>


🔧 Step 2: Extract and Set Path<br/>
Extract the ZIP file to a folder like:<br/>
<br/>
makefile<br/>
C:\ffmpeg<br/>
Inside that folder, go to:<br/>
C:\ffmpeg\bin<br/>
There you’ll see:<br/>
ffmpeg.exe<br/><br/><br/>


🔧 Step 3: Add FFmpeg to System PATH<br/>
Press Windows + S, search for: "Environment Variables"<br/>
Click: Edit the system environment variables<br/>
Click the "Environment Variables…" button<br/>
Under System variables, select Path → click Edit<br/>
Click New → add:<br/>
makefile<br/>
C:\ffmpeg\bin<br/>
Click OK → OK → OK<br/><br/>


