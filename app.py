import hashlib
import os  # Biblioteca para manipulação de pastas e arquivos
import xml.etree.ElementTree as ET
from tkinter import Tk, Label, Button, filedialog, messagebox

def calcular_hash(conteudo):
    """
    Calcula o hash MD5 do conteúdo fornecido, usando o encoding ISO-8859-1.
    """
    return hashlib.md5(conteudo.encode('ISO-8859-1')).hexdigest()

def atualizar_hash_no_arquivo(caminho_arquivo):
    """
    Lê o arquivo XML, recalcula o hash, cria uma pasta com o nome do arquivo e salva o arquivo atualizado dentro.
    """
    try:
        # Carregar o XML
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()

        # Namespace usado no XML
        namespaces = {"ptu": "http://ptu.unimed.coop.br/schemas/V2_2"}  # Atualize o namespace aqui conforme o arquivo

        # Encontrar a tag <ptu:hash>
        tag_hash = root.find(".//ptu:hash", namespaces)
        if tag_hash is None:
            messagebox.showerror("Erro", "Tag <ptu:hash> não encontrada no XML.")
            return False

        # Recalcular o hash com base no conteúdo do XML (exceto o valor do hash atual)
        valor_original = tag_hash.text
        tag_hash.text = ""  # Temporariamente removendo o hash para recalcular
        conteudo = ET.tostring(root, encoding='ISO-8859-1', method='xml').decode('ISO-8859-1')
        novo_hash = calcular_hash(conteudo)

        # Atualizar o hash no XML
        tag_hash.text = novo_hash

        # Criar a pasta na raiz do projeto (dentro de "Processados")
        nome_arquivo = os.path.basename(caminho_arquivo)  # Nome completo do arquivo
        nome_sem_extensao = os.path.splitext(nome_arquivo)[0]  # Apenas o nome, sem a extensão
        pasta_processados = os.path.join(os.getcwd(), "Processados", nome_sem_extensao)  # Caminho completo da pasta

        # Criar a pasta, se não existir
        os.makedirs(pasta_processados, exist_ok=True)

        # Caminho para salvar o arquivo atualizado
        caminho_arquivo_processado = os.path.join(pasta_processados, nome_arquivo)

        # Salvar o arquivo com o hash atualizado no encoding ISO-8859-1
        try:
            tree.write(caminho_arquivo_processado, encoding='ISO-8859-1', xml_declaration=True)
            messagebox.showinfo("Sucesso", f"Arquivo processado com sucesso! Salvo em:\n{caminho_arquivo_processado}")
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o XML atualizado: {e}")
            tag_hash.text = valor_original  # Reverter para o valor original em caso de erro
            return False

    except ET.ParseError as e:
        messagebox.showerror("Erro", f"Erro ao ler o XML: {e}")
        return False

def selecionar_arquivo():
    """
    Abre a janela de seleção de arquivo para escolher o arquivo .228.
    """
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=[("Arquivos .228", "*.228")]
    )
    if caminho_arquivo:
        # Processar o arquivo selecionado
        if atualizar_hash_no_arquivo(caminho_arquivo):
            print("Processo concluído com sucesso!")
        else:
            print("Ocorreu um erro durante o processo.")

# Criar a interface gráfica
def criar_interface():
    # Configurar a janela principal
    janela = Tk()
    janela.title("Atualizar Hash do Arquivo A500")
    janela.geometry("400x200")
    janela.resizable(False, False)

    # Título
    label_titulo = Label(janela, text="Selecione o arquivo A500 (.228)", font=("Arial", 14))
    label_titulo.pack(pady=20)

    # Botão para selecionar o arquivo
    botao_selecionar = Button(
        janela, text="Selecionar arquivo", command=selecionar_arquivo, font=("Arial", 12)
    )
    botao_selecionar.pack(pady=20)

    # Iniciar a interface
    janela.mainloop()

# Executar a aplicação
if __name__ == "__main__":
    criar_interface()
