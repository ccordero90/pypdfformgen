ECHO ON

del /F /Q output
python test.py
cd output
pdftk *.pdf cat output forms.pdf
chrome forms.pdf