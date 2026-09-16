# 🧮 Resolvedor de Sistemas Lineares (Métodos de Gauss e LU)

Um sistema interativo desenvolvido em **Python** para a resolução de sistemas de equações lineares utilizando métodos diretos de Cálculo Numérico. O projeto aplica conceitos de álgebra linear matricial e foca na eficiência computacional através da vetorização de operações.

## 🚀 Funcionalidades

O programa conta com um menu interativo executado via terminal, oferecendo 4 abordagens diferentes para a resolução de sistemas $Ax = b$:

1. **Eliminação de Gauss com Pivoteamento Parcial:** Evita divisões por zero e reduz erros de arredondamento em ponto flutuante trocando as linhas da matriz.
2. **Eliminação de Gauss Simples:** Fatoração direta (ideal para matrizes estritamente diagonais dominantes).
3. **Decomposição LU Simples:** Fatora a matriz em $A = L \cdot U$, permitindo a troca rápida do vetor de termos independentes ($b$) sem necessidade de reescalonar a matriz principal.
4. **Decomposição LU com Pivoteamento Parcial ($PA = LU$):** A versão mais robusta, utilizando um vetor de permutação $P$ para rastrear o histórico de troca de equações e garantir a consistência matemática durante as substituições sucessivas e regressivas.

## 🧠 Aprendizados e Arquitetura

Este projeto foi construído como aplicação prática para a disciplina de **Cálculo Numérico** no curso de **Engenharia de Computação** do IFF Bom Jesus. 

Do ponto de vista de Estrutura de Dados, o algoritmo abandona as iterações clássicas célula a célula (típicas de C/C++) em favor de **operações vetorizadas e fatiamento avançado de arrays (*slicing*)** utilizando a biblioteca `NumPy`. Isso delega o trabalho pesado de iteração para rotinas otimizadas em C, garantindo maior performance.

## 🛠️ Pré-requisitos e Instalação

Para rodar este projeto, você precisará ter o Python instalado e a biblioteca `NumPy`.