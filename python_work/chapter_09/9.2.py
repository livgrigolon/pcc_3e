class Restaurant:
    """Uma classe simples para modelar um restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Exibe o nome e o tipo de culinária do restaurante."""
        print(f"Nome do restaurante: {self.restaurant_name}\nTipo de culinária: {self.cuisine_type}")

    def open_restaurant(self):
        """Exibe uma mensagem indicando que o restaurante está aberto."""
        print(f"O restaurante {self.restaurant_name} está aberto!")
  
# 4. Criando um objeto (instância) da classe
restaurant1 = Restaurant("Ziyad", "Arabic")
restaurant2 = Restaurant("La Petite Brasserie", "French")
restaurant3 = Restaurant("De la Rua", "Mexican")

# 6. Chamando métodos
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()