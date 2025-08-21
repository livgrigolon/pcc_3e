idiomas = ['Português', 'Inglês', 'Espanhol', 'Italiano', 'Francês']

# .append() → adiciona um elemento no final da lista
idiomas.append('Alemão')
print(idiomas)

# .insert() → insere um elemento no índice indicado (nesse caso, no início)
idiomas.insert(0, 'Mandarim')
print(idiomas)

# .pop() → remove e retorna o último elemento (ou um índice específico se passar argumento)
idiomas.pop()
print(idiomas)

# del → deleta o elemento da posição indicada (nesse caso, o primeiro da lista)
del idiomas[0]
print(idiomas)

# .remove() → remove o primeiro elemento com o valor especificado
idiomas.remove('Inglês')
print(idiomas)

# .sort() → ordena a lista em ordem alfabética (ou crescente, no caso de números)
idiomas.sort()
print(idiomas)

# .sort(reverse=True) → ordena a lista em ordem decrescente
idiomas.sort(reverse=True)
print(idiomas)

# sorted() → retorna uma NOVA lista ordenada em ordem crescente, sem alterar a original
idiomas_sorted = sorted(idiomas)
print(idiomas_sorted)

# sorted(x, reverse=True) → retorna uma NOVA lista ordenada em ordem decrescente, sem alterar a original
idiomas_sorted = sorted(idiomas, reverse=True)
print(idiomas_sorted)

# .reverse() → inverte a ordem atual da lista (não é ordenação, apenas espelha)
idiomas.reverse()
print(idiomas)

# len() → retorna o número de elementos da lista
print(len(idiomas))
