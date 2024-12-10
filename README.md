# Atualizador de Hash para Arquivos XML

## Descrição

Este projeto foi desenvolvido para recalcular o hash de arquivos XML do padrão A500 (versão XML 2.2) utilizados na integração com sistemas da Nova CMB. O hash é calculado utilizando o algoritmo MD5, garantindo que os dados estejam íntegros e em conformidade com as especificações esperadas.

O programa utiliza uma interface gráfica (GUI) para facilitar o uso, permitindo selecionar arquivos XML ou .228, recalcular o hash, atualizar o valor na tag <ptu:hash> e salvar o arquivo processado em uma pasta dedicada.

## Funcionalidades

* **Interface Gráfica**:

   - Desenvolvido com Tkinter para facilitar a seleção e processamento dos arquivos.


* **Recalcular o Hash**: 
    - O hash MD5 é recalculado com base no conteúdo concatenado das tags do arquivo XML (excluindo a tag <ptu:hash> durante o cálculo).


* **Atualizar o Arquivo**:

    - Atualiza automaticamente o campo <ptu:hash> com o novo hash calculado.


* **Salvar Arquivo Processado**:

    - O arquivo atualizado é salvo em uma subpasta específica dentro da pasta Processados.


* **Suporte a Arquivos .xml e .228**:

    - Compatível com arquivos XML (A500 - versão XML 2.2) e arquivos com a extensão .228.


* **Debug do Conteúdo**:

    - O conteúdo utilizado no cálculo do hash é salvo em um arquivo chamado conteudo_para_hash.txt para facilitar a inspeção.


## Tecnologias Utilizadas

  * *Python 3.x*
  * *Tkinter:* Biblioteca nativa para criar a interface gráfica.
  * *lxml:* Biblioteca para manipulação de arquivos XML com suporte avançado a namespaces.
  * *Hashlib:* Para o cálculo do hash MD5.
  * *OS:* Para manipulação de diretórios.


## Pré-requisitos

Certifique-se de que as seguintes dependências estão instaladas no seu sistema:

### Instalar Python:

* Faça o download do Python em https://www.python.org/.


### Instalar Dependências do Projeto:

Execute o seguinte comando para instalar a biblioteca lxml, caso não esteja instalada:

```bash
 pip install lxml
```

## Modo de Uso

1. Execute o programa:

   * Salve o código Python em um arquivo, por exemplo, atualizador_hash.py.
   * Execute o arquivo no terminal ou clique diretamente para abri-lo:

```bash
 python calculahash_A500.py
```

2. Selecione o Arquivo:

   * Na interface gráfica que será aberta, clique no botão "Selecionar arquivo".
   * Escolha um arquivo .xml ou .228 no seu sistema.
   

3. Processamento do Arquivo:

   * O programa recalcula o hash do arquivo, atualiza o campo <ptu:hash> e salva o arquivo atualizado.
   

4. Arquivo Salvo:

   * O arquivo atualizado será salvo na pasta Processados, dentro de uma subpasta com o nome do arquivo processado.
   * Exemplo de estrutura gerada:


```bash
 Processados/
└── NomeDoArquivo/
    └── NomeDoArquivo.xml
```

5. Conteúdo para Debug:

* O conteúdo utilizado no cálculo do hash será salvo em um arquivo chamado conteudo_para_hash.txt, gerado na mesma pasta do script.


## Exemplo de Uso

### Entrada: 

Arquivo XML com a seguinte estrutura:

```bash
<ptu:ptuA500 xmlns:ptu="http://ptu.unimed.coop.br/schemas/V2_2">
    <ptu:cabecalho>
        <ptu:nrVerTra_PTU>05</ptu:nrVerTra_PTU>
        <ptu:unimed>
            <ptu:cd_Uni_Destino>865</ptu:cd_Uni_Destino>
            <ptu:cd_Uni_Origem>228</ptu:cd_Uni_Origem>
        </ptu:unimed>
    </ptu:cabecalho>
    <ptu:hash>1234567890ABCDEF1234567890ABCDEF</ptu:hash>
</ptu:ptuA500>
```

### Saída:

Arquivo atualizado com o novo hash:

```bash
<ptu:ptuA500 xmlns:ptu="http://ptu.unimed.coop.br/schemas/V2_2">
    <ptu:cabecalho>
        <ptu:nrVerTra_PTU>05</ptu:nrVerTra_PTU>
        <ptu:unimed>
            <ptu:cd_Uni_Destino>865</ptu:cd_Uni_Destino>
            <ptu:cd_Uni_Origem>228</ptu:cd_Uni_Origem>
        </ptu:unimed>
    </ptu:cabecalho>
    <ptu:hash>098F6BCD4621D373CADE4E832627B4F6</ptu:hash>
</ptu:ptuA500>
```

## Estrutura do Projeto

```bash
calculahash_A500.py        # Código principal do programa
app.py                     # Código Primário (versão 1.0)
app2.py                    # Código Secundário - funcional, porém sem melhorias
conteudo_para_hash.txt     # Conteúdo usado no cálculo do hash (debug)
Processados/               # Pasta onde os arquivos atualizados são salvos
```

## Como Contribuir

Se desejar contribuir para este projeto:

1. Realize um fork do repositório.

2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).

3. Faça commit das suas alterações (git commit -m 'Adiciona nova feature').

4. Submeta um Pull Request.


## Autor

**Wellington Barbosa de Jesus**

💻 Desenvolvedor de Software | Especialista em Automação e Bancos de Dados


* 🌟 **Sobre:** Apaixonado por resolver problemas complexos com soluções simples e eficientes.

* 📧 **Contato:** <wellington_developer@outlook.com.br>

* 🌐 **Portfólio:** *Em construção*

* 🐙 **GitHub:** <https://github.com/Wellington-Barbosa>

* 👔 **LinkedIn:** <https://www.linkedin.com/in/wellington-barbosa2908/>