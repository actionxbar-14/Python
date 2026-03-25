



#csv : Using csv module 

import csv
file = open('file.csv', mode = 'r')
reader = csv.reader(file)




#csv : Using pandas library

import pandas as pd 
df = pd.read_csv('file.csv')



#excel : Using pandas library

import pandas as pd 
df = pd.read_excel('file.xlsx')



#PDF Using PyPDF2 library :

import PyPDF2 
file = open('file.pdf', 'b')
pdf_reader = PyPDF.PdfReader(file)