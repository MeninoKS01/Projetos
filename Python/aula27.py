"""
CONSTANTE = "variáveis" que não vão mudar
Muitas condições do mesmo if (ruim)
    ~quanto mais longe~   <-- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

antes_do_radar_1 = (LOCAL_1 - RADAR_RANGE)
depois_do_radar_1 = (LOCAL_1 + RADAR_RANGE)

carro_pass_radar_1 = local_carro >= antes_do_radar_1 \
    and local_carro <= depois_do_radar_1

carro_multado_radar_1 = carro_pass_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print("Velocidade do carro passou do radar 1")

if carro_pass_radar_1:
    print("O carro passou o radar 1")

if carro_multado_radar_1:
    print("Carro multado em radar 1")