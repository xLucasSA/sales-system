
async function coletarDados(nomeGrafico, dataInicio, dataFim) {
    const url = quantidadeVendida.getAttribute('data-url')
    const data = {
        nomeGrafico,
        'data_inicio': dataInicio,
        'data_fim': dataFim,
    }
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })

    return response
}

window.utils = {
    coletarDados,
};