import random 

#Dicionário para armazenar o estoque de livros
livros = {
    "Às de espadas": {"preço": 60, "estoque": 125},
    "O lado mais sombrio": {"preço": 55, "estoque": 22},
    "Vermelho branco e sangue azul": {"preço": 56, "estoque": 124},
    "Eu e esse meu coração": {"preço": 47, "estoque": 92},
}

#Várivel com o total de vendas
total_vendas = 0.0 

#Função para cadastrar um novo livro
def cadastrar_livro():
    nome = input("Digite o nome do novo livro:")
    preco = float(input("Digite o preço do novo livro:"))
    estoque = int(input("Digite a quantidade de estoque do novo livro: "))
    livros[nome] = {"preço":preco, "'estoque":estoque}
    print(f"Livro {nome} cadastrado com sucesso!\n")

#Função para exibir os livros disponíveis
def livros_disponiveis():
    print("\nLivros disponíveis:")
    for livros, info in livros.items():
     print(f"{livros} - Preço: R${info['preço']:.2f}, Estoque: {info['estoque']} unidades")
    print ()  

#Função para realizar uma venda
def realizar_venda():
    global total_vendas
livro_vendido = input("Digite o nome do livro que deseja comprar:")

#Verifica se o produto está disponivel na loja e no estoque
if livro_vendido in livros:
    quantidade = int(input(f"Digite a quantidade de {livro_vendido}que deseja comprar:"))
    if livros[livro_vendido]["estoque"] >= quantidade:
       valor_venda = quantidade * livros[livro_vendido]["preço"]
       livros[livro_vendido]["estoque"] -= quantidade
       total_vendas += valor_venda
       print(f"Venda realizada: {quantidade}x {livro_vendido} - Total: R${valor_venda: .2f}\n")
    else:
       print(f"Quantidade em estoque insuficiente\n")
else:
   print("Livro não encontrado")

#Função para exibir o total de vendas
   def exibir_vendas():
      print(f"\nTotal de vendas realizadas: R${total_vendas: .2f}\n")

#Função para aplicar uma promoção
def sortear_promocao():
  livro_sorteado = random.choice(list(livros.keys()))
  desconto = random.randint(10, 50) #Quantidade de desconto permitido
  print(f"\nVocê ganhou um desconto de {desconto}% no livro {livro_sorteado}!")

#Menu principal
def menu():
   while True:
      print("===Gerenciamento dos livros na loja===")
      print("1. Cadastrar novo livro")
      print("2. Exibir livros disponíveis")
      print("3. Realizar venda")
      print("4. Exibir total de vendas")
      print("5. Sortear promoção")
      print("6. Sair")

      opcao = input("Por favor escolha uma opção: ")

      if opcao == "1":
        cadastrar_livro()
      elif opcao == "2":
        livros_disponiveis()
      elif opcao == "3":
        realizar_venda()
      elif opcao == "4":
        exibir_vendas()
      elif opcao == "5":
        sortear_promocao()
      elif opcao == "6":
        print("Obrigado por usar o sistema!")
        break
      else:
        print("Por favor escolha uma opção válida")

 #iniciar o sistema
menu()

    

