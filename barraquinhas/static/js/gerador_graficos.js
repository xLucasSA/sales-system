async function criarGraficoQuantidades(nomeGrafico, htmlElement) {
    const response = await coletarDados(nomeGrafico)

    const dados = await response.json()
    const labels = Object.keys(dados)
    const data = Object.values(dados)

    await criarGrafico(htmlElement, 'bar', labels, data, 'Quantidade de Itens Vendidos', 'y')
}

async function criarGraficoValorVendido(nomeGrafico, htmlElement) {
    const response = await coletarDados(nomeGrafico)

    const dados = await response.json()
    const labels = Object.keys(dados)
    const data = Object.values(dados)

    await criarGrafico(htmlElement, 'line', labels, data, 'Valor Arrecadado (R$)', 'x')
}

window.utils = {
    criarGraficoQuantidades,
};