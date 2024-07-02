import os
cont =0
#contador = 0
def contar_arquivos_caminho(caminho):
    try:
        lista_arquivos = os.listdir(caminho)

        return len(lista_arquivos)
    except OSError:
        return "Caminho inválido"

for c in range(1, 10):
  caminho_da_sua_pasta = fr"C:\Users\Oliveira\Documents\Pibic\images\images_00{c}\images"
  print("Número de arquivos na pasta:",c, contar_arquivos_caminho(caminho_da_sua_pasta))
  cont += contar_arquivos_caminho(caminho_da_sua_pasta)

for c in range(10, 13):
  caminho_da_sua_pasta = fr"C:\Users\Oliveira\Documents\Pibic\images\images_0{c}\images"
  print("Número de arquivos na pasta:",c, contar_arquivos_caminho(caminho_da_sua_pasta))
  cont += contar_arquivos_caminho(caminho_da_sua_pasta)


print(cont)

