#Feature: Gerencimento de Guiche
  
#    Background: Em todos os testes o usuário deve estar logado.
#        Given Eu sou um usuario logado
      
#    Scenario: Guiche cadastrado com sucesso
#        Given Eu estou na pagina de cadastrado de guiche
#        And Eu informo um numero do guiche ainda nao cadastrado
#        And Eu informo a descricao do guiche
#        And Eu informo um codigoCEF do guiche ainda nao cadastrado
#        When Eu clico no botao cadastrar o guiche
#        Then Eu sou redirecionado para a pagina com a lista de guiches cadastrados
#        And O guiche deve estar devidamente cadastrado
    
#    Scenario: Guiche editado com sucesso
#        Given Estou na pagina de lista de guiches
#        And Seleciono o botao editar de um guiche
#        And Sou redirecionado para a pagina com os dados do guiche ja preenchidos
#        And Preencho o campo descricao com um novo nome
#        When Clico no botao editar o guiche
#        Then Eu sou redirecionado para a pagina com a lista de guiches cadastrados
    
#    Scenario: Guiche excluido com sucesso
#        Given Estou na pagina de lista de guiches
#        When Clico no botao excluir o guiche
#        Then O guiche deixara de existir
#        And Eu sou redirecionado para a pagina com a lista de guiches cadastrados