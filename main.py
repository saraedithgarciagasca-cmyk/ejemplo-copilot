from soluciones.salario_semanal import calcularSalario, mostrarSalario, leer_datos

def main():
    horas, pago = leer_datos()
    salario = calcularSalario(horas, pago)
    mostrarSalario(salario) 

if __name__ == "__main__":
    main() 