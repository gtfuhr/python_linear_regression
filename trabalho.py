from math import sqrt
import math


def tamanho(x):
    return len(x)


def somatorio(lista):
    somatorio = 0
    for num in lista:
        somatorio += num
    return somatorio


def media(lista_num):
    somatorio = 0
    tam_lista = tamanho(lista_num)
    for num in lista_num:
        somatorio += num
    if tam_lista > 0:
        return float(somatorio/tam_lista)
    else:
        # Evitar possivel divisao por zero
        return 0


def elevado_a(num, potencia):
    return pow(num, potencia)


def desvio_padrao(lista_num):
    media_ = media(lista_num)
    tam_lista = tamanho(lista_num)

    for num in lista_num:
        somatorio_quadrados += num ** 2
    return (somatorio_quadrados - tam_lista*media) / (tam_lista-1)


def coeficiente_de_correlacao_de_Pearson(x, y):
    if(tamanho(x) != tamanho(y)):
        exit(0)
    n = tamanho(x)
    somatorio_x = float(somatorio(x))
    somatorio_y = float(somatorio(y))
    x_squared = [xi * xi for xi in x]
    y_squared = [yi * yi for yi in y]
    somatorio_x_sq = somatorio(x_squared)
    somatorio_y_sq = somatorio(y_squared)
    psomatorio = 0
    for xi, yi in zip(x, y):
        psomatorio += (xi * yi)
    num = psomatorio - (somatorio_x * somatorio_y/n)
    den = elevado_a((somatorio_x_sq - elevado_a(somatorio_x, 2) / n)
                    * (somatorio_y_sq - elevado_a(somatorio_y, 2) / n), 0.5)
    return num / den


def le_listas(lista_desejada):
    arq_name = "ex"+str(lista_desejada) + ".csv"
    arq = open(arq_name)
    import csv
    with open(arq_name) as csvfile:
        data = list(csv.reader(csvfile))
    print("\n", data.pop(0))
    x = [float(a[0]) for a in data]
    y = [float(a[1]) for a in data]

    return x, y


def calc_b1(x, y):
    somatorio_x1_vezes_y1 = 0
    for xi, yi in zip(x, y):
        somatorio_x1_vezes_y1 += (xi * yi)

    x_media = media(x)
    y_media = media(y)
    somatorio_mediasx_y = tamanho(x) * (x_media * y_media)

    somatorio_xi_quadrado = 0
    for num in x:
        somatorio_xi_quadrado += (num * num)

    somatorio_media_x_quadrado = tamanho(x) * (x_media * x_media)

    b1 = (somatorio_x1_vezes_y1 - somatorio_mediasx_y) / \
        (somatorio_xi_quadrado - somatorio_media_x_quadrado)
    return b1


def calc_b0(x, y, b1):
    return media(y) - (b1 * media(x))


def estimadores_de_minimos_quadrados(x, y):
    b1 = calc_b1(x, y)
    b0 = calc_b0(x, y, b1)

    return b0, b1


def calc_erro_padrao(x, y, b0, b1):
    return


def teste_hipotese_existencia_regressao_linear(x, y, b0, b1):
    tamanho_lista = tamanho(x)

    # HIPOTESE NULA
    print("Hipotese nula == H0: b1 = 0")
    # HIPOTESE ALTERNATIVA
    print("Hipotese alternativa == H1: b1 != 0")

    y_squared = [yi * yi for yi in y]
    y_media = media(y)
    x_squared = [xi * xi for xi in x]
    x_media = media(x)
    Syy = somatorio(y_squared) - (tamanho(y) * (y_media * y_media))
    Sxy = somatorio(x_squared) - (tamanho(y) * (y_media * y_media))
    Sxx = somatorio(x_squared) - (tamanho(x) * (x_media * x_media))

    c = sqrt((Syy - b1*Sxy) / (tamanho(x)-2))

    tc = (b1 * sqrt(Sxx)) / c

    print("C e igual a:", c)
    print("T Calculado e igual a:", tc)


def teste_hipotese_coeficiente_correlacao(x, y, pearson):
    tamanho_lista = tamanho(x)
    # HIPOTESE NULA
    print("Hipotese nula == H0: p = 0")

    # HIPOTESE ALTERNATIVA
    print("Hipotese alternativa == H1: p != 0")

    tc = (pearson * sqrt(tamanho_lista - 2))/sqrt(1 - elevado_a(pearson, 2))

    print("O t estatistico e:", tc)


def main():
    print("Qual e a lista que voce deseja?")
    print("1 - ex1")
    print("2 - ex2")

    lista_desejada = input("Selecione a lista digitando o seu numero:")
    x, y = le_listas(lista_desejada)
    tamanho_lista = tamanho(x)

    # QUESTAO 1 #############################
    # LETRA a ###############################
    pearson = coeficiente_de_correlacao_de_Pearson(x, y)
    print("\nCoeficiente de Correlacao de Pearson:\n", pearson)

    # LETRA b ###############################
    print("\nTeste de hipoteses para os coeficientes de relacao:")
    teste_hipotese_coeficiente_correlacao(x, y, pearson)

    # LETRA c ###############################
    print("\nEstimadores de minimos quadrados ordinarios para regressao:\n")
    b0, b1 = estimadores_de_minimos_quadrados(x, y)
    print("B0 ==", b0, "b1 ==", b1)

    # LETRA d ###############################
    print("\nTeste de hipotese de significancia para regressao linear:\n")
    teste_hipotese_existencia_regressao_linear(x, y, b0, b1)


def questao_2():
    x, y = le_listas(1)
    tamanho_lista = tamanho(x)
    pearson = coeficiente_de_correlacao_de_Pearson(x, y)
    print("Coeficiente de Correlacao de Pearson:", pearson)
    teste_hipotese_coeficiente_correlacao(x, y, pearson)


def questao_3():
    x, y = le_listas(1)
    tamanho_lista = tamanho(x)
    b0, b1 = estimadores_de_minimos_quadrados(x, y)
    teste_hipotese_significancia_regressao_linear(x, y, b0, b1)


def preve(b0, b1, valor):
    return b0 + b1 * valor


def questao_4():
    x, y = le_listas(1)
    tamanho_lista = tamanho(x)
    b0, b1 = estimadores_de_minimos_quadrados(x, y)
    previsao = preve(x, y, b0, b1, 900.00)
    print("Se espera, para uma empresa que investiu 900 em propaganda\n,\
         que o retorno seja de:", previsao)


def questao_5():
    x, y = le_listas(2)
    tamanho_lista = tamanho(x)
    pearson = coeficiente_de_correlacao_de_Pearson(x, y)
    print("Coeficiente de Correlacao de Pearson:", pearson)
    teste_hipotese_coeficiente_correlacao(x, y, pearson)


def questao_6():
    x, y = le_listas(2)
    tamanho_lista = tamanho(x)
    b0, b1 = estimadores_de_minimos_quadrados(x, y)
    teste_hipotese_significancia_regressao_linear(x, y, b0, b1)


def questao_7():
    x, y = le_listas(2)
    tamanho_lista = tamanho(x)
    b0, b1 = estimadores_de_minimos_quadrados(x, y)
    previsao = preve(x, y, b0, b1, 350.00)
    print("Se espera, para um caminhao que percorreu 350 quilometros\n,\
         que o gasto de gasolina sera em media(Litros) de:", previsao)


if __name__ == "__main__":
    main()
