nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = int(input("Renda mensal: "))
valor_emprestimo = int(input("Valor desejado de empréstimo: "))
parcelas = int(input("Número de parcelas: "))


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    elif parcelas <= 24:
        return 0.10
    else:
        return 0

if parcelas < 3 or parcelas > 24:
    print("Número de parcelas inválido, digite um número entre 3 a 24")
else:
    if idade >= 18 and valor_emprestimo <= renda_mensal * 20:
        print("Cliente Aprovado!")

        taxa = definir_taxa(parcelas)
        print(taxa)


    else:
        print("Reprovado")
