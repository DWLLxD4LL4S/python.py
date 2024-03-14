import socket

ports = [20,21,22,25,53,80,123,179,443,445,500,587,3306,3389] 

for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
        client.settimout(0.1)
        code = client.connect_ex(("dominio", port))
        if code == 0:
                print(port, "OPEN")


# Comando simples pra testar quais portas o dominio em questao esta rodando.
# Apenas colocar domino desejado em "dominio".
# Diminuir ou aumentar as opcoes de ports e opcional.                                               