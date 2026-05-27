# IA BANCARIA ----- CLASIFICADO DE CREDITO
#PESO
wIngresos = 0.8
wAhorros = 0.4
# BIAS LAS PILOTICAS DE EXIGENTES DEL BANCO
#Un bias negativo hace que el banco sea exigente
#Un bias positivo hace que el banco sea flexible
bias = -0.7
umbral = 1.0


clientes = [
    ["Paloma", 1.5, 1.0],
    ["Edwin", 1.5, 0.5],
    ["Chistian", 0.5, 0.2]
    ]
print(f"{'CLIENTE':<10} | {'SUMA + BIAS':<12} | {'ESTADO'}")

for c in clientes:
    nombre, x1, x2 = c

    suma_ponderada = (x1 * wIngresos) + (x2 * wAhorros) + bias

    if suma_ponderada >= umbral:
        decision = "Credito aprobado"

    else:
        decision = "Credito rechazado"

    print(f"{nombre:<10} | {suma_ponderada:^12.1f} | {decision}")

print("-" * 40)
print(f"Configuracion actual del bias: {bias}")
