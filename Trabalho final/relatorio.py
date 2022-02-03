import os 
from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Times", "", 16)

texto = "Aluno: Vitor O. da Silva / Turma: C \n\nCoronavirus Munícipio de Itapetininga - Dias Atuais\n\nSARS-CoV-2 é um vírus que causa uma doença respiratória (a covid-19) pelo agente coronavírus, identificado em dezembro de 2019 na China. Os coronavírus são uma grande família viral, conhecidos desde meados de 1960, que causam infecções respiratórias em seres humanos e em animais.\nNos dias de hoje estamos passando uma das piores épocas já vivenciadas, e no município Brasileiro de Itapetininga do estado de São Paulo, na Região Sudeste do país não é diferente. Atualmente, Itapetininga possui uma população de 167.106 habitantes. Foram confirmados cerca de 17.632 casos e 559 mortes até agora.\nTanto homens como mulheres vêm sendo vítimas dessa doença e a faixa etária está bastante dividida.\nApesar de outros municípios estarem mais prejudicados, Itapetininga vem conseguindo controlar as mortes, fazendo com que a porcentagem de óbitos seja baixa em relação a outros lugares.\nEntretanto, se as pessoas não se colocarem no lugar do proximo e começarem a se cuidar, mais vidas serão tiradas."

pdf.multi_cell(w=0, h=8, txt=texto, align="C")

pdf.image(name="casos.png", x=90, y=163, w=126)

pdf.image(name="obitos.png", x=37, y=172, w=87)

pdf.output("relatorio.pdf")

print("Sim, o PDF foi criado!")
os.system("pause")