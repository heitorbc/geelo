Feature: Gerencimento de Produto
  
    Background: Em todos os testes o usuário deve estar logado.
        Given Eu sou um usuario logado
      
    Scenario: Produto cadastrado com sucesso
        Given Eu estou na pagina de cadastrado de produto
        And Eu informo a descricao, valor do produto, valor da comissao, modalidade, quantidade disponivel e data/hora
        When Eu clico no botao cadastrar o produto
        Then Eu sou redirecionado para a pagina com a lista de produtos cadastrados
        And O produto deve estar devidamente cadastrado
    
    Scenario: Produto editado com sucesso
        Given Estou na pagina de lista de produtos
        And Seleciono o botao editar de um produto
        And Sou redirecionado para a pagina com os dados do produto ja preenchidos
        And Preencho o campo valor da comissao com um novo valor
        When Clico no botao editar o produto
        Then Eu sou redirecionado para a pagina com a lista de produtos cadastrados
    
    Scenario: Produto excluido com sucesso
        Given Estou na pagina de lista de produtos
        When Clico no botao excluir o produto
        Then O produto deixara de existir
        And Eu sou redirecionado para a pagina com a lista de produtos cadastrados