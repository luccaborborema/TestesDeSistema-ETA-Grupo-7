# Teste de Automação com Selenium - GlobalSQA Banking Project

Este projeto contém testes automatizados usando **Python** e **Selenium WebDriver** para o site de demonstração de internet banking da [GlobalSQA](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login).

## 💻 Site-alvo

[https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login)

O site simula funcionalidades de um banco digital, como login de cliente, adicionar cliente, deletar cliente, abrir conta, depósitos, saques e verificação de transações.

## 📂 Estrutura do Projeto

banking-automation/
│
├── tests/
│ ├── conftest.py
│ ├── pytest.ini
│ ├── test_1.py
│ ├── test_2.py
│ ├── test_3.py
│ ├── test_4.py
│ ├── test_5.py
│ ├── test_6.py
│ ├── test_7.py
│ ├── test_8.py
│ ├── test_9.py
│ ├── test_10.py
│ ├── test_11.py
│ └── test_12.py
│
├── pages/
│ ├── AccountPage.py
│ ├── AddCustomerPage.py
│ ├── BasePage.py
│ ├── CustomerPage.py
│ ├── CustomersListPage.py
│ ├── LoginPage.py
│ ├── ManagerPage.py
│ ├── OpenAccountPage.py
│ ├── TransactionsPage.py
│ └── __init__.py
│
└── README.md


## ⚙️ Pré-requisitos

- PyCharm 2025.1.1.1 (Community Edition)
- Python 3.8+
- Google Chrome
- Package (pytest ,selenium)

## 📦 Instalação

1. Clone o repositório:
   git clone [https://github.com/seu-usuario/banking-automation.git](https://github.com/luccaborborema/TestesDeSistema-ETA-Grupo-7.git)
2. Crie um ambiente virtual:
✅python -m venv
✅source venv/bin/activate  # Linux/Mac
✅venv\Scripts\activate     # Windows
3. Instale os package no Pycharm:
✅pytest
✅selenium

## 🧪 Executando os Testes

Execute todos os testes com o pytest:
- pytest

Ou um teste específico:
pytest tests/test_login.py

## 🧱 Funcionalidades Testadas

✅ Login com cliente cadastrado
✅ Cadastrar cliente
✅ Deletar cliente
✅ Realizar depósito
✅ Realizar saque
✅ Verificar transações


## 🧰 Tecnologias Utilizadas

Python
Selenium WebDriver
Pytest
Page Object

## 📌 Notas

Os testes usam o padrão Page Object para melhor organização e reutilização de código.


## 📄 Licença
Este projeto é apenas para fins educacionais e de demonstração.








