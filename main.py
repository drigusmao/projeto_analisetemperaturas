# Instala as bibliotecas que serão utilizadas no projeto
import numpy as np  # Importa a biblioteca NumPy com apelido (np)
import matplotlib.pyplot as plt  # Importa a biblioteca com apelido (plt)

# Imprime na tela a mensagem de boas-vindas
print("Olá, vamos analisar as temperaturas da semana!")

# Cria uma lista com todos os dias da semana com acentuação correta
dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]

# Salva as temperaturas da semana que serão obtidas através do usuário
temperaturas = []

# Solicita ao usuário o valor da temperatura de cada dia, valida a entrada
for dia in dias:  # Laço for que percorre cada item da lista dias
    while True:  # Laço infinito que para quando interrompido pelo break
        try:  # Começa as tentativas de registro das temperaturas
            temp = float(input(f"Digite a temperatura de {dia}: "))  # Mensagem personalizada pedindo a temperatura do dia
            temperaturas.append(temp)  # Se o valor é válido é adicionado por ordem na lista temperaturas
            break  # Interrompe o laço while
        except ValueError:  # Se o usuário não digitar um número válido o laço continua pedindo até o usuário colocar um número válido
            print("Valor inválido! Digite um número.")  # Informa ao usuário que ele digitou algo errado que não é um número

# Mostra todas as temperaturas registradas
print("\n--- TEMPERATURAS REGISTRADAS ---")  # Imprime o título para mostrar as temperaturas registradas
for i in range(len(dias)):  # Usa o laço for que percorre os índices da lista dias
    print(f"{dias[i].capitalize()}: {temperaturas[i]}°C")  # Imprime os dias da semana e suas respectivas temperaturas

# Converte a lista temperaturas para um array Numpy
temperaturas = np.array(temperaturas)

# Calcula a média das temperaturas apresentadas da semana usando apenas np.mean()
media = np.mean(temperaturas)

# Verifica a maior temperatura e o dia correspondente
maior_temp = np.max(temperaturas)  # Salva na variável maior_temp o maior número presente da lista temperaturas
indice_maior = np.argmax(temperaturas)  # Retorna o índice da maior temperatura na lista
dia_maior = dias[indice_maior]  # Busca o dia correspondente à maior temperatura da lista

# Verifica a menor temperatura e o dia correspondente
menor_temp = np.min(temperaturas)  # Salva na variável menor_temp o menor número presente da lista temperaturas
indice_menor = np.argmin(temperaturas)  # Retorna o índice da menor temperatura na lista
dia_menor = dias[indice_menor]  # Busca o dia correspondente à menor temperatura da lista

# Mostra na tela a análise das temperaturas da semana
print("\n--- ANÁLISE DA SEMANA ---")  # Imprime o título da análise das temperaturas
print(f"Temperatura média da semana: {media:.1f}°C")  # Imprime a média da temperatura da semana
print(f"Maior temperatura: {maior_temp:.1f}°C ({dia_maior})")  # Imprime a maior temperatura da semana
print(f"Menor temperatura: {menor_temp:.1f}°C ({dia_menor})")  # Imprime a menor temperatura da semana

# Criação do gráfico de barras e sua formatação
x = np.arange(len(dias))  # Índices para o eixo x

plt.figure(figsize=(10, 5))  # Cria uma figura do gráfico com tamanho definido
plt.bar(x, temperaturas, color='lightcoral')  # Cria o gráfico de barras
plt.xticks(x, dias)  # Substitui os números do eixo x pelos nomes dos dias da semana
plt.xlabel("Dias da Semana")  # Adiciona o título no eixo x
plt.ylabel("Temperatura (°C)")  # Adiciona título no eixo y
plt.title("Temperaturas da Semana")  # Adiciona o título principal do gráfico
plt.grid(axis='y', linestyle='--', alpha=0.6)  # Adiciona linhas de grade no eixo Y

# Exibe a média como linha horizontal e faz sua formatação
plt.axhline(media, color='blue', linestyle='--', label=f"Média: {media:.1f}°C")
plt.legend()  # Exibe a legenda do gráfico
plt.tight_layout()  # Ajusta o espaçamento dos elementos do gráfico

# Exibe finalmente o gráfico na tela
plt.show()

# Exibe uma mensagem de finalização da análise das temperaturas
print("\nAnálise concluída com sucesso. Obrigado por utilizar o programa!")