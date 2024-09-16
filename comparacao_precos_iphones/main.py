from manipulacao_planilhas import (
    create_sheet, adicionar_novo_modelo, atualizar_preco, 
    excluir_modelo, filtrar_por_preco, salvar_arquivo
)

if __name__ == "__main__":
    # Cria o workbook e a planilha
    book = create_sheet()  # Cria o Workbook

    # Verifica se a planilha 'Iphones' já existe, e cria se não existir
    if 'Iphones' not in book.sheetnames:
        book.create_sheet('Iphones')  # Cria a planilha 'Iphones'
    
    iphones_page = book['Iphones']  # Acessa a planilha criada

    # Adiciona os cabeçalhos e algumas linhas de exemplo
    iphones_page.append(['Índice', 'Tipo', 'Preço Loja 1', 'Preço Loja 2', 'Preço Loja 3'])
    iphones_page.append(['1', 'Iphone 15', 'R$5.200,00', 'R$6.600,00', 'R$7.950,00'])
    iphones_page.append(['2', 'Iphone 12', 'R$2.800,00', 'R$3.400,00', 'R$3.560,00'])
    iphones_page.append(['3', 'Iphone 13', 'R$4.000,00', 'R$4.200,00', 'R$4.350,00'])

    # Salva o arquivo com o nome desejado
    salvar_arquivo(book, 'comparacao_precos_iphones_atualizado.xlsx')
