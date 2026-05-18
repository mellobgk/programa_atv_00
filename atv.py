print ("BEM VINDO AO PROGRAMA!!!")

while True: #coloco while pois não sei a quantidade de vezes que o úsuario vai repetir o programa
    print("\n")
    op1 = print ("\nCrie um lista de 10 números inteiros e descubra o maior e menor valor (1)")
    op2 = print ("\nCrie uma lista com 15 números inteiros pares e impares (2)")
    op3 = print ("\nLista interativa com 8 números inteiros (3)")
    op4 = print ("\nLista com remoção de elementos (4)")
    op5 = print ("\nLista com 20 números inteiros (5)")
    op6 = print ("\nDuas listas com 5 números inteiros (6)")
    op7 = print ("\nCadastros de produtos (7)")
    op8 = print ("\nLista com 12 números inteiros (8)")
    op9 = print ("\nEncerrar o programa (9)")

    op = int(input("\nEscolha uma opção: "))
#quetão 1
    if op == 1: 
        lista = [] #vai criar uma lista vazia

        for i in range (10): #cria um laço de repetição de 10 números
            num = int(input("digite um número inteiro: "))
            lista.append(num) #adiciona o número digitado na lista
        
        print("\n =========RESULTADO=========")
        print(f"\n A lista criada é: {lista}")
        print(f"\nO maior número da lista é: {max(lista)}")
        print(f"\nO menor número da lista é: {min(lista)}")
#questão 2
    elif op == 2: 
        lista = [] #vai criar uma lista vazia 
        for i in range (15): #cria um laço de repetição de 15 números
            num = int(input("Digite um número inteiro: "))
            lista.append(num) #adiciona o número digitado na lista
            
        listapar = [numero for numero in lista if numero % 2 == 0] #cria uma nova lista com os números pares
        listaimpar = [numero for numero in lista if numero % 2 != 0] #cria uma nova lista com os números impares
        print("\n =========RESULTADO=========")
        print(f"\n A lista criada é: {lista}")
        print(f"\nOs números pares são: {listapar}")
        print(f"\nOs números impares são: {listaimpar}")
#questão 3
    elif op == 3:
        lista = [] #vai criar uma lista vazia
        for i in range (8): #vai criar um laço de repetição de 8 números
            num = int(input("Digite um número inteiro: "))
            lista.append(num)

        numpro = int(input("Digite um número para procurar na lista: ")) #vai pedir pro usúario procurar um número na lista
        if numpro in lista:
            print(f"{numpro} está presente na lista!!")
        else:
            print(f"{numpro} não está presente na lista!!")
#quetão 4
    elif op == 4:
        lista = [] #vai criar uma lista vazia
        for i in range (10): #vai criar um laço de repetição de 10 números
            num = int(input("Digite um número inteiro: "))
            lista.append(num)
        print(f"\n A lista criada é {lista}")
        
        numrem = int(input("\nDigite um número para remover da lista: ")) #vai pedir para o usúario remover um número
        if numrem in lista: #vai ver se o numero está a lista e se estiver ele remove o número da lista
            lista.remove(numrem) #remove o número da lista
            print(f"\n {numrem} foi removido da lista!!")
            print(f"\n A lista atualizada é: {lista}")
        else:
            print(f"\n O número {numrem} não está na lista!!")
#questão 5
    elif op == 5:
        lista = [] #cria uma lista vazia
        positivos = 0 #variavel para contar quantidade de números positivos
        negativos = 0
        zeros = 0 
        for i in range (20): #cria um laço de repetição de 20 números
            num = int(input("\n Digite um número inteiro: "))
            lista.append(num)
            if num > 0: #condição para contar quantidade de números positivos, negativos e zeros
                positivos += 1
            elif num < 0: 
                negativos += 1
            else:
                zeros += 1
        print("\n =========RESULTADO=========")
        print(f"\n A lista criada é: {lista}")
        print(f"\n Quantidade de números positivos: {positivos}")
        print(f"\n Quantidade de núemeros negativos: {negativos}")
        print(f"\n Quantidade de zeros: {zeros}")
#questão 6
    elif op == 6:
        lista1 = [] #cria lista vazia para a primeira lista
        lista2 = [] #cria lista vazia para a segunda lista
        #primeira lista
        for i in range (5): #cria um laço de repetição de 5 números para a primeira lista
            num1 = int(input("\n Digite um número inteiro para a primeira lista: "))
            lista1.append(num1)
        #segunda lista
        for i in range (5): #cria um laço de repetição de 5 números para a segunda lista
            num2 = int(input("\n Digite um número inteiro para a segunda lista: "))
            lista2.append(num2)
        print("\n =========RESULTADO=========")
        
        igauis = [num for num in lista1 if num in lista2] #cria uma nova lista para os números iguais nas duas listas
        print(f"\n Os números igauis nas duas listas são: {igauis}")

        exclusivo1 = [num for num in lista1 if num not in lista2] #cria uma nova lista para os números exclusivos da primeira lista
        print(f"\n Os números excluvivos da primeira lista são: {exclusivo1}")

        exclusivo2 = [num for num in lista2 if num not in lista1] #cria uma nova lista para os números exclusivos da segunda lista
        print(f"\n Os números exclusivos da segunda lista são: {exclusivo2}")
#questão 7
    elif op == 7:
        lista_produtos = []
        lista_precos = []
        lista_quantidades = []
        for i in range (5):
            produto = input("\n Digite o nome do produto: ")
            preco = float(input("\n Digite o preço do produto: "))
            quantidade = int(input("\n Digite a quantidade do produto no estoque: "))
            lista_produtos.append(produto)
            lista_precos.append(preco)
            lista_quantidades.append(quantidade)
            
        print("\n =========RESULTADO=========")
        #estoque baixo
        estoque_baixo = [lista_produtos[i] for i in range(len(lista_produtos))if lista_quantidades[i] < 10] #cria uma nova lista para os produtos com estoque menor que 10, ele vai percorrer a lista de produtos e dizer o indice do produto com estoque baixo para mostrar o nome do produto
        print(f"\n Os produtos com estoque baixo são: {estoque_baixo}")
        #maior preço
        maior_preco = max(lista_precos) #vai encotrar o maior valor da lista
        indice_maior_preco = lista_precos.index(maior_preco) #aqui ele vai encotrar o índice do maior valor
        print(f"\n O produto com maior preço é: {lista_produtos[indice_maior_preco]}") #ele pega o mesmo valor para ver o nome do produto
        print(f"\n O preço do produto mais caro é: R${maior_preco}")
#questão 8 
    elif op == 8:
        lista = [] #cria lista vazia
        par = 0 #variavel para contar quantidade de números pares
        impar = 0
        for i in range (12): #cria um laço de repetição de 12 números
            num = int(input("\n Digite um número inteiro: "))
            lista.append(num)
            if num % 2 == 0: #verifica se o número é par ou impar e conta a quantidade de cada um
                par += 1
            else: 
                impar += 1
        print("\n =========RESULTADO=========")
        print(f"\n A lista em ordem crescente é: {sorted(lista)}") #a função sorted() vai ordenar a lista em ordem crescente
        print(f"\n A lista em ordem decrescente é: {sorted(lista, reverse=True)}") #a função sorted() com parametro reverse=True vai ordenar alista em ordem decrrescente
        print(f"\n Quantidade de números pares: {par}")
        print(f"\n Quantidade de números ímpares: {impar}")

    elif op == 9:
        print("\n Programa encerrado!!!")
        break #comando para encerrar o laço while 