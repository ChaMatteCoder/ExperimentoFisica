#Matheus da Silva Fernandes - 12121ECP002 
#Experimento Física (Caixote)

# Constantes
massa = float(input("Digite a massa do caixote (KG): ")) # kg
coef_atrito_estatico = 0.6
coef_atrito_cinetico = 0.4
gravidade = 9.81 # m/s^2

# Força aplicada
forca_aplicada = float(input("Digite a força aplicada em (N): ")) # começa com 0 N
incremento_forca = 1 # incremento de 1 N a cada iteração

Fmin = coef_atrito_estatico * massa * gravidade
print()
print("-----------------------------------------")
print(f"O caixote precisa de pelo menos {Fmin} N, para se mover; portanto:")
print("-----------------------------------------")
print()

# Simulação
while True:
    forca_resultante = forca_aplicada - coef_atrito_estatico * massa * gravidade
    if forca_resultante < 0:
        print(f"O caixote não se moveu com uma força de {forca_aplicada} N.")
        break
    elif forca_resultante >= 0 and forca_resultante < coef_atrito_cinetico * massa * gravidade:
        if forca_aplicada == Fmin: 
            print(f"O caixote começou a se mover EXATAMENTE com uma força {forca_aplicada} N.")
            break
        else:
            print(f"O caixote começou a se mover com uma força de {forca_aplicada} N.")
            break
    
    else:
        forca_aplicada += incremento_forca


