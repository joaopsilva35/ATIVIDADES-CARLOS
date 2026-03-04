# Exemplo de estrutura condicional aninhada
#match-case substitui o uso do if-elif-else

dia = input("Digite o dia da semana")

match dia:
    case "segunda":
        print("hoje e segunda-feira.")
    case "terca":
        print("hoje e terca-feira")
    case "quarta": 
        print("hoje e quarta-feira.")
    case "quinta":
        print("hoje e quinta-feira")
    case "sexta":
        print ("hoje e sexta-feira")
    case "sabado" | "domingo":
        print("hoje e fim de samana!")
    case _:
        print("dia invalido.")

print(dia)

print("=== FIM ===")