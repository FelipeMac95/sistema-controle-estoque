## -------------------- VARIÁVEIS ---------------------------------------- ##
USUARIO = 'admin'
SENHA = '123'
ROTINA = 1
ESTOQUE = []

## -------------------- FUNÇÃO INCLUIR --------------------------------------##
def incluir():
    COD = int(input('Digite o código do produto:'))
    PRO = input('Digite o nome do produto:')
    QTD = int(input('Digite a quantidade do produto:'))
    PR = float(input('Digite o preço do produto:'))

    CADASTRO = {'CODIGO':COD,'PRODUTO':PRO,'QUANTIDADE':QTD,'PRECO':PR}
    ESTOQUE.append (CADASTRO)

## -------------------- FUNÇÃO MENU -------------------------------------------##
def menu():
    op = int(input('SELECIONE UMA OPÇÃO\n 1.Incluir item\n 2.Pesquisar item\n 3.Alterar item\n 4.Deletar item\n'))
    if op == 1:
        while op == 1:
            incluir()
            op = int(input('Gostaria de adicionar mais algum produto? 1.Sim - 0.Não'))
        print(ESTOQUE)
    elif op == 2:
        print('criar a funcao pesquisar')
    elif op == 3:
        print('criar a funcao alterar')
    elif op == 4:
        print('criar a funcao deletar')
    else:
        print('opção inválida')
        menu() #trocar por um while pra não ocupar memória

while ROTINA == 1:

    ## -------------------  LEITURA CREDENCIAIS DO USUÁRIO    ---------------- ##
    print ('SISTEMA GESTÃO ESTOQUE')
    teste_log = input ('Login:')
    teste_senha = input('Senha:')

    ## -------------------  TESTE CREDENCIAIS DO USUÁRIO    ------------------ ##
    if teste_log == USUARIO and teste_senha == SENHA:
        print('Login realizado com sucesso!')
        menu()
    else:
        print('Usuário ou senha inválidos.')
        ROTINA = int(input('Gostaria de sair? Digite 0 \n Tentar novamente? Digite 1 \n'))
        if ROTINA == 0:
            print('Programa encerrado.')
        else:
            ROTINA = 1





