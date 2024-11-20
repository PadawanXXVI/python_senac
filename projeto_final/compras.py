import pandas as pd
from fpdf import FPDF

# Função para calcular o total da compra
def calcular_total(carrinho):
    return carrinho['Total'].sum()

# Função para aplicar desconto
def aplicar_desconto(total, desconto):
    return total - (total * (desconto / 100))

# Função para calcular o troco
def calcular_troco(total, pagamento):
    return pagamento - total

# Função para gerar o comprovante em PDF
def gerar_comprovante(carrinho, total, desconto, total_com_desconto, pagamento, troco):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Comprovante de Compra", ln=True, align="C")
    pdf.cell(200, 10, txt="---------------------------", ln=True, align="C")

    for index, row in carrinho.iterrows():
        pdf.cell(200, 10, txt=f"Produto: {row['Produto']} - Quantidade: {row['Quantidade']} - Total: R${row['Total']:.2f}", ln=True)

    pdf.cell(200, 10, txt=f"Total: R${total:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Desconto: {desconto}%", ln=True)
    pdf.cell(200, 10, txt=f"Total com Desconto: R${total_com_desconto:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Pagamento: R${pagamento:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Troco: R${troco:.2f}", ln=True)

    pdf.output("comprovante.pdf")

# Função para adicionar produto ao carrinho (CREATE)
def adicionar_produto(carrinho):
    carrinho = list()
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    total = quantidade * valor_unitario
    novo_produto = {'Produto': produto, 'Quantidade': quantidade, 'Valor Unitário': valor_unitario, 'Total': total}
    carrinho = carrinho.append(novo_produto, ignore_index=True)
    return carrinho

# Função para remover produto do carrinho (DELETE)
def remover_produto(carrinho):
    produto = input("Digite o nome do produto a ser removido: ")
    carrinho = carrinho[carrinho['Produto'] != produto]
    return carrinho

# Função para atualizar produto no carrinho (UPDATE)
def atualizar_produto(carrinho):
    produto = input("Digite o nome do produto a ser atualizado: ")
    if produto in carrinho['Produto'].values:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        novo_valor_unitario = float(input("Digite o novo valor unitário: "))
        carrinho.loc[carrinho['Produto'] == produto, 'Quantidade'] = nova_quantidade
        carrinho.loc[carrinho['Produto'] == produto, 'Valor Unitário'] = novo_valor_unitario
        carrinho.loc[carrinho['Produto'] == produto, 'Total'] = nova_quantidade * novo_valor_unitario
    else:
        print("Produto não encontrado.")
    return carrinho

# Função para exibir o carrinho (READ)
def exibir_carrinho(carrinho):
    print("\nCarrinho de Compras:")
    print(carrinho)
    print("\nTotal: R${:.2f}".format(calcular_total(carrinho)))

# Função para exibir o menu
def exibir_menu():
    print("\n" + "="*35)
    print(f"{'Menu de Compras':^35}")
    print("="*35)
    print(f"1.{'Adicionar produto':>32}")
    print(f"2.{'Remover produto':>32}")
    print(f"3.{'Atualizar produto':>32}")
    print(f"4.{'Exibir carrinho':>32}")
    print(f"5.{'Finalizar compra':>32}")
    print(f"6.{'Sair':>32}")
    print("="*35)

# Função principal
def main():
    produtos = {
        'Produto': [],
        'Quantidade': [],
        'Valor Unitário': []
    }

    carrinho = pd.DataFrame(produtos)
    carrinho['Total'] = carrinho['Quantidade'] * carrinho['Valor Unitário']

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            carrinho = adicionar_produto(carrinho)
        elif escolha == '2':
            carrinho = remover_produto(carrinho)
        elif escolha == '3':
            carrinho = atualizar_produto(carrinho)
        elif escolha == '4':
            exibir_carrinho(carrinho)
        elif escolha == '5':
            exibir_carrinho(carrinho)
            desconto = float(input("Digite o percentual de desconto: "))
            total = calcular_total(carrinho)
            total_com_desconto = aplicar_desconto(total, desconto)
            pagamento = float(input("Digite o valor pago: "))
            troco = calcular_troco(total_com_desconto, pagamento)
            gerar_comprovante(carrinho, total, desconto, total_com_desconto, pagamento, troco)
            print("Compra finalizada. Comprovante gerado em 'comprovante.pdf'.")
            break
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
