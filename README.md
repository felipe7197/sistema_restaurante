🍽️ Sistema de Gerenciamento de Restaurantes utilizando a linguagem Python 
Este projeto é um sistema de gerenciamento de restaurantes baseado em linha de comando (CLI), desenvolvido com a linguagem Python. Ele permite cadastrar, listar e ativar/desativar restaurantes de forma interativa.

📋 Funcionalidades (O que nosso programa faz )



✅ Cadastrar um novo restaurante

✅ Listar restaurantes cadastrados

✅ Alternar o estado (ativo/desativado) de um restaurante

✅ Interface é via terminal

✅ Estrutura organizada com funções reutilizáveis





🧠 Conceitos Aplicados
Estrutura de dados (list, dict)

Encapsulamento de lógica via funções

Limpeza de tela com os.system('cls') (Windows)

Tratamento de exceções (try/except)

Modularidade e boas práticas de organização de código

Docstrings para documentação de funções

Estrutura do Código
O que faz nossas funções do codigo.

exibir_nome_do_programa() Exibe o título estilizado do programa
exibir_opcoes()	                   -  Mostra o menu principal com as opções disponíveis
cadastrar_novo_restaurante()       -  Permite ao usuário cadastrar um novo restaurante
listas_restaurantes()	             -  Lista todos os restaurantes cadastrados, com nome, categoria e status
alternar_estado_do_restaurante()	 -  Alterna o status de um restaurante (ativo ↔ desativado)
escolher_opcao()	                 -  Lê a opção do usuário e direciona para a função correspondente
voltar_menu_principal()	           -  Retorna ao menu após a conclusão de uma operação
finalizar_app()                    -  Encerra a execução do programa
main()	                           -  Função principal que inicia o sistema


Exemplo de Uso
Ao iniciar o programa, você verá um menu como este:
1. Cadastrar restaurante  
2. Listar restaurante  
3. Alternar estado restaurante  
4. Sair  


Cadastrando um Restaurante
Escolha uma opção: 1
Cadastre o nome do novo restaurante: Sabor da Terra
Cadastre a categoria do restaurante Sabor da Terra: Brasileira

Listando Restaurantes
Nome do Restaurante      | Categoria           | Status
- Praça                 | Japonesa            | desativado
- Pizza Suprema         | Pizza               | ativo
- Cantina               | Italiano            | desativado
- Sabor da Terra        | Brasileira          | desativado


🔄 Alternando o Estado

Digite o nome do restaurante que deseja alternar o estado: Sabor da Terra
O restaurante Sabor da Terra foi ativado!


🧰 Requisitos
Python 3.6 ou superior
Sistema operacional Windows (ou adaptar os.system('cls') para clear no Linux/Mac)

▶️ Como Executar
1. Clone este repositório:
git clone https://github.com/seu-usuario/gerenciador-restaurantes.git
cd gerenciador-restaurantes

2. Execute o arquivo Python:
python app.py

📝 Melhorias Futuras (Ideias)
- Salvar e carregar dados de um arquivo (.json ou .csv)
- Interface gráfica com Tkinter ou PyQt
- Filtros de busca por categoria
- Suporte a múltiplos usuários

  👨‍💻 Autor
Seu Nome Aqui – @felipe7197



