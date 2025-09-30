def make_shirt(size = 'G', text = 'Eu amo Python'):
    print(f'A camiseta escolhida é tamanho {size} com a frase "{text}".')

# 1 - camiseta grande com a frase padrão
make_shirt()

# 2 - camiseta média com a frase padrão
make_shirt("M")

# 3 - camiseta de qualquer tamanho com frase diferente
make_shirt("P", "Keep calm and code in Python")