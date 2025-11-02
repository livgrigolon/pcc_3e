class User:
    """Uma classe simples para visualizar um perfil de usuário."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    # Adiciona o atributo 'login_attempts' com valor default 0
        self.login_attempts = 0

    def describe_user(self):
        """Exibe o nome e sobrenome do usuário."""
        print(f"Nome: {self.first_name}\nSobrenome: {self.last_name}")

    def greet_user(self):
        """Exibe uma saudação personalizada ao usuário."""
        print(f"Olá, {self.first_name}! Bem vindo!")

    def increment_login_attempts(self):
        """Incrementa o valor de login_attempts em 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Redefine o valor de login_attempts para 0."""
        self.login_attempts = 0
  
# Este bloco 'if' faz com que o código abaixo
# SÓ execute quando você rodar 'python user.py'
if __name__ == "__main__":
    # Criando um objeto (instância) da classe
    user1 = User("Livia", "Maria")
    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()

    # Exiba o valor para verificar que foi incrementado
    print(f"Tentativas após 3 incrementos: {user1.login_attempts}")

    # Chame reset_login_attempts()
    print("Resetando tentativas...")
    user1.reset_login_attempts()

    # Exiba login_attempts novamente para verificar o reset
    print(f"Tentativas após o reset: {user1.login_attempts}")