def parse_expression(fun):
    # Substitui 'x^n' por 'x**n' para n de 1 a 9
    corrected_expression_str = fun
    for i in range(1, 9):
        corrected_expression_str = corrected_expression_str.replace(f'x^{i}', f'x**{i}')

    return corrected_expression_str

def calcular(funcao_composta, x):
    resultado = eval(funcao_composta)
    return resultado

# Exemplo de uso:
F = input("Digite a sua função f(x) na forma: Usando a*x para representar a x e x^n para representar x elevado a n:")
F = parse_expression(F)

G = input("Digite a sua função g(x) na forma: Usando a*x para representar a x e x^n para representar x elevado a n:")
G = parse_expression(G)
#Variáveis para não zerar
composed_function = 0
funcao_composta = 0

while True:
    qual_utilizar = input("Digite 1 para (g ° f), 2 para (g ° g), 3 para (f ° f), 4 para (f ° g) ou 0 para sair: ")

    if qual_utilizar == '0':
        break
    elif qual_utilizar == '1':
        # Composição de G e F
        funcao_composta = f"{G.replace('x', f'({F})')}"
        x = float(input("Digite o valor de x para calcular a função composta: "))
        resultado = calcular(funcao_composta, x)
        print(f"O resultado da função composta é: {resultado}")
    elif qual_utilizar == '2':
        # Composição de G e G
        funcao_composta = f"{G.replace('x', f'({G})')}"
        x = float(input("Digite o valor de x para calcular a função composta: "))
        resultado = calcular(funcao_composta, x)
        print(f"O resultado da função composta é: {resultado}")
    elif qual_utilizar == '3':
        # Composição de F e F
        funcao_composta = f"{F.replace('x', f'({F})')}"
        x = float(input("Digite o valor de x para calcular a função composta: "))
        resultado = calcular(funcao_composta, x)
        print(f"O resultado da função composta é: {resultado}")
    elif qual_utilizar == '4':
        # Composição de F e G
        funcao_composta = f"{F.replace('x', f'({G})')}"
        x = float(input("Digite o valor de x para calcular a função composta: "))
        resultado = calcular(funcao_composta, x)
        print(f"O resultado da função composta é: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")

    # Exibe a função composta
    print(f"A função composta é: {funcao_composta}")

print("Obrigado por utilizar o programa.\n Feito por Bryan e Ricardo")
