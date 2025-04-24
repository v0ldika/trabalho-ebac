import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

#historiograma
plt.figure(figsize=(10, 6))
sns.histplot(df['Nota'], bins=20, kde=True, color='skyblue')
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota (1-5)')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#Gráfico de Dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Preço', y='N_Avaliações', data=df, hue='Gênero', alpha=0.7)
plt.title('Relação entre Preço e Número de Avaliações')
plt.xlabel('Preço (R$)')
plt.ylabel('Número de Avaliações')
plt.yscale('log')  # Escala logarítmica para melhor visualização
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Gênero')
plt.show()

# Mapa de Calor
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de Calor - Correlação entre Variáveis Numéricas')
plt.show()

top_marcas = df['Marca'].value_counts().head(10)

#Gráfico de Barras
plt.figure(figsize=(12, 6))
sns.barplot(x=top_marcas.index, y=top_marcas.values, palette='viridis')
plt.title('Top 10 Marcas por Número de Produtos')
plt.xlabel('Marca')
plt.ylabel('Quantidade de Produtos')
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()

#Gráfico de Pizza
top_materiais = df['Material'].value_counts().head(5)

plt.figure(figsize=(8, 8))
plt.pie(top_materiais, labels=top_materiais.index, autopct='%1.1f%%',
        startangle=90, colors=sns.color_palette('pastel'))
plt.title('Distribuição dos 5 Materiais Mais Comuns')
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='purple')
plt.title('Densidade de Distribuição de Preços')
plt.xlabel('Preço (R$)')
plt.ylabel('Densidade')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#Gráfico de Regressão
plt.figure(figsize=(10, 6))
sns.regplot(x='Desconto', y='Qtd_Vendidos', data=df)
plt.title('Relação entre Desconto e Quantidade Vendida')
plt.xlabel('Desconto (%)')
plt.ylabel('Quantidade Vendida (log)')
plt.yscale('log')  # Escala logarítmica para melhor visualização
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()