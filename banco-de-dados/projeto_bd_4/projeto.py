import pandas as pd
import matplotlib.pyplot as plt

#salvar como: Pasta de Trabalho do Excel
#caso não faça isso, não será possível ler o arquivo!
df = pd.read_excel(r"D:/codigo-vsCode/programa-python/banco-de-dados/projeto_bd_4/ccont_2t_AC_271020181441.xlsx", sheet_name='ccont_2t_AC_271020181441')
print(df)

