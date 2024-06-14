def removerLetrasESubstituirVigulasPorPontosDosValores(valor):
    ValorFormatado = ''

    for caractereOuDigito in valor:
        if caractereOuDigito == ',':
            caractereOuDigito = '.'
            ValorFormatado+= caractereOuDigito
        elif caractereOuDigito.isdigit():
            ValorFormatado += caractereOuDigito
    return ValorFormatado

def removerTodosOsCaracteres(ValorDaPagina):
    valorDaPaginaFormatado = ''
    lixeira = ''
    for digitos in ValorDaPagina:
        while True:
            if digitos.isdigit():
                valorDaPaginaFormatado += digitos
                break
            else: 
                lixeira += digitos
                break
    return valorDaPaginaFormatado

def acharNumeroMaximoDePaginas():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://www.mercadolivre.com.br/ofertas'

    response = requests.get(url, )
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    buscarClasse = soup.findAll('li', class_='andes-pagination__button')
    maiorNumeroDaPagina = 0

    for classe in buscarClasse:
        numeroPaginas = classe.find('a', attrs={'class' : 'andes-pagination__link'})
        if numeroPaginas:
            numeroPaginasFormatado = removerTodosOsCaracteres(numeroPaginas.text)
            if numeroPaginasFormatado.isdigit():
                numeroPaginasFormatado = int(numeroPaginasFormatado)
                if maiorNumeroDaPagina <= int(numeroPaginasFormatado):
                    maiorNumeroDaPagina = numeroPaginasFormatado
                else:
                    pass
    return maiorNumeroDaPagina 

def calcularMedia(somaDeValores, dados):
    media = somaDeValores / len(dados)
    media = round(media, 2)
    return media
def calcularMediana(listaDeValores):
    import statistics as sta
    mediana = round(sta.median(listaDeValores), 2)
    return mediana
def calcularAmplitude(listaDeValores):
    amplitude = max(listaDeValores) - min(listaDeValores)
    return amplitude
def calcularVariancia(listaDeValores):
    import statistics as sta
    variancia = round(sta.variance(listaDeValores), 2)
    return variancia
def calcularDesvioPadrao(listaDeValores):
    import statistics as sta
    desvioPadrao = round(sta.stdev(listaDeValores), 2)
    return (desvioPadrao)

def irParaAProximaPagina(paginaAtual, ultimaPagina):
    if paginaAtual <= ultimaPagina:
        return ('https://www.mercadolivre.com.br/ofertas?&page=' + str(paginaAtual))
    
def EmprimirDadosCalculadosPeloPrograma(somaDeValores, dadosColetados, listaDeValores):
    print(f'''
Calculos Realizados com base nos dados coletados:
Media = {calcularMedia(somaDeValores, dadosColetados)}
Mediana = {calcularMediana(listaDeValores)}
Amplitude = {calcularAmplitude(listaDeValores)}
Variancia = {calcularVariancia(listaDeValores)}
Desvio Padrao = {calcularDesvioPadrao(listaDeValores)}          
''')

def formatarOsNumerosDoDataFrame(dadosColetados):
    dadosDeValorFormatados = []    
    for dados in dadosColetados['valor']:
        dadosDeValorFormatados.append(float(removerLetrasESubstituirVigulasPorPontosDosValores(dados)))
    return dadosDeValorFormatados