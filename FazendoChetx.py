import os
from ContandoArquivos import FuncaoContarArquivos

caminho_DataSet = fr"C:\Users\Oliveira\Documents\Pibic\DataSetDoencasPulmonares"
total_de_arquivos_DataSet = 0

print("Caminho datset", len(caminho_DataSet))
doencas_arquivos = os.listdir(caminho_DataSet)


print(doencas_arquivos)
print(len(doencas_arquivos))


for arquivo in doencas_arquivos:
    #analisar = fr"C:\Users\Oliveira\Documents\Pibic\DataSetDoencasPulmonares\{arquivo}"
    pegar_caminho = os.listdir(fr"C:\Users\Oliveira\Documents\Pibic\DataSetDoencasPulmonares\{arquivo}")
    arquivos_diretorio = len(pegar_caminho)

    total_de_arquivos_DataSet += arquivos_diretorio
    print(f"pego de {arquivo} tem {arquivos_diretorio} arquivos ")

print(f"\nTotal de aruqinos no DATASET há {total_de_arquivos_DataSet}")







