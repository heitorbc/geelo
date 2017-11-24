Feature: Gerencimento de Bolao
  
    Background: Em todos os testes o usuário deve estar logado.
        Given Eu sou um usuario logado
      
    Scenario: Bolao cadastrado com sucesso
        Given Eu estou na pagina de cadastrado de bolao
        And Eu informo identificador, data do sorteio, hora do sorteio e o tipo do bolao
        When Eu clico no botao cadastrar o bolao
        Then Eu sou redirecionado para a pagina com a lista de boloes cadastrados
        And O bolao deve estar devidamente cadastrado
    
    Scenario: Bolao editado com sucesso
        Given Estou na pagina de lista de boloes
        And Seleciono o botao editar de um bolao
        And Sou redirecionado para a pagina com os dados do bolao ja preenchidos
        And Preencho o campo identificador com um novo valor 
        When Clico no botao editar o bolao
        Then Eu sou redirecionado para a pagina com a lista de boloes cadastrados
    
    Scenario: Bolao excluido com sucesso
        Given Estou na pagina de lista de boloes
        When Clico no botao excluir o bolao
        Then O bolao deixara de existir
        And Eu sou redirecionado para a pagina com a lista de boloes cadastrados