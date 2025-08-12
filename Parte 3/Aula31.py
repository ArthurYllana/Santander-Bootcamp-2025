arquivo = open("C:/Users/USUARIO/Desktop/Curso Santander/Santander-Bootcamp-2025/Parte 3/novo.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo")
arquivo.writelines(['\n', "escrevendo", '\n', "um", '\n', "novo", '\n', "texto" ])
arquivo.close()