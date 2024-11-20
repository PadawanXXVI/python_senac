import pandas as pd
from fpdf import FPDF

# Função para adicionar uma tarefa (CREATE)
def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ")
    nova_tarefa = {'Descrição': descricao, 'Prioridade': prioridade}
    tarefas = pd.concat([tarefas, pd.DataFrame([nova_tarefa])], ignore_index=True)
    return tarefas

# Função para exibir todas as tarefas (READ)
def exibir_tarefas(tarefas):
    print("\nTarefas:")
    print(tarefas)

# Função para atualizar uma tarefa (UPDATE)
def atualizar_tarefa(tarefas):
    indice = int(input("Digite o índice da tarefa a ser atualizada: "))
    if 0 <= indice < len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        nova_prioridade = input("Digite a nova prioridade da tarefa (alta, média, baixa): ")
        tarefas.loc[indice, 'Descrição'] = nova_descricao
        tarefas.loc[indice, 'Prioridade'] = nova_prioridade
    else:
        print("Índice inválido.")
    return tarefas

# Função para remover uma tarefa (DELETE)
def remover_tarefa(tarefas):
    indice = int(input("Digite o índice da tarefa a ser removida: "))
    if 0 <= indice < len(tarefas):
        tarefas = tarefas.drop(indice).reset_index(drop=True)
    else:
        print("Índice inválido.")
    return tarefas

# Função para gerar um relatório das tarefas em PDF
def gerar_relatorio(tarefas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Relatório de Tarefas", ln=True, align="C")
    pdf.cell(200, 10, txt="---------------------", ln=True, align="C")
    
    for index, row in tarefas.iterrows():
        pdf.cell(200, 10, txt=f"Tarefa {index}: {row['Descrição']} (Prioridade: {row['Prioridade']})", ln=True)
    
    pdf.output("relatorio_tarefas.pdf")
    print("Relatório gerado em 'relatorio_tarefas.pdf'.")

# Função para exibir o menu
def exibir_menu():
    print("\n" + "="*50)
    print(f"{'Menu de Gerenciamento de Tarefas':^50}")
    print("="*50)
    print(f"{'1. Adicionar tarefa'}")
    print(f"{'2. Exibir tarefas'}")
    print(f"{'3. Atualizar tarefa'}")
    print(f"{'4. Remover tarefa'}")
    print(f"{'5. Gerar relatório'}")
    print(f"{'6. Sair'}")
    print("="*50)

# Função principal
def main():
    tarefas = pd.DataFrame(columns=['Descrição', 'Prioridade'])

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefas = adicionar_tarefa(tarefas)
        elif escolha == '2':
            exibir_tarefas(tarefas)
        elif escolha == '3':
            tarefas = atualizar_tarefa(tarefas)
        elif escolha == '4':
            tarefas = remover_tarefa(tarefas)
        elif escolha == '5':
            gerar_relatorio(tarefas)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
