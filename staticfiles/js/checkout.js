import "./vendas"

function fecharPedido(pedido, totalPedido) {
    const formData = {};

    for (let produto of pedido) {
        const id = produto.id
        const quantidade = Number(produto.quantidade)

        if (quantidade > 0) {
            formData[id] = quantidade
        }
        else {
            continue
        }
    }

    const form = gerarFormulario(formData, "venda_finalizada")

    let hiddenField = document.createElement("input")
    hiddenField.setAttribute("type", "hidden")
    hiddenField.setAttribute("name", "valor_total")
    hiddenField.setAttribute("value", Number(totalPedido))
    form.appendChild(hiddenField)

    if (Object.keys(form).length > 1) {
        document.getElementById("venda_finalizada").submit();
    }
}