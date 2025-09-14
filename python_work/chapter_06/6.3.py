glossario = {
    'variável': 'Um espaço nomeado na memória usado para armazenar valores.',
    'lista': 'Uma coleção ordenada de elementos que pode ser alterada.',
    'dicionário': 'Estrutura de dados que armazena pares chave-valor.',
    'condicional': 'Instrução que executa código apenas se uma condição for verdadeira.',
    'laço': 'Estrutura usada para repetir um bloco de código várias vezes.'
}

for palavra, significado in glossario.items():
    print(f'{palavra.title()}:\n {significado}')