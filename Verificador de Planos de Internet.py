def recomendar_plano(consumo):
    if consumo > 0:
        if consumo <= 10:
            return "Plano Essencial Fibra - 50Mbps"
        elif consumo <= 20:
            return "Plano Prata Fibra - 100Mbps"
        else:
            return "Plano Premium Fibra - 300Mbps"
    else:
        return "\n@@@ Operação falhou! O valor informado é inválido. @@@"

consumo = float(input())
print(recomendar_plano(consumo))
