import pandas as pd
import matplotlib.pyplot as plt

planilha = pd.read_excel("Dados.xlsx")

sexo = planilha["SEXO"]
casos = planilha["CASOS"]

plt.title("Coronavirus Casos Itapetininga - 2021")

plt.pie(casos, labels=sexo, autopct="%1.2f%%")

plt.show()