function changeImage(id) {
    let imagem = document.getElementById(id);
    imagem.src = `/static/barraquinas/img/${id}-hover.png`
    console.log(imagem.src);
}
  
function resetImage() {
    var mainImage = document.getElementById('mainImage');
    mainImage.src = 'default-image.jpg'; // Set it back to the default image
  }