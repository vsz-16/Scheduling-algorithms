#Este códgio também está disponível no: https://github.com/vsz-16/Scheduling-algorithms.git
import numpy as np #Chama a função numpy de np e traz pro código
np.set_printoptions(precision=3, suppress=True) #Arredonda as casas decimais na matriz pra não ficar horrível

def recebeDados():
    while True:
        m = int(input("Digite a magnitude da matriz:\n"))
    
        #recebe todos os dados da matriz em um vetor
        entradaA = input(f"Digite os {m*m} dados da matriz com espaço entre eles:\n")
        entradaB = input(f"\nDigite os {m} dados da coluna de respostas com espaço entre eles\n")

        #Cria um vetor do np e fatia os dados que eram uma string em várias strings. Depois transforma as mesmas em float
        v1 = np.array(entradaA.split(), dtype=float)
        v2 = np.array(entradaB.split(), dtype=float)

        #transforma o vetor em matriz 
        matriz = v1.reshape((m, m))
        matriz = np.column_stack((matriz, v2))

        #parte que o usuário confirma a informação
        print("---Essa é sua matriz---")
        print(matriz)
        resposta = input("\nTudo certo?Y/N:\n")
        if resposta == "Y":
            return matriz, m
        else: 
            print("\nOk! Vamos preencher os dados novamente.\n")

def pivot(matriz, m):
    #Salvando a matriz pra usar no calculo do resíduo depois
    AOrig = np.copy(matriz[:, :m])
    bOrig = np.copy(matriz[:, m])

    for i in range(m - 1):
        # Variáveis auxiliares para encontrar o maior pivô na coluna 'i'
        maior = np.abs(matriz[i, i])
        lmaior = i
        
        # Procura o maior número em módulo na coluna da linha i+1 em diante
        for k in range(i + 1, m):
            if np.abs(matriz[k, i]) > maior:
                maior = np.abs(matriz[k, i])
                lmaior = k
                
        # Teste e troca de linhas
        if maior == 0:
            print(f"Erro: A coluna {i} tem apenas zeros. A matriz não é válida.")
            return
        elif lmaior != i:
            matriz[[i, lmaior]] = matriz[[lmaior, i]]
            
        # Zerando tudo
        for j in range(i + 1, m):
            a = matriz[j, i] / matriz[i, i]
            matriz[j] = matriz[j] - a * matriz[i]
            
#Resolvendo o sistema
    x = np.zeros(m)
    for l in range(m - 1, -1, -1):
        soma = matriz[l, m] 
        
        for n in range(l + 1, m):
            soma = soma - (matriz[l, n] * x[n])
            
        x[l] = soma / matriz[l, l]
    print(f"\nA resolução é: {x}\n")

    #Calculo do resíduo
    residuo = bOrig - np.dot(AOrig, x)
    erro = np.linalg.norm(residuo)
    print("--- Análise de Erro ---")
    print(f"Vetor Resíduo: {residuo}")
    print(f"Magnitude do Erro: {erro:.2e}\n")

def gauss(matriz, m):
    AOrig = np.copy(matriz[:, :m])
    bOrig = np.copy(matriz[:, m])
    
    #Mesma coisa do outro só que sem trocar as linhas
    for i in range(m - 1):
        # Se o pivô da diagonal for zero o Gauss simples não consegue resolver
        if matriz[i, i] == 0:
            print(f"\nErro: O pivô na posição [{i},{i}] é zero! O Gauss simples falhou.")
            return
            
        # Eliminação direta nas linhas abaixo
        for j in range(i + 1, m):
            a = matriz[j, i] / matriz[i, i]
            matriz[j] = matriz[j] - a * matriz[i]

    x = np.zeros(m)
    for i in range(m - 1, -1, -1):
        soma = matriz[i, m]
        for j in range(i + 1, m):
            soma = soma - matriz[i, j] * x[j]
        x[i] = soma / matriz[i, i]
        
    print("\n=== Solução pelo Método de Gauss Simples ===")
    for idx in range(m):
        print(f"X{idx+1} = {x[idx]:.2f}")

    residuo = bOrig - np.dot(AOrig, x)
    erro = np.linalg.norm(residuo)
    print("--- Análise de Erro ---")
    print(f"Vetor Resíduo: {residuo}")
    print(f"Magnitude do Erro: {erro:.2e}\n")

def lu(matriz, m):
    AOrig = np.copy(matriz[:, :m])
    bOrig = np.copy(matriz[:, m])

    # Separa a matriz A do vetor b
    A = np.copy(matriz[:, :m])
    b = np.copy(matriz[:, m])
    
    L = np.eye(m)       # Matriz identidade para o L
    U = np.copy(A)      # U começa como A e vai sendo zerada
    
    for i in range(m - 1):
        if U[i, i] == 0:
            print(f"\nErro: O pivô na posição [{i},{i}] é zero,")
            return
            
        # Eliminação e construção do L
        for j in range(i + 1, m):
            a = U[j, i] / U[i, i]
            L[j, i] = a               
            U[j] = U[j] - a * U[i]      
            
    print("\nMatriz L:\n", L)
    print("Matriz U:\n", U)
    
    #Resolvendo L * y = b 
    y = np.zeros(m)
    # Como não teve troca de linhas, é só usar o vetor b direto
    for i in range(m):
        soma = b[i]
        for j in range(i):
            soma = soma - (L[i, j] * y[j])
        y[i] = soma
    #Substituição regressiva
    x = np.zeros(m)
    for i in range(m - 1, -1, -1):
        soma = y[i]
        for j in range(i + 1, m):
            soma = soma - (U[i, j] * x[j])
        x[i] = soma / U[i, i]
        
    print(f"\n==== A resolução pelo método LU Simples ====\n{x}\n")

    residuo = bOrig - np.dot(AOrig, x)
    erro = np.linalg.norm(residuo)
    print("--- Análise de Erro ---")
    print(f"Vetor Resíduo: {residuo}")
    print(f"Magnitude do Erro: {erro:.2e}\n")

def luP(matriz, m):
    AOrig = np.copy(matriz[:, :m])
    bOrig = np.copy(matriz[:, m])

    # Separa a matriz A do vetor b 
    A = np.copy(matriz[:, :m])
    b = np.copy(matriz[:, m])
    
    L = np.eye(m)       # Matriz identidade para o L
    U = np.copy(A)      # U começa como A e vai sendo zerada
    P = np.arange(m)    # Vetor de permutação: [0, 1, 2, ...]

    for i in range(m - 1):
        lmaior = i + np.argmax(np.abs(U[i:m, i]))
        maior = np.abs(U[lmaior, i]) 
        if maior == 0:
            print(f"Erro: A coluna {i} tem apenas zeros.")
            return
        elif lmaior != i:
            # Troca as linhas na matriz U e guarda a troca no vetor de permutação
            U[[i, lmaior]] = U[[lmaior, i]]
            P[[i, lmaior]] = P[[lmaior, i]]
            if i > 0:
                L[[i, lmaior], :i] = L[[lmaior, i], :i]

        # Zerando tudo
        for j in range(i + 1, m):
            a = U[j, i] / U[i, i]
            L[j, i] = a         # Guardando o multiplicador no L
            U[j] = U[j] - a * U[i]
            
    print("Matriz L:\n", L)
    print("Matriz U:\n", U)
    print("Vetor de Permutação P:\n", P)
    
    #As duas etapas de substituição (Ly=Pb e Ux=y) 
    y = np.zeros(m)
    bPermutado = b[P]
    for i in range(m):
        soma = bPermutado[i]
        for j in range(i):
            soma = soma - (L[i, j] * y[j])
        y[i] = soma
        
    x = np.zeros(m) # É o vetor final de respostas
    for i in range(m - 1, -1, -1):
        soma = y[i]
        for j in range(i + 1, m):
            soma = soma - (U[i, j] * x[j])
            
        x[i] = soma / U[i, i]

    print(f"\n====A resolução pelo método LU==== \n{x}\n")

    residuo = bOrig - np.dot(AOrig, x)
    erro = np.linalg.norm(residuo)
    print("--- Análise de Erro ---")
    print(f"Vetor Resíduo: {residuo}")
    print(f"Magnitude do Erro: {erro:.2e}\n")

def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Método de Gauss com Pivotamento")
        print("2 - Método de Gauss simples")
        print("3 - Método LU")
        print("4 - Método LU parcial")
        print("0 - Sair do Programa")
        
        opcao = input("Escolha uma opção:\n").strip()
        
        if opcao == "1":
            matriz, m = recebeDados()
            pivot(matriz, m)
        if opcao == "2":
            matriz, m = recebeDados()
            gauss(matriz, m)
        if opcao == "3":
            matriz, m = recebeDados()

        if opcao =="4":
            matriz, m = recebeDados()
            luP(matriz, m)
        elif opcao == "0":
            print("\nEncerrando o programa...")
            break
        else:
            print("\nOpção inválida! Digite 1 ou 0.")
main()