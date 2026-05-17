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
        lista = [] 
        positivos = 0
        negativos = 0
        zeros = 0 
        for i in range (20):
            num = int(input("\n Digite um número inteiro: "))
            lista.append(num)
            if num > 0:
                positivos += 1
            elif num < 0: 
                negatvos += 1
            else:
                zeros += 1
        print("\n =========RESULTADO=========")
        print(f"\n A lista criada é: {lista}")
        print(f"\n Quantidade de números positivos: {positivos}")
        print(f"\n Quantidade de núemeros negativos: {negativos}")
        print(f"\n Quantidade de zeros: {zeros}")

        
        
