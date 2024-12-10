import hashlib
import os
from lxml import etree
from tkinter import Tk, Label, Button, filedialog, messagebox

def calcular_hash(xml_path):
    """
    Calcula o hash MD5 concatenando os conteúdos das tags do XML na ordem em que aparecem.
    """
    # Parse do arquivo XML
    parser = etree.XMLParser(remove_blank_text=True)  # Remove espaços extras
    tree = etree.parse(xml_path, parser)
    root = tree.getroot()

    # Função para concatenar os textos de todas as tags
    def concatenar_textos(element):
        textos = []
        if element.text:  # Adicionar o texto interno da tag
            textos.append(element.text.strip())
        for child in element:  # Recursivamente processar os filhos
            textos.append(concatenar_textos(child))
            if child.tail:  # Adicionar textos após o fechamento da tag
                textos.append(child.tail.strip())
        return ''.join(textos)

    # Encontrar a tag <ptu:hash> e temporariamente limpar seu valor
    namespaces = {"ptu": "http://ptu.unimed.coop.br/schemas/V2_2"}
    tag_hash = root.find(".//ptu:hash", namespaces)
    if tag_hash is not None:
        tag_hash.text = ""  # Limpa o valor do hash temporariamente

    # Concatenar textos de todas as tags
    conteudo_concatenado = concatenar_textos(root)

    # Salvar o conteúdo usado no cálculo do hash para debug
    with open("conteudo_para_hash.txt", "w", encoding="ISO-8859-1") as f:
        f.write(conteudo_concatenado)

    # Calcular o hash MD5
    hash_md5 = hashlib.md5(conteudo_concatenado.encode('ISO-8859-1')).hexdigest().upper()

    return hash_md5

def atualizar_hash_no_arquivo(caminho_arquivo):
    """
    Recalcula o hash do arquivo XML, atualiza o valor no campo <ptu:hash>
    e salva o arquivo em uma nova pasta.
    """
    try:
        # Calcular o hash MD5 do XML
        novo_hash = calcular_hash(caminho_arquivo)

        # Parse do XML novamente para atualizar o hash
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(caminho_arquivo, parser)
        root = tree.getroot()

        # Namespace usado no XML
        namespace_ptu = "http://ptu.unimed.coop.br/schemas/V2_2"
        namespaces = {"ptu": namespace_ptu}

        # Registrar o namespace com o prefixo 'ptu'
        etree.register_namespace("ptu", namespace_ptu)

        # Atualizar a tag <ptu:hash> com o novo valor do hash
        tag_hash = root.find(".//ptu:hash", namespaces)
        if tag_hash is None:
            messagebox.showerror("Erro", "Tag <ptu:hash> não encontrada no XML.")
            return False
        tag_hash.text = novo_hash

        # Criar a pasta na raiz do projeto (dentro de "Processados")
        nome_arquivo = os.path.basename(caminho_arquivo)  # Nome completo do arquivo
        nome_sem_extensao = os.path.splitext(nome_arquivo)[0]  # Apenas o nome, sem a extensão
        pasta_processados = os.path.join(os.getcwd(), "Processados", nome_sem_extensao)  # Caminho completo da pasta

        # Criar a pasta, se não existir
        os.makedirs(pasta_processados, exist_ok=True)

        # Caminho para salvar o arquivo atualizado
        caminho_arquivo_processado = os.path.join(pasta_processados, nome_arquivo)

        # Salvar o arquivo atualizado
        with open(caminho_arquivo_processado, "wb") as f:
            f.write(etree.tostring(tree, encoding="ISO-8859-1", xml_declaration=True))

        messagebox.showinfo("Sucesso", f"Arquivo processado com sucesso! Salvo em:\n{caminho_arquivo_processado}")
        return True

    except etree.XMLSyntaxError as e:
        messagebox.showerror("Erro", f"Erro ao processar o XML: {e}")
        return False

def selecionar_arquivo():
    """
    Abre a janela de seleção de arquivo para escolher o arquivo .xml.
    """
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo",
        filetypes=[("Arquivos .228", "*.228"), ("Arquivos .xml", "*.xml")]
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
    janela.title("Atualizar Hash do Arquivo XML")
    janela.geometry("400x200")
    janela.resizable(False, False)

    # Título
    label_titulo = Label(janela, text="Selecione o arquivo XML", font=("Arial", 14))
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
