#Projeto para mesclar PDF´s

import PyPDF2 as pdf2
import os

merger = pdf2.PdfMerger()

lista_arquivos = os.listdir("arquivos") #listar o que está dentro de uma pasta
lista_arquivos.sort() #.sort() sempre ordena os arquivos

for arquivo in lista_arquivos:
    if ".pdf" in arquivo: #só existe para garantir que será um .pdf
        merger.append(f'arquivos/{arquivo}') #o append adiciona o arquivo no merger
        #não se esqueça de numerar os pdfs para saber a ordem correta.
        #tem que passar o caminho todo da pasta, para ser dinamico formatamos de forma dinamica.

merger.write('PDF Final.pdf') #write escreve o arquivo, cria um arquivo novo.
print('Os Pdfs foram mesclados')