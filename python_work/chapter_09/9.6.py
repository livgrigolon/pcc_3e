from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Representa uma sorveteria, um tipo específico de restaurante."""

    def __init__(self, restaurant_name, flavors):
        """
        Inicializa os atributos da classe pai (Restaurant).
        Em seguida, inicializa o atributo específico da sorveteria (flavors).
        """
        # A função super() chama o __init__ da classe PAI (Restaurant)
        # Passamos o nome e definimos o cuisine_type como "Sorveteria"
        super().__init__(restaurant_name, "Sorveteria")
        self.flavors = flavors

    # Escreva um método que exiba esses sabores
    def display_flavors(self):
        """Exibe a lista de sabores de sorvete disponíveis."""
        print("\nSabores disponíveis:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# --- TESTANDO A NOVA CLASSE ---
# Crie uma instância a partir de IceCreamStand
sabores_da_casa = ["Chocolate Belga", "Baunilha", "Morango", "Flocos", "Pistache"]
minha_sorveteria = IceCreamStand("Gelato da Praça", sabores_da_casa)

# Chame esse método
minha_sorveteria.display_flavors()
minha_sorveteria.describe_restaurant()
minha_sorveteria.open_restaurant()