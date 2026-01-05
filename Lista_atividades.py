import datetime

tarefas = []                                                            # teste 2.5 

def mostrar_menu():
    print("\n=== ORGANIZADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa():
    nome = input("Nome da tarefa (ex: Estudo, Sono): ")
    horario = input("Horário (opcional, ex: 20:00): ")
    tarefas.append({"nome": nome, "horario": horario})
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def ver_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nSuas tarefas:")
    for i, tarefa in enumerate(tarefas):
        horario = f" às {tarefa['horario']}" if tarefa['horario'] else ""
        print(f"{i+1}. {tarefa['nome']}{horario}")

def remover_tarefa():
    ver_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa para remover: ")) - 1
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida['nome']}' removida com sucesso!")
        except (ValueError, IndexError):
            print("Número inválido.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_tarefa()
    elif opcao == '2':
        ver_tarefas()
    elif opcao == '3':
        remover_tarefa()
    elif opcao == '4':
        print("Saindo... Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
