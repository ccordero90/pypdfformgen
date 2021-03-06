#!/usr/bin/env python

import csv
from fdfgen import forge_fdf
import os
import sys

sys.path.insert(0, os.getcwd())
filename_prefix = "formulario"
csv_file = "formulario.csv"
pdf_file = "formulario.pdf"
tmp_file = "tmp.fdf"
output_folder = './output/'
#os.environ['PATH'] += os.pathsep + 'C:\\Program Files (x86)\\PDFtk\\bin;'  #descomentar si en windows

def process_csv(file):
    headers = []
    data =  []
    csv_data = csv.reader(open(file), delimiter=',')   # cambiar a ';' si se genera csv en libreoffice
    for i, row in enumerate(csv_data):
      if i == 0:
        headers = row
        continue;
      field = []
      for i in range(len(headers)):
        field.append((headers[i], row[i]))
      data.append(field)
    return data

def form_fill(fields):
  fdf = forge_fdf("",fields,[],[],[])
  fdf_file = open(tmp_file,"wb")
  fdf_file.write(fdf)
  fdf_file.close()
  output_file = '{0}{1}_{2}.pdf'.format(output_folder, filename_prefix, fields[1][1])
  cmd = 'pdftk "{0}" fill_form "{1}" output "{2}" dont_ask flatten'.format(pdf_file, tmp_file, output_file)
  os.system(cmd)
  os.remove(tmp_file)

data = process_csv(csv_file)
print('Generating Forms:')
print('-----------------------')
for i in data:
  if i[0][1] == 'Yes':
    continue
  print('{0}_{1} created...'.format(filename_prefix, i[1][1]))
  form_fill(i)
