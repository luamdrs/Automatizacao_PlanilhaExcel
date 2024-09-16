# 📌Automação de Planilhas 

## Como automatizar Planilhas com Excel usando o Python


Este projeto utiliza a biblioteca **openpyxl** para manipular planilhas Excel. Ele realiza operações de criação, atualização e exclusão de dados de uma planilha que compara preços de modelos de iPhone. Abaixo estão as principais funcionalidades implementadas:

### Funcionalidades:

1. Criação de Planilha:

A função create_sheet() cria um novo arquivo Excel (Workbook) e adiciona uma planilha chamada Iphones caso ela ainda não exista.

2. Adição de Modelos:

A função adicionar_novo_modelo() permite inserir novas linhas na planilha com informações de um novo modelo de iPhone, incluindo preço de três lojas diferentes.

3. Atualização de Preços:

A função atualizar_preco() permite alterar os preços de um modelo de iPhone específico com base no seu índice.

4. Exclusão de Modelos:

A função excluir_modelo() remove um modelo de iPhone da planilha, utilizando o índice como referência.

5. Filtragem de Modelos por Preço:

A função filtrar_por_preco() permite exibir os modelos de iPhone cujo preço da Loja 1 é menor ou igual a um valor especificado.

5. Salvamento de Planilha:

A função salvar_arquivo() salva o arquivo Excel no diretório local após todas as modificações, garantindo que as alterações realizadas sejam persistentes.

#

*Este projeto também pode ser utilizado para uma análise básica de dados, focada em comparar preços de diferentes modelos de iPhone entre várias lojas.*