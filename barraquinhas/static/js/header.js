function confimrarSaida() {
    const resposta = confirm('Deseja realmente sair?')

    if (resposta) {
        url = document.getElementById('sair').getAttribute('data-url')
        
        document.location.href = url
    }
}