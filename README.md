# Sistema Bancário

Projeto realizado para disciplina DIM0517 - Gerência de Configuração e Mudanças (2023.1)

## Autores

- [@Douglas08Santos](https://github.com/Douglas08Santos)

## Critérios Avaliados

- Aplicação correta das boas práticas e convenções de Controle de Versão apresentados
em sala de aula
- Uso adequado das ferramentas relacionadas
- Linguagem utilizada: **Python**
- Ferramenta utilizada para gerência: **Git Flow**


## Requisitos

- Desenvolvimento de sistema bancário (Front-end pode ser Console ou Web)
- Apenas 5 operações: 
    - **Cadastrar Conta**
    - **Consultar Saldo**
    - **Crédito**
    - **Débito** e
    - **Transferência**
- Separação em camadas (pelo menos Front-end e Back-end)
- Utilizar o Github para gestão do repositório
    - Adicionar o usuário gibeonufrn como colaborador do projeto
- Utilizar o padrão Gitflow OU GitLabFlow
- O repositório não poderá ser removido após a criação.
- As branches **NÃO** devem ser removidas – nem mesmo as auxiliares -- durante todo o desenvolvimento do projeto.

## Especificação dos requisitos

- **Cadastrar Conta**
    - Solicita um número e cria uma conta com este número e saldo igual a zero
- **Consulta Saldo**
    - Solicita um número de conta e exibe o saldo da conta
- **Crédito**
    - Solicita um número e valor
    - Atualiza a conta informada acrescentando o valor informado ao saldo
- **Débito**
    - Solicita um número e valoro
    - Atualiza a conta informada subtraindo o valor informado ao saldo
- **Transferência**
    - Solicita o número de conta de origem, número de conta de destino e valor a ser transferido
    - Realiza o débito da conta de origem e o crédito na conta destino

## Requisitos adicionais
- As contas podem ter saldo negativo
- Não existe limite de número de contas que podem ser criadas
- A conta deve ter apenas os atributos número e saldo

# Para executar
    
    python main.py