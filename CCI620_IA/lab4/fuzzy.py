from skfuzzy import control
import numpy as np
import matplotlib.pyplot as plt

#entradas
comida = control.Antecedent(np.arange(0, 10.1, 0.1), 'comida')
servico = control.Antecedent(np.arange(0, 10.1, 0.1), 'servico')

#saida
gorjeta = control.Consequent(np.arange(5, 25.1, 0.1), 'gorjeta')

from skfuzzy import gaussmf, zmf, smf, trimf # mf - membership function = função de pertinência

comida['boa'] = gaussmf(comida.universe, 5.0, 1)
comida['ruim'] = zmf(comida.universe, 0, 5)
comida['otima'] = smf(comida.universe, 5, 10)

servico['bom'] = gaussmf(servico.universe, 5.0, 1)
servico['ruim'] = zmf(servico.universe, 0, 5)
servico['otimo'] = smf(servico.universe, 5, 10)

gorjeta['pouca'] = trimf(gorjeta.universe, [5,5,15])
gorjeta['media'] = trimf(gorjeta.universe, [5,15,25])
gorjeta['muita'] = trimf(gorjeta.universe, [15,25,25])

import matplotlib.pyplot as plt
comida['otima'].view()
servico.view()
gorjeta.view()

regra1 = control.Rule(comida['ruim'] | servico['ruim'], gorjeta['pouca'])
regra2 = control.Rule(comida['boa'], gorjeta['media'])
regra3 = control.Rule(comida['otima'] | servico['bom'], gorjeta['muita'])


regras = control.ControlSystem([regra1, regra2, regra3])
gorjeta_controle = control.ControlSystemSimulation(regras)

gorjeta_controle.input['comida'] = 0
gorjeta_controle.input['servico'] = 0

gorjeta_controle.compute()

comida.view(sim=gorjeta_controle)
servico.view(sim=gorjeta_controle)

print(gorjeta_controle.output['gorjeta'])
gorjeta.view(sim=gorjeta_controle)
