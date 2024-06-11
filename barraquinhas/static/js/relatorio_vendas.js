const quantidadeVendida = document.getElementById('quantidadeVendida')
const valorVendido = document.getElementById('valorVendido')

quantidadeVendida.addEventListener('load', gerarGraficos())

async function gerarGraficos() {
   await criarGraficoQuantidades('quantidadeVendida', quantidadeVendida)
   await criarGraficoValorVendido('valorArrecadado', valorVendido)
}  