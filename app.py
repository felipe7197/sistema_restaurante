import os  #importa o os que limpa a tela

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, # cria um dicionario com nome, categoria e se está ativo ou baixo
               {'nome': 'Pizza Suprema','categoria': 'Pizza','ativo': True},
               {'nome': 'Cantina', 'categoria': 'Italiano','ativo':False}]


#essa função abaixo ira aparecer na função principal main() e sempre será ativada
def exibir_nome_do_programa():

      print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)


def exibir_opcoes(): #essa função abaixo ira aparecer na função principal main() e sempre será ativada e mostrara as opções
      '''Essa função define as opções do menu'''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Alternar estado restaurante')
      print('4. Sair\n')

def voltar_menu_principal():
       '''Essa função faz com que se retorno ao menu principal'''
       input("Digite qualquer tecla para voltar!\n ")# ira retornar
       main()

      
def finalizar_app():
      '''Ess função finaliza o app'''
      os.system('cls') #limpa a tela
      print("Finalizando app\n")
      voltar_menu_principal()

def opcao_invalida():
      '''Essa opção é um tratamento de opção invalida que retorna ao menu principal'''
      print("Opção inválida!\n")
      voltar_menu_principal()

def exibir_subtitulo(texto) :
      '''Função responsavel pela exibição de subtitulo e sua formataçãp'''
      os.system('cls')
      linha = '*' * (len(texto))
      print(linha)
      print(texto)
      print(linha)
      print()

def cadastrar_novo_restaurante():
      '''Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:

      - Nome do restaurante
      - Categoria

      Output:

      - Adiciona um novo restaurante  a lista de restaurantes   
      
      '''
      exibir_subtitulo('Cadastro de Novos restaurantes')
      nome_do_restaurante = input('Cadastre o nome do novo restaurante: ')
      categoria = input(f'Cadastre a categoria do restaurante {nome_do_restaurante} : ')
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria,'ativo': False}
      restaurantes.append(dados_do_restaurante)
      print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ')

      voltar_menu_principal()

def listas_restaurantes():
      '''Função qie lista restaurantes cadastrados'''
      exibir_subtitulo('Listando restaurantes')

      print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')

      for restaurante in restaurantes :
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativo' if restaurante['ativo'] else 'desativado'
            print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

      voltar_menu_principal()

def alternar_estado_do_restaurante():
      '''Função que muda o estado do restaurante'''
      exibir_subtitulo('Alternar estado do restaurante')
      nome_restaurante = (input('Digite o nome do restaurante que deseja alternar o estado: '))
      restaurante_encontrado = False

      for restaurante in restaurantes:
          if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado! 'if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado'
            print(mensagem)
      if not restaurante_encontrado:
            print('Restaurante não encontrado! ')
      
      voltar_menu_principal()
            


def escolher_opcao(): 
      '''Função que define a opção escolhida pelo usuario'''
      try: # ele vai tentar executar a condição, caso opção seja invalida ele ira tratar na exceção
            opcao_escolhida = int (input ('Escolha uma opção: '))

            if  opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida  == 2:
                  listas_restaurantes()  
            elif opcao_escolhida  == 3:
                  alternar_estado_do_restaurante()
            elif opcao_escolhida  == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except: # ira ir para a função opção innvalida e orientar o usuario
            opcao_invalida()

def main():
      os.system("cls")
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == "__main__":
      main()