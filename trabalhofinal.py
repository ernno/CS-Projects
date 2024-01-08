class Tarefa:
    id = None
    descricao = None
    tempo_l = None
    sit = 'Ativa'

def existe_id_tarefa(lista_tarefas, id):
    for i in range(len(lista_tarefas)):
        if id == lista_tarefas[i].id:
            return True

def adiciona_tarefa(lista_tarefas):
    tarefa = Tarefa()
    tarefa.id = input("Digite o identificador da tarefa: ")
    tarefa.descricao = input("Digite a descrição da tarefa: ")
    tarefa.tempo_l = input("Defina um tempo limite (em horas) para a conclusão da tarefa: ")

    if not existe_id_tarefa(lista_tarefas, tarefa.id):
        lista_tarefas.append(tarefa)
    else:
        print("Uma tarefa com o mesmo identificador já existe. Não foi adicionada uma nova tarefa.")

def visualiza_tarefas_a(lista_tarefas):
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].sit == 'Ativa':
            print("\n Identificador: ", lista_tarefas[i].id, "\n Descrição: ", lista_tarefas[i].descricao, "\n Tempo Limite: ", lista_tarefas[i].tempo_l, "horas \n situação: ", lista_tarefas[i].sit)

def visualiza_tarefas_c(lista_tarefas):
    for i in range(len(lista_tarefas)):
        if lista_tarefas[i].sit == 'Concluída':
            print("\n Identificador: ", lista_tarefas[i].id, "\n Descrição: ", lista_tarefas[i].descricao, "\n Tempo Limite: ", lista_tarefas[i].tempo_l, "horas \n situação: ", lista_tarefas[i].sit)

def atualiza_tarefas(lista_tarefas):
    id_tracker = input("Digite o identificador da tarefa a ser atualizada: ")
    for i in range(len(lista_tarefas)):
        if id_tracker == lista_tarefas[i].id:
            new_d = input("Digite a nova descrição da tarefa: ")
            new_tl = input("Digite o novo tempo limite da tarefa: ")
            lista_tarefas[i].descricao = new_d
            lista_tarefas[i].tempo_l = new_tl

def conclui_tarefa(lista_tarefas):
    id_tracker = input("Digite o identificador da tarefa a ser concluída: ")
    for i in range(len(lista_tarefas)):
        if id_tracker == lista_tarefas[i].id:
            lista_tarefas[i].sit = 'Concluída'

def exclui_tarefas(lista_tarefas):
    id_tracker = input("Digite o identificador da tarefa a ser excluída: ")
    for i in range(len(lista_tarefas)):
        if id_tracker == lista_tarefas[i].id:
            del lista_tarefas[i]
            break

def menu_principal():
    lista_tarefas = []

    while True:
        print("\n*** Sistema de Gerenciamento de Tarefas ***")
        print("Digite a opção desejada:")
        print("\t0 - Sair")
        print("\t1 - Adicionar tarefa")
        print("\t2 - Visualizar todas as tarefas")
        print("\t3 - Visualizar apenas tarefas ativas")
        print("\t4 - Visualizar apenas tarefas conclídas")
        print("\t5 - Atualizar dados de uma tarefa")
        print("\t6 - Concluir tarefa")
        print("\t7 - Excluir tarefa")

        opcao = input()

        if opcao == "0":
            break

        if opcao == "1":
            adiciona_tarefa(lista_tarefas)
        elif opcao == "2":
            visualiza_tarefas_a(lista_tarefas)
            visualiza_tarefas_c(lista_tarefas)
        elif opcao == "3":
            visualiza_tarefas_a(lista_tarefas)
        elif opcao == "4":
            visualiza_tarefas_c(lista_tarefas)
        elif opcao == "5":
            atualiza_tarefas(lista_tarefas)
        elif opcao == "6":
            conclui_tarefa(lista_tarefas)
        elif opcao == "7":
            exclui_tarefas(lista_tarefas)
        else:
            print("Opção inválida!")

menu_principal()