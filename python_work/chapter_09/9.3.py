class User:
    """Uma classe simples para visualizar um perfil de usuário."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Exibe o nome e sobrenome do usuário."""
        print(f"Nome: {self.first_name}\nSobrenome: {self.last_name}")

    def greet_user(self):
        """Exibe uma saudação personalizada ao usuário."""
        print(f"Olá, {self.first_name}! Bem vindo!")
  
# Criando um objeto (instância) da classe
user1 = User("Livia", "Maria")
user2 = User("Marcos", "Nog")
user3 = User("Lais", "Silva")

# Chamando métodos
user1.describe_user() 
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()