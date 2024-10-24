# Aprimorando a técnica de dividir e conquistar para o alinhamento de múltiplas sequências de pares

Esse é um artigo e estudo sobre o aprimoramento da técnica de dividir e conquistar para o alinhamento de múltiplas sequências de pares. Muito utilizado em bioinformática para alinhar sequências de DNA, RNA e proteínas.

O repositório contém o código em python que implementa a técnica de dividir e conquistar para o alinhamento de múltiplas sequências de pares, além do artigo em pdf traduzido, o código fonte em latex e os slides da apresentação.

## Rodando o código

primeiro dê o git clone do repositório

```bash
git clone https://github.com/icarompo/Improving-the-divide-and-conquer-approach-to-sum-of-pairs-msa.git
```

Depois entre na pasta do repositório

```bash
cd Improving-the-divide-and-conquer-approach-to-sum-of-pairs-msa
```

crie um ambiente virtual

```bash
python3 -m venv venv
```

ative o ambiente virtual

```bash
source venv/bin/activate
ou para windows: 
venv\Scripts\activate
```

instale as dependências

```bash
pip install -r requirements.txt
```

rode o código

```bash
python main.py
```

obs: atualize as dependências com o comando `pip freeze > requirements.txt` caso instale alguma nova dependência