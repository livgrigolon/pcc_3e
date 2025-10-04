def itens_sanduiche(*itens): # Recebe quantos argumentos quiser
    """Mostra o resumo do sanduíche pedido."""
    print("\nFazendo um sanduíche com os seguintes ingredientes:")
    for item in itens:
        print(f"- {item.title()}")

itens_sanduiche('queijo')
itens_sanduiche('queijo', 'presunto')
itens_sanduiche('queijo', 'presunto', 'tomate')
