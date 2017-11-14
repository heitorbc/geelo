Feature: Efetuar Venda
  
  
    Background: Em todos os testes o usuário deve estar logado.
      Given Eu sou um usuario logado
  
    Scenario: Venda de bolao efetuada com sucesso
      Given Eu estou na pagina principal
      Given Eu possuo tipo de funcionario cadastrado no sistema
      And Eu possuo funcionario cadastrado no sistema
      And Eu possuo guiche cadastrado no sistema
      And Eu possuo modalidade cadastrado no sistema
      And Eu possuo produto cadastrado no sistema
      And Eu possuo tipo de bolao cadastrado no sistema
      And Eu possuo bolao cadastrado no sistema
      When Eu clico na aba vender
      Then Sou redirecionado para a pagina de vendas
      And Carrego os boloes disponiveis na tela
      
      And  Eu estou na pagina de vendas
      When Eu clico no botao vender
      Then Eu confirmo a venda
      And A venda e efetuada e armazenada