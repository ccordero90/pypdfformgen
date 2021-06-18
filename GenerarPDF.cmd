ECHO OFF 

REM agregar PATH para python, pdftk y lector de pdf (en mi caso chrome)
SET PATH=%PATH%;C:\Program Files (x86)\PDFtk\bin\;C:\Users\%username%\AppData\Local\Chromium\Application;C:\Users\%username%\AppData\Local\Programs\Python\Python39\

REM inicio del codigo
del /F /Q output
python pdfformgen.py
cd output
pdftk *.pdf cat output forms.pdf
chrome file:///%~dp0output/forms.pdf
PAUSE 1
