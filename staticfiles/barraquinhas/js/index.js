document.getElementById('vendas').addEventListener(onclick, function(){
    window.location.href = "{% url 'login' %}"
})

document.getElementById('administrativa').addEventListener(onclick, function(){
    window.location.href = "{% url 'admin' %}"
})