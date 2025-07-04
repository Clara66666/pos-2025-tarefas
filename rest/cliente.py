import users

def menu():
    print("\nMenu de Usuários")
    print("1 - Listar usuários")
    print("2 - Ver usuário")
    print("3 - Criar usuário")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("6 - Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            try:
                print("Antes da chamada users.list()")  
                lista = users.list()
                print("DEBUG: lista recebida =", lista)  
                for user in lista:
                    print(f"{user['id']}: {user['name']}")
            except Exception as e:
                print("Erro ao listar usuários:", e)
                
        elif escolha == "2":
            uid = input("Digite o ID do usuário: ").strip()
            if not uid.isdigit():
                print("ID inválido.")
                continue
            try:
                user = users.read(uid)
                print(user)
            except Exception as e:
                print("Erro:", e)
                
        elif escolha == "3":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            dados = {"name": nome, "email": email}
            try:
                user = users.create(dados)
                print("Criado:", user)
            except Exception as e:
                print("Erro ao criar usuário:", e)
            
        elif escolha == "4":
            uid = input("ID do usuário para atualizar: ").strip()
            if not uid.isdigit():
                print("ID inválido.")
                continue
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            dados = {"name": nome, "email": email}
            try:
                user = users.update(uid, dados)
                print("Atualizado:", user)
            except Exception as e:
                print("Erro:", e)
                
        elif escolha == "5":
            uid = input("ID do usuário para deletar: ").strip()
            if not uid.isdigit():
                print("ID inválido.")
                continue
            try:
                res = users.delete(uid)
                print(res)
            except Exception as e:
                print("Erro:", e)
                
        elif escolha == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()