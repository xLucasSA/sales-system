function confimrarSaida() {
    const resposta = confirm('Deseja realmente sair?')

    if (resposta) {
        url = document.getElementById('sair').getAttribute('data-url')
        
        window.location.assign(url)
    }
}