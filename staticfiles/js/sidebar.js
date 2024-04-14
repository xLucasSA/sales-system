window.addEventListener('scroll', function () {
    let viewportHeight = window.innerHeight;
    let scroll = window.scrollY || document.documentElement.scrollTop;
    let limiteHeader = 0.07 * viewportHeight;

    let elemento = document.getElementById('inicio').firstElementChild
    if (scroll > limiteHeader) {
       elemento.style.marginTop = `${scroll - limiteHeader}px`
    }
    else {
        elemento.style.marginTop = 0 
    }
})