import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Dados.xlsx")

sexo = planilha["SEXO"]
óbitos = planilha["ÓBITOS"]

plt.title("Coronavirus Óbitos Itapetininga - 2021")


plt.bar(sexo, óbitos, color="brown", width=0.5) 

plt.show()

