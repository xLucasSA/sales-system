function variarQuantidade(id, operacao) {
    let quantidadeHTML = document.getElementById(id+"-quantidade")
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

function limparCampos(idProdutos) {
    for (let idProduto of idProdutos) {
        let produtoHtml = document.getElementById(idProduto+"-quantidade")
        
        produtoHtml.tagName == "INPUT" ? produtoHtml.value = 0 : produtoHtml.innerText = 0
    }
}

function gerarFormulario(formData, formId) {
    const newForm = document.getElementById(formId)

    for (let chave in formData) {
        let hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", chave);
        hiddenField.setAttribute("value", formData[chave]);
        newForm.appendChild(hiddenField);
    }

    return newForm
}

function coletarEnviarProdutos(idProdutos) {
    const formData = {};
    
    for (let idProduto of idProdutos) {
        const quantidadeHtml = document.getElementById(idProduto+"-quantidade")
        const quantidade = quantidadeHtml.tagName == "INPUT" ? Number(quantidadeHtml.value) : Number(quantidadeHtml.innerText)

        if (quantidade > 0) {
            formData[idProduto] = quantidade
        }
        else {
            continue
        }
    }

    const form = gerarFormulario(formData, "formulario_vendas")
    
    const resposta = confirm("Deseja fechar o pedido?")

    if (Object.keys(form).length > 0 && resposta) {
        document.getElementById("formulario_vendas").submit();
    }
}