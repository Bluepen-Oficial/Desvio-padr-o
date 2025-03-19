import streamlit as st
import pandas as pd

# Código capaz de realizar o cálculo da variância e do desvio padrão e mostrar a resolução
def main():
    st.title('Calculadora Desvio Padrão')
    st.warning('Digite valores decimais usando ponto em vez de vírgula. Ex.: 11.5')
    st.image('image.png')

    # Listas para armazenar os valores e cálculos
    lista = []
    lista_sub = []
    lista_pot = []

    # Solicita a quantidade de valores
    variaveis = st.text_input('Quantos valores você deseja calcular? ')
    
    # Verifica se há um valor inserido
    if variaveis:
        try:
            # Converte a quantidade de variáveis para inteiro
            int_variaveis = int(variaveis)
            
            with st.form(key='valores'):
                # Entrada de valores individuais
                for i in range(int_variaveis):
                    valor = st.number_input(f'Informe o {i+1}° valor: ', value=None, placeholder="Insira um valor", key=f'valor_{i}')
                    
                    # Adiciona apenas se o valor for fornecido
                    if valor:
                        lista.append(float(valor))

                # Botão para calcular
                calcular = st.form_submit_button('Calcular')

            # Realiza os cálculos após clicar no botão
            if calcular:
                if len(lista) == int_variaveis:
                    # Cálculo da média
                    media = sum(lista) / int_variaveis

                    # passo 01
                    for i in range(int(variaveis)):
                        entrar = lista[i]
                        subtrair = entrar - media
                        lista_sub.append(subtrair)

                    # passo 02
                    for i in range(int(variaveis)):
                        entrar_1 = lista_sub[i]
                        elevar = entrar_1**2
                        lista_pot.append(elevar)

                    # variância
                    valor_med = int(variaveis) - 1
                    variancia = sum(lista_pot) / valor_med

                    # desvio padrão
                    desvio_pd = variancia**0.5
                    st.write(f'\nA variância é igual a: {variancia:.3f}')
                    st.write(f'O desvio padrão é igual a: {desvio_pd:.3f}')
                    
                    # Exibindo a tabela de dados
                    data = {
                        'Valores': lista,
                        'Média (X̄)': [media] * int_variaveis,
                        'Desvio (X - X̄)': lista_sub,
                        'Desvio²': lista_pot
                    }
                    df = pd.DataFrame(data)

                    # Transpor a tabela para melhor visualização
                    df_trns = df.T
                    df_trns.columns = [f"valor {i+1}" for i in range(int_variaveis)]
                    st.dataframe(df_trns)
limpar = st.button('Calcular')

        except ValueError:
            st.error('Por favor, insira um número inteiro válido para a quantidade de valores.')

if __name__ == '__main__':
    main()
