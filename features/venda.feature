Feature: Venda
  
    Scenario: Venda de Produto

        Given Eu possuo usuarios cadastrados no sistema
        And Eu possuo tipo de funcionario cadastrado no sistema
        And Eu possuo funcionario cadastrado no sistema
        And Eu possuo guiche cadastrado no sistema
        And Eu possuo modalidade cadastrado no sistema
        And Eu possuo produto cadastrado no sistema
        And Eu possuo tipo de bolao cadastrado no sistema
        And Eu possuo bolao cadastrado no sistema

        When Eu chamo a funcao efetuar venda
        Then A venda é efetuada
        And A venda é armazenada no sistema