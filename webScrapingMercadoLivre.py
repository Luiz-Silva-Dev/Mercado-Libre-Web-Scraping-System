import requests
from bs4 import BeautifulSoup
import pandas
import statistics as sta
import matplotlib.pyplot as plt
from funcoesDoPrograma.tratamentoDeDados import *

dadosColetados = []
listaDeValores = []
paginaAtual = 0
ultimaPagina = acharNumeroMaximoDePaginas()
somaDeValores = 0       

while True:
    if paginaAtual < ultimaPagina:
        paginaAtual +=1
        print(f'Analisando Pagina {paginaAtual}')
        url = irParaAProximaPagina(paginaAtual, ultimaPagina)

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        dadosDeCadaProduto = soup.findAll('li', class_='promotion-item')

        for dadosDosProdutos in dadosDeCadaProduto:
            tituloDoProduto = dadosDosProdutos.find('p', attrs={'class' : 'promotion-item__title'}).text
            valorDoProduto = dadosDosProdutos.find('span', attrs={'class' : 'andes-money-amount andes-money-amount--cents-superscript'}).text
            porcentagemDoProduto =removerLetrasESubstituirVigulasPorPontosDosValores(dadosDosProdutos.find('span', attrs={'class':'promotion-item__discount-text'}).text)
            linkDoProduto = dadosDosProdutos.find('a', attrs={'class' : 'promotion-item__link-container'})
            linkDoProduto = linkDoProduto['href']

            if porcentagemDoProduto == '':
                porcentagemDoProduto = '0'
            if int(porcentagemDoProduto) >= 15:
                somaDeValores += float(removerLetrasESubstituirVigulasPorPontosDosValores(valorDoProduto))
                dadosColetados.append((tituloDoProduto, valorDoProduto, porcentagemDoProduto, linkDoProduto))
                listaDeValores.append(float(removerLetrasESubstituirVigulasPorPontosDosValores(valorDoProduto)))   
        print('------Sucesso------')         
    else:
        break

EmprimirDadosCalculadosPeloPrograma(somaDeValores, dadosColetados, listaDeValores)
dataFrameDeDados = pandas.DataFrame(dadosColetados, columns=["titulo", "valor", "porcentagem", "link"])
dataFrameDeDados.to_csv('DadosArquivados.csv', index=False)
dadosArquivadosCSV = 'DadosArquivados.csv'
lerArquivoCSV = pandas.read_csv(dadosArquivadosCSV)
dadosArquivadosExcel = dadosArquivadosCSV.replace('csv', 'xlsx')
lerArquivoCSV.to_excel(dadosArquivadosExcel, index=None, header=True)
valoresDoDataFrameFormatados = formatarOsNumerosDoDataFrame(dataFrameDeDados)
fig, box = plt.subplots()
box.boxplot([valoresDoDataFrameFormatados], labels=['Produtos'])
plt.title('Boxplot de Valores')
plt.ylabel('Valores')
plt.grid(True)
plt.show()