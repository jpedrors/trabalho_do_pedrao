"""
DIGITE A SENHA CORRETA
"""
senha_correta = "turminha2B" # essa é a senha correta

while True: 
    senha = input("Digite a senha: ") 
    if senha == senha_correta: # se a senha for digitada certa 
        print("Senha correta! Acesso concedido.")  # apareçe senha correta
        break
    else: # caso o contrario 
        print("Senha incorreta! Tente novamente.") # senha correta