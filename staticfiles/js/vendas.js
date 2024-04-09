function variarQuantidade(id, operacao) {
    let quantidadeHTML = document.getElementById(id)
    const quantidadeNum = Number(quantidadeHTML.innerText)
    let novaQuantidade = 0

    if (operacao === 'reduzir') {
        quantidadeNum > 0 ? novaQuantidade = quantidadeNum - 1 : novaQuantidade = 0
    }
    if (operacao === 'aumentar') {
        novaQuantidade = quantidadeNum + 1
    }

    quantidadeHTML.innerText = novaQuantidade
}

function limparCampos(produtos) {
    for (let produto of produtos) {
        let produtoHtml = document.getElementById(produto)
        
        produtoHtml.tagName == "INPUT" ? produtoHtml.value = 0 : produtoHtml.innerText = 0
    }
}

function coletarEnviar(produtos) {
    const formData = {};
    
    for (let produto of produtos) {
        let produtoHtml = document.getElementById(produto)

        let quantidade = produtoHtml.tagName == "INPUT" ? Number(produtoHtml.value) : Number(produtoHtml.innerText)

        if (quantidade > 0) {
            formData[produto] = quantidade
        }
        else {
            continue
        }
    }

    for (let chave in formData) {
        let hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", chave);
        hiddenField.setAttribute("value", formData[chave]);
        document.getElementById("formularioVendas").appendChild(hiddenField);
    }

    if (Object.keys(formData).length > 0) {
        document.getElementById("formularioVendas").submit();
    }
}