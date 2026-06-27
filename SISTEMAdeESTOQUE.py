## -------------------- VARIÁVEIS ---------------------------------------- ##
USUARIO = 'admin'
SENHA = '123'
ROTINA = 1

while ROTINA == 1:

    ## -------------------  LEITURA CREDENCIAIS DO USUÁRIO    ---------------- ##
    print ('SISTEMA GESTÃO ESTOQUE')
    teste_log = input ('Login:')
    teste_senha = input('Senha:')

    ## -------------------  TESTE CREDENCIAIS DO USUÁRIO    ------------------ ##
    if teste_log == USUARIO and teste_senha == SENHA:
        print('Login realizado com sucesso!')
    else:
        print('Usuário ou senha inválidos.')
        ROTINA = int(input('Gostaria de sair? Digite 0 \n'))
        if ROTINA == 0:
            print('Programa encerrado.')




