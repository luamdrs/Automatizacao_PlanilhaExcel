import openpyxl

# Carregando arquivo
book = openpyxl.load_workbook('Comparacao_precos_iphones.xlsx')

# Selecionando uma página
iphones_page = book['Iphones']

# Imprimindo os dados de cada linha
for rows in iphones_page.iter_rows(min_row=2, max_row=4):
    print(
        f'{rows[0].value} ~ '
        f'{rows[1].value} ~ '
        f'{rows[2].value} ~ '
        f'{rows[3].value} ~ '
        f'{rows[4].value}'
    )

