#Feature: Gerencimento de Funcionario
  
#    Background: Em todos os testes o usuário deve estar logado.
#        Given Eu sou um usuario logado
      
#    Scenario: Funcionario cadastrado com sucesso
#        Given Eu estou na pagina de cadastrado de funcionario
#        And Eu informo o primeiro e segundo nome, usuario, email e password
#        When Eu clico no botao cadastrar o funcionario
#        Then Eu sou redirecionado para a pagina com a lista de funcionarios cadastrados
        
#        Given Estou na pagina de lista de funcionarios
#        And Eu clico no botao vizualizar dados para finalizar o cadastro
#        And Eu informo o tipo do funcionario, cpf, rg, ctps e salario
#        When Eu clico no botao editar dados do funcionario
#        Then Eu sou redirecionado para a pagina com a lista de funcionarios cadastrados
#        And O funcionario deve estar devidamente cadastrado
    
#    Scenario: Funcionario editado com sucesso
#        Given Estou na pagina de lista de funcionarios
#        And Seleciono o botao vizualizar acesso de um funcionario
#        And Sou redirecionado para a pagina com os dados do funcionario ja preenchidos
#        And Preencho o campo primeiro nome com um novo valor
#        When Clico no botao editar o funcionario
#        Then Eu sou redirecionado para a pagina com a lista de funcionarios cadastrados
    
#    Scenario: Funcionario excluido com sucesso
#        Given Estou na pagina de lista de funcionarios
#        When Clico no botao excluir o funcionario
#        Then O funcionario deixara de existir
#        And Eu sou redirecionado para a pagina com a lista de funcionarios cadastrados