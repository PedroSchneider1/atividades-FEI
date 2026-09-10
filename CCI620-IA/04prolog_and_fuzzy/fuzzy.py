import numpy as np
import skfuzzy as fuzz
from skfuzzy import control
import matplotlib.pyplot as plt

# Distância do obstáculo: 0 a 100 metros
distancia = control.Antecedent(
    np.arange(0, 100.1, 0.1),
    'distancia'
)

# Velocidade: 0 a 100 km/h
velocidade = control.Antecedent(
    np.arange(0, 100.1, 0.1),
    'velocidade'
)

# Pressão no freio: 0 a 100%
pressao = control.Consequent(
    np.arange(0, 100.1, 0.1),
    'pressao'
)

# REGRAS PERTINENCIA

# DISTANCIA
distancia['curta'] = fuzz.trimf(
    distancia.universe, [0, 0, 40]
)

distancia['media'] = fuzz.trimf(
    distancia.universe, [20, 50, 80]
)

distancia['longa'] = fuzz.trimf(
    distancia.universe, [60, 100, 100]
)

# VELOCIDADE
velocidade['lenta'] = fuzz.trimf(
    velocidade.universe, [0, 0, 40]
)

velocidade['moderada'] = fuzz.trimf(
    velocidade.universe, [20, 50, 80]
)

velocidade['rapida'] = fuzz.trimf(
    velocidade.universe, [60, 100, 100]
)

# PRESSAO NO FREIO
pressao['suave'] = fuzz.trimf(
    pressao.universe, [0, 0, 40]
)

pressao['media'] = fuzz.trimf(
    pressao.universe, [20, 50, 80]
)

pressao['forte'] = fuzz.trimf(
    pressao.universe, [60, 100, 100]
)

# REGRAS FUZZY

# Distância CURTA
regra1 = control.Rule(
    distancia['curta'] & velocidade['lenta'],
    pressao['media']
)

regra2 = control.Rule(
    distancia['curta'] & velocidade['moderada'],
    pressao['forte']
)

regra3 = control.Rule(
    distancia['curta'] & velocidade['rapida'],
    pressao['forte']
)

# Distância EDIA
regra4 = control.Rule(
    distancia['media'] & velocidade['lenta'],
    pressao['suave']
)

regra5 = control.Rule(
    distancia['media'] & velocidade['moderada'],
    pressao['media']
)

regra6 = control.Rule(
    distancia['media'] & velocidade['rapida'],
    pressao['forte']
)

# Distância LONGA
regra7 = control.Rule(
    distancia['longa'] & velocidade['lenta'],
    pressao['suave']
)

regra8 = control.Rule(
    distancia['longa'] & velocidade['moderada'],
    pressao['suave']
)

regra9 = control.Rule(
    distancia['longa'] & velocidade['rapida'],
    pressao['media']
)

regras = control.ControlSystem([
    regra1, regra2, regra3,
    regra4, regra5, regra6,
    regra7, regra8, regra9
])

pressao_controle = control.ControlSystemSimulation(regras)

d = float(input(
    "Digite a distância do obstáculo (em metros): "
))

v = float(input(
    "Digite a velocidade atual (em km/h): "
))

# Verificação dos limites
if not 0 <= d <= 100:
    print("Erro: a distância deve estar entre 0 e 100 metros.")
    exit()

if not 0 <= v <= 100:
    print("Erro: a velocidade deve estar entre 0 e 100 km/h.")
    exit()

pressao_controle.input['distancia'] = d
pressao_controle.input['velocidade'] = v
pressao_controle.compute()

resultado = pressao_controle.output['pressao']

print("\n===== RESULTADO =====")
print(f"Distância: {d:.1f} m")
print(f"Velocidade: {v:.1f} km/h")
print(f"Pressão no freio: {resultado:.2f}%")

