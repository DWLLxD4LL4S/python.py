import socket

# Loop de 1 a 99999
for port in range(1, 100000):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex(("dominio.com", port))  # substitua "dominio.com" pelo IP ou domínio desejado
        if code == 0:
            print(port, "OPEN")
        client.close()
    except KeyboardInterrupt:
        print("\nScan interrompido pelo usuário.")
        break
    except Exception as e:
        pass  # opcional: print(f"Erro na porta {port}: {e}")
