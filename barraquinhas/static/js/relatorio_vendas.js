const quantidadeVendida = document.getElementById('quantidadeVendida')
const valorVendido = document.getElementById('valorVendido')

const dataInicio = document.getElementById('dataInicio')
const dataFim = document.getElementById('dataFim')

async function gerarGraficos(dataInicio, dataFim) {
   await utils.criarGraficoQuantidades('quantidadeVendida', quantidadeVendida.id, dataInicio, dataFim)
   await utils.criarGraficoValorVendido('valorArrecadado', valorVendido.id, dataInicio, dataFim)
}

dataFim.addEventListener('change', function() {
   utils.destruirGraficos()
   gerarGraficos(dataInicio.value, dataFim.value)
})

dataInicio.addEventListener('change', function() {
   utils.destruirGraficos()
   gerarGraficos(dataInicio.value, dataFim.value)
})

document.addEventListener('DOMContentLoaded', function() {
   gerarGraficos(dataInicio.value, dataFim.value)
})

//exportar excel
function exportarExcel(){
   const dataInicio = document.getElementById('dataInicio').value
   const dataFim = document.getElementById('dataFim').value
   let url = document.getElementById('excel-download').getAttribute('data-url')

   url += '?data_inicio' + '=' + encodeURIComponent(dataInicio) + '&'
   url += 'data_fim' + '=' + encodeURIComponent(dataFim)

   window.location.href = url;
}