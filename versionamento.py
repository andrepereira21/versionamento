idades = []      # Cria duas listas vazias chamadas idades e alturas. Estas listas serão usadas para armazenar as idades e alturas das 5 pessoas.
alturas = []
    
# Solicita a idade e altura de 5 pessoas

for i in range(5):      # Inicia um loop for que irá iterar 5 vezes, uma para cada pessoa. A variável i assume valores de 0 a 4 durante as iterações.
        
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))      # Dentro do loop, solicita ao usuário que insira a idade da pessoa i+1 (i+1 é usado para que a contagem comece em 1 ao invés de 0). O input() captura a entrada do usuário como uma string, int() converte essa string em um inteiro, e o resultado é armazenado na variável idade.

        altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))      #Solicita ao usuário que insira a altura da pessoa i+1. Semelhante à linha anterior, o input() captura a entrada do usuário como uma string, float() converte essa string em um número de ponto flutuante, e o resultado é armazenado na variável altura.

        idades.append(idade)       #  Adiciona a idade e altura obtidas às listas idades e alturas, respectivamente, usando o método append().
        alturas.append(altura)    
    
    # Imprime as idades e alturas na ordem inversa
print("\nIdades na ordem inversa:")       # Após o loop, imprime uma linha em branco seguida de "Idades na ordem inversa:", para indicar que as idades serão exibidas na ordem inversa.

for idade in reversed(idades):         # Usa o reversed() para iterar sobre a lista idades na ordem inversa. Para cada idade na lista invertida, imprime a idade.
      print(idade)
    
print("\nAlturas na ordem inversa:")        #  Imprime uma linha em branco seguida de "Alturas na ordem inversa:", para indicar que as alturas serão exibidas na ordem inversa.

for altura in reversed(alturas):          #   Similar às linhas 18-19, mas para a lista alturas. Usa reversed() para iterar sobre a lista alturas na ordem inversa e imprime cada altura.
        print(altura)
