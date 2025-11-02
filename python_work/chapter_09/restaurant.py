# 1. O Construtor (Método __init__)
    # Este método é chamado automaticamente quando você cria um novo objeto (instância) da classe.
    # 'self' se refere à própria instância do objeto.

class Restaurant:
    """Uma classe simples para modelar um restaurante."""
    # 2. Atributos (Variáveis da instância)
    # São as características ou dados que o objeto vai armazenar.
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos restaurant_name e cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # 3. Métodos (Funções da instância)
    # São as ações ou comportamentos que o objeto pode realizar.
    def describe_restaurant(self):
        """Exibe o nome e o tipo de culinária do restaurante."""
        # Este método pode acessar os atributos da instância usando 'self'.
        print(f"Nome do restaurante: {self.restaurant_name}\nTipo de culinária: {self.cuisine_type}")

    def open_restaurant(self):
        """Exibe uma mensagem indicando que o restaurante está aberto."""
        print(f"O restaurante {self.restaurant_name} está aberto!")
  
# 4. Criando um objeto (instância) da classe
# Você "chama" a classe como se fosse uma função, passando os argumentos para o __init__.
restaurant = Restaurant("Ziyad", "Arabic")

# 5. Acessando atributos
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# 6. Chamando métodos
restaurant.describe_restaurant()
restaurant.open_restaurant()