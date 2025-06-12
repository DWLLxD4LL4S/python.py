import dns.resolver

res = dns.resolver.Resolver()
arquivo = open("caminho da wordlist", "r")
subdominios = arquivo.read().splitlines()

alvo = ""

for subdominio in subdominios:
        try:
                sub_alvo = subdominio + "." + alvo
                resultado = res.resolve(sub_alvo, "A")
                for info in resultado:
                        print(sub_alvo, "->", info)
        except:
                pass
