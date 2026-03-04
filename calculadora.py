print("=== CALCULADORA SIMPLES ===")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação: ")

if operacao == "1":
    print("Resultado:", num1 + num2)
elif operacao == "2":
    print("Resultado:", num1 - num2)
elif operacao == "3":
    print("Resultado:", num1 * num2)
elif operacao == "4":
    print("Resultado:", num1 / num2)
else:
    print("Operação inválida")
