import pyautogui as pa
import time
import pandas as pd
import os
import glob

pa.PAUSE = 0.5
arquivo = pd.read_excel("PyAutoGUI2/papers_id.xlsx")
print(arquivo)

lista_doi = arquivo["DOI"]

def abrir_navegador():
    pa.press("win") # apertar win
    pa.write("edge")# digitar chorme
    pa.press("enter")# apertar enter
    pa.hotkey("win", "up")
    time.sleep(2)

def abrir_scihub():
    pa.hotkey("ctrl", "l")
    pa.write("https://sci-hub.in/")
    pa.press("enter")
    time.sleep(2)

def pesquisar_doi(doi):
    pa.write(doi)
    pa.press("enter")
    time.sleep(7)

def fazer_download():
    pa.click(x=1856, y=99)
    time.sleep(1)
    pa.press("enter")
    time.sleep(3)
    pa.press("esc")

def pegar_ultimo_arquivo(pasta):
    list_of_files = glob.glob(os.path.join(pasta, "*"))
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def verificar_download(pasta, qtde_antiga_arquivos):
    qtde_nova_arquivos = len(os.listdir(pasta))
    nome_ultimo_arquivo = pegar_ultimo_arquivo(pasta)
    if qtde_nova_arquivos > qtde_antiga_arquivos:
        erro = False
    else:
        erro = True

    return erro, nome_ultimo_arquivo

def registrar_log(erro, nome_ultimo_arquivo, doi):
    if erro:
        mensagem = f"{doi}:\terro\n"
    else:
        mensagem = f"{doi}:\tsucesso - Arquivo: {nome_ultimo_arquivo}\n" 

    print(mensagem)
    with open("PyAutoGUI2/log.txt", "a") as log_texto:
        log_texto.write(mensagem)


# Abrir o navegador
abrir_navegador()

pasta = r"D:\Documentos\Estudo\AutomacaoPython\PyAutoGUI2\donwload_papers"
# para cada arquivo
for doi in lista_doi:
    qtde_antiga_arquivos = len(os.listdir(pasta))
    # abrir o scihub
    abrir_scihub()

    # presquisar o DOI
    pesquisar_doi(doi)

    # fazer o download
    fazer_download()

    # vrrificar se o download deu certo
    erro, nome_ultimo_arquivo = verificar_download(pasta, qtde_antiga_arquivos)

    # registrar no registro
    registrar_log(erro, nome_ultimo_arquivo, doi)


pa.hotkey("ctrl", "w")