# Banco de Dados 1 ​🗃️​​

Evolução da aplicação web em Flask com foco na persistência de dados utilizando o padrão Object-Relational Mapping (ORM) com SQLite e Flask-SQLAlchemy.

---

## 🚀 O que mudou? (Versão Anterior vs. Versão Atual)

- **Persistência Permanente de Dados:** A aplicação deixou de utilizar apenas variáveis de sessão temporárias e passou a armazenar os nomes cadastrados em um banco de dados relacional SQLite.
- **Listagem Dinâmica de Registros:** Além da interface de boas-vindas, a página foi expandida para consultar e exibir uma tabela dinâmica contendo todos os usuários já salvos no banco.

---

## ⚙️ O que foi necessário implementar?

- **Configuração do SQLAlchemy:** Inicialização do ORM no projeto e definição da URI de conexão com o banco de dados SQLite (`data.sqlite`).


- **Modelagem de Dados:** Criação da classe `User` mapeando a tabela de usuários com identificador único (`id`) e nome (`username`).


- **Persistência de Dados:** Implementação da lógica de salvamento (`db.session.add` e `db.session.commit`) acionada após o envio bem-sucedido do formulário.


- **Consulta e Exibição:** Uso de consultas via SQLAlchemy (`User.query.all()`) para recuperar os registros e renderizá-los em formato de tabela na interface web.

---

## 💡 Dicas de Boas Práticas Descobertas

- **Prevenção de Duplicidade:** Verificar se o registro já existe na base antes de realizar o commit evita entradas duplicadas desnecessárias no banco de dados.


- **Uso do ORM:** Abstrair as consultas SQL em classes Python facilita a manutenção do código e garante maior portabilidade entre diferentes sistemas de banco de dados.

---

## 👩🏽‍💻 Demonstração
| Página Inicial - Home |
| :---: |
| <img src="https://github.com/user-attachments/assets/0f960650-25e1-47ca-99b2-506fc5f85b54" /> |
> 💡 Nota: Os demais nomes exibidos na tabela foram populados e persistidos durante as etapas da atividade posterior (atv-7).
