print("Salario Bruto...")

salarioBruto = float(input("Digite o salário bruto: R$ "))

if salarioBruto >= 2000:
    desconto = salarioBruto * 0.11
else:
    desconto = salarioBruto * 0.09

salarioFinal = salarioBruto - desconto

print("\n--- Demonstrativo Salarial ---")
print(f"Salário Bruto: R$ {salarioBruto:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Salário Final: R$ {salarioFinal:.2f}")