import streamlit as st
import pandas as pd

# Código capaz de realizar o cálculo da variância e do desvio padrão e mostrar a resolução

def main():
    st.title('Calculadora Desvio Padrão')
    st.warning('Digitar valores decimais com ponto ao invés de vírgula. Ex.: 11.5')
    st.image('image.png')

    # listas
    lista = []
    lista_sub = []
    lista_pot = []

    # medidas
    variaveis = st.text_input('Quantos valores você deseja calcular? ')

    # transforma o input em int
    if variaveis:
        try:
            with st.form(key='valores'):
                for i in range(int(variaveis)):
                    valor = st.number_input(f'Informe o {i+1}° valor: ', key=f'valor_{i}')

                    if valor:
                        int_valor = float(valor)
                        lista.append(int_valor)
                # st.button('Resetar', type="primary")
                calcular = st.form_submit_button('Calcular')

            # média
            if calcular:
                if len(lista) == int(variaveis):
                    media = sum(lista) / int(variaveis)
                    # st.write(media)
                    # st.write(variaveis)

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

                    data = {
                        'Valores': lista,
                        'Média (X̄)': media,
                        'Desvio (X - X̄)': lista_sub,
                        'Desvio²': lista_pot
                    }
                    df = pd.DataFrame(data)

                    df_trns = df.T
                    df_trns.columns = [f"valor {i+1}" for i in range(len(lista))]

                    st.dataframe(df_trns)

        except:
            st.error('Insira um valor correto')

if __name__ == '__main__':
    main()
