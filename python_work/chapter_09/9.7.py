from user import User

class Admin(User):
    """Representa um administrador, um tipo especial de usuário."""
    
    def __init__(self, first_name, last_name):
        """
        Inicializa os atributos da classe pai (User)
        e depois os atributos específicos do Admin.
        """
        # Inicializa a classe pai
        super().__init__(first_name, last_name)
        
        # Adicione um atributo 'privileges'
        self.privileges = [
            "can add post", 
            "can delete post", 
            "can ban user"
            ]
    
    def show_privileges(self):
        """Exibe a lista de privilégios do administrador."""
        print(f"\nPrivilégios para o Admin {self.first_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
   
# Este código só roda quando você executa este arquivo diretamente
if __name__ == "__main__":
    # Crie uma instância Admin
    admin_user = Admin("Livia", "Admin")
    # Chame o método
    admin_user.show_privileges()