import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

covid = pd.read_csv('Dados-covid-19-municipios.csv', sep = ';', encoding='latin-1')

covid.head()

cidades = covid.query('Município == "Bauru" | Município == "São José do Rio Preto" | Município == "Campinas" ')

fig, (axis1) = plt.subplots(1, 1, figsize=(15, 5))
axis1 = sns.barplot(x = 'Município', y = 'Mun_Total de casos', data = cidades, ax = axis1, palette = 'mako')
axis1.set_title('Casos da Covid 19 em Cidades que não fizeram o Lockdown', fontsize=25, pad=25)
axis1.set_ylabel("Total", fontsize=18)
axis1.set_xlabel("Cidade", fontsize=18)

plt.show()