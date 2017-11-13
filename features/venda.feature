Feature: Efetuar Venda
  
  Background: Login Efetuado com sucesso
  
    Scenario: Venda de bolao efetuada com sucesso

        Given Eu estou na pagina principal
        And Eu possuo tipo de funcionario cadastrado no sistema
        And Eu possuo funcionario cadastrado no sistema
        And Eu possuo guiche cadastrado no sistema
        And Eu possuo modalidade cadastrado no sistema
        And Eu possuo produto cadastrado no sistema
        And Eu possuo tipo de bolao cadastrado no sistema
        And Eu possuo bolao cadastrado no sistema
        When Eu clico na aba vender
        Then Sou redirecionado para a pagina de vendas
        And Carrego os boloes disponiveis na tela
        
        Given Eu estou na pagina de vendas
        When Eu clico no botao vender
        Then A venda e efetuada e armazenada