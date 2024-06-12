let charts = {}

async function criarGrafico(chartId, type, labels, data, subtitles, axis) {
    const ctx = document.getElementById(chartId).getContext('2d')

    charts[chartId] = new Chart(ctx, {
        type,
        data: {
            labels,
            datasets: [{
                label: subtitles,
                data,
                borderWidth: 3,
                tension: 0.4
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                }
            },
            indexAxis: axis,
        }
    })

    return charts[chartId]
}

async function criarGraficoQuantidades(nomeGrafico, htmlElementId, dataInicio, dataFim) {
    const response = await coletarDados(nomeGrafico, dataInicio, dataFim)

    if (!response.ok) {
        alert('Erro ao coletar dados:', response.statusText)
        return
    }

    const dados = await response.json()
    const labels = Object.keys(dados)
    const data = Object.values(dados)

    await criarGrafico(htmlElementId, 'bar', labels, data, 'Quantidade de Itens Vendidos', 'y')
}

async function criarGraficoValorVendido(nomeGrafico, htmlElementId, dataInicio, dataFim) {
    const response = await coletarDados(nomeGrafico, dataInicio, dataFim)

    if (!response.ok) {
        alert('Erro ao coletar dados:', response.statusText)
        return
    }

    const dados = await response.json()
    const labels = Object.keys(dados)
    const data = Object.values(dados)

    await criarGrafico(htmlElementId, 'line', labels, data, 'Valor Arrecadado (R$)', 'x')
}

function destruirGraficos() {
    for (let chartId in charts) {
        if (charts[chartId]) {
            charts[chartId].destroy()
            charts[chartId] = null  // Limpa a referência
        }
    }
}

window.utils = {
    criarGraficoQuantidades,
    criarGraficoValorVendido,
    destruirGraficos
}