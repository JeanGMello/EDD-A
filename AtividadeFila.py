import os, heapq
from random import randrange

def menu():
    print("     Pedidios")
    print(" Escolha a operação que deseja realizar:")
    print(" 1)Definir tamanho da fila com prioridades")
    print(" 2)Adicionar novo grupo na fila com prioridades")
    print(" 3)Mostrar próximo grupo aguardando")
    print(" 4)Preparar próxima refeição")
    print(" 5)Entregar refeição")
    print(" 6)Gerar simulação")
    print(" 7)Fechar (exclui todos os registros!)")
    print("")

    escolha = input(" ")
    return escolha.lower()

def  verifica_fila(lista):
    os.system("cls")
    if len(lista) > 0:
        return True
    else:
        print("Fila vazia.")
        return False

def Define_tam(escolha):#1
    if escolha == '6':
        tamanho_fila = randrange(1,9)
        print(" O tamanho da fila foi definido como:",tamanho_fila)
        input(" Pressione enter para continuar...")
    else:
        os.system("cls")
        tamanho_fila = int(input(" Informe o tamanho da fila de pedidos: "))
    return tamanho_fila

def Add_grupo(tamanho_fila, escolha):#2
    if escolha == '6':
        if len(fila_ped) < tamanho_fila:
            qnt = randrange(1,9)
            tempo = randrange(1,9)
            reserva = 'A'+str(randrange(1,9))
            pedido = (qnt,tempo,reserva)
            fila_ped.append(pedido)
            heapq.heapify(fila_ped)
            print(" o grupo foi definido como:",pedido)
            input(" Pressione enter para continuar...")
        else:
            print(" A fila de pedidos esta lotada")
    else:  
        os.system("cls")
        if len(fila_ped) < tamanho_fila:
            qnt = int(input(" Insira a quantidade de pessoas na mesa: "))
            tempo = int(input(" Informe o tempo de preparo: "))
            reserva = input(" Informe o nome da resera: ")
            pedido = (qnt,tempo,reserva)
            fila_ped.append(pedido)
            heapq.heapify(fila_ped)
        else:
            print(" A fila de pedidos esta lotada")

def Mostrar_proximo(fila_ped):#3
    if verifica_fila(fila_ped):
        print(" Próximo pedidio da fila:")
        print(" ",fila_ped[0])

def Preparar(fila_ped,fila_prep):#4
    if verifica_fila(fila_ped):
        item = heapq.heappop(fila_ped)
        tempo_item = int(item[1])
        tempo_prep = tempo_item
        for x in fila_prep:
            tempo_prep = tempo_prep + int(x[1])

        print(" Pedido entrou para preparo:")
        print(" Nome do pedido: ",item[2])
        print(" Tempo de prearo: " ,tempo_prep)
        fila_prep.append(item)

def Entregar(fila_prep):#5
    if  verifica_fila(fila_prep):
        ped_pronto = fila_prep.pop(0)
        print(" O pedido", ped_pronto[2],"esta pronto!")

def Simulacao(fila_ped,fila_prep,escolha):
    os.system("cls")
    tamanho_fila = Define_tam(escolha)
    os.system("cls")
    Add_grupo(tamanho_fila, escolha)
    os.system("cls")
    Mostrar_proximo(fila_ped)
    input(" Pressione enter para continuar...")
    os.system("cls")
    Preparar(fila_ped,fila_prep)
    input(" Pressione enter para continuar...")
    os.system("cls")
    Entregar(fila_prep)

fila_prep = []
fila_ped = []
tamanho_fila = 0
while True:
    os.system("cls")
    escolha = menu()
    if escolha == "1":
        tamanho_fila = Define_tam(escolha)
    elif escolha == "2":
        Add_grupo(tamanho_fila, escolha)
    elif escolha == "3":
        Mostrar_proximo(fila_ped) 
    elif escolha == "4":
        Preparar(fila_ped,fila_prep)
    elif escolha == "5":
        Entregar(fila_prep)
    elif escolha == "6":
        Simulacao(fila_ped,fila_prep,escolha)
    elif escolha == "7":
        os.system("cls")
        print(" --Fim do programa!--")
        print("     Até mais!  :)")
        break
    else:
        print(" Escolha invalida!")
    print("")
    print(" Fila de pedidio: ",fila_ped)
    print(" Fila de preparo: ",fila_prep)
    input(" Pressione enter para continuar...")