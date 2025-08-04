# 🔐 Gerador de Senhas Aleatórias em Python

Projeto simples desenvolvido com o objetivo de praticar conceitos fundamentais do Python como:

- Importação de módulos
- Estrutura de menus
- Uso de funções
- Manipulação de strings com `string` e `random`
- Arte ASCII com `pyfiglet`
- Modularização em arquivos separados

---

## 🔍 Objetivo

Este projeto foi criado para gerar senhas seguras e aleatórias de forma simples via terminal, com um menu interativo e uma apresentação visual em ASCII Art personalizada.

---

## 📂 Estrutura do Projeto

```
gerador-senhas/
├── ASCII_Art.py           # Gera o banner ASCII com pyfiglet
├── OP.py                 # Contém a função gerador() que cria senhas aleatórias
├── GERADOR_SENHAS.py     # Arquivo principal com o menu de interação
├── README.md             # Documentação do projeto
├── pyproject.toml        # Arquivo de configuração do Poetry
```

---

## 🚀 Como executar

### Requisitos
- Python 3.7+
- [Poetry](https://python-poetry.org/) instalado

### Instalando dependências

```bash
poetry install
```

### Rodando o projeto

```bash
poetry run python GERADOR_SENHAS.py
```

---

## 🛡️ Como funciona

- Ao iniciar o projeto, o menu ASCII aparece no terminal
- O usuário escolhe entre gerar uma senha ou sair
- A senha gerada contém letras maiúsculas, minúsculas, números e caracteres especiais
- O tamanho padrão da senha é 12 caracteres (pode ser ajustado facilmente na função `gerador()`)

---

## 🌐 Tecnologias

- Python 3
- `string` + `random`
- `pyfiglet`
- Poetry para gerenciamento de dependências

---

## 📄 Licença

Projeto sob licença MIT. Livre para usar, modificar e distribuir com créditos.

---

## 👤 Autor

Desenvolvido por **IC4R0**  

---

<p align="center">
  <img src="banner.png" alt="Banner do Gerador de Senhas" width="600">
</p>
