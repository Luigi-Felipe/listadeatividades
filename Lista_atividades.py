from datetime import datetime

tarefas = []

DIAS_SEMANA = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
]


def mostrar_menu():
  print("\n=== ORGANIZADOR DE TAREFAS ===")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Alternar status (Concluída/Pendente)")
  print("4. Remover tarefa")
  print("5. Sair")


def adicionar_tarefa():
  nome = input("Nome da tarefa (ex: Estudo, Sono): ").strip()
  if not nome:
    print("O nome da tarefa não pode estar vazio.")
    return

  data_str = input("Data (opcional, formato DD/MM/AAAA): ").strip()
  data_formatada = ""
  dia_semana = ""

  if data_str:
    try:
      data_obj = datetime.strptime(data_str, "%d/%m/%Y")
      data_formatada = data_obj.strftime("%d/%m/%Y")
      dia_semana = DIAS_SEMANA[data_obj.weekday()]
    except ValueError:
      print("Data inválida! Formato correto: DD/MM/AAAA. Salva sem data.")

  horario = input("Horário (opcional, ex: 20:00): ").strip()

  tarefas.append({
      "nome": nome,
      "data": data_formatada,
      "dia_semana": dia_semana,
      "horario": horario,
      "concluida": False,
  })
  print(f"Tarefa '{nome}' adicionada com sucesso!")


def ver_tarefas():
  if not tarefas:
    print("\nNenhuma tarefa cadastrada.")
    return

  print("\nSuas tarefas:")
  for i, tarefa in enumerate(tarefas):
    status = "✓" if tarefa["concluida"] else " "
    data = f" em {tarefa['data']}" if tarefa["data"] else ""
    dia = f" ({tarefa['dia_semana']})" if tarefa["dia_semana"] else ""
    horario = f" às {tarefa['horario']}" if tarefa["horario"] else ""
    print(f"{i+1}. [{status}] {tarefa['nome']}{data}{dia}{horario}")


def alternar_status():
  ver_tarefas()
  if tarefas:
    try:
      indice = (
          int(input("Digite o número da tarefa para alternar o status: ")) - 1
      )
      tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
      estado = "concluída" if tarefas[indice]["concluida"] else "pendente"
      print(f"Tarefa '{tarefas[indice]['nome']}' marcada como {estado}.")
    except (ValueError, IndexError):
      print("Número inválido.")


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
  opcao = input("Escolha uma opção: ").strip()

  if opcao == "1":
    adicionar_tarefa()
  elif opcao == "2":
    ver_tarefas()
  elif opcao == "3":
    alternar_status()
  elif opcao == "4":
    remover_tarefa()
  elif opcao == "5":
    print("Saindo... Até logo!")
    break
  else:
    print("Opção inválida. Tente novamente.")