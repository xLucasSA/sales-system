
async function criarGrafico(chartId, type, labels, data, subtitles, axis) {
    new Chart(chartId, {
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
     });
}

async function coletarDados(nomeGrafico) {
    const url = quantidadeVendida.getAttribute('data-url')
    const data = {
        nomeGrafico
    }
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })

    if(!response.ok) {
        // TODO:Mensagem de ERRO!
        return console.log(response.status);
    }

    return response
}

window.utils = {
    coletarDados,
};