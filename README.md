# <center> Sistema de Vendas Local </center>
<hr>

Esse é um sistema que foi desenvolvido utilizando o framework django. Será necessário que se tenha pelo menos o python instalado em sua máquina/servidor local. Se não o possui instalado pode instalar [clicando aqui](https://www.python.org/downloads/)

**Obs.:** O sistema ainda não foi projetado para utilização através de aparelhos celulares. 

Para seguir o passo-a-passo será necessário também que sua máquina utilize um dos sistemas **Windows**.

1. Baixe o zip desse programa;
2. Extraia a pasta para a sua área de trabalho e renomeie para: **sistema_igreja**;
3. Procure o arquivo: *example.env*. Nele contém duas configuraçoes, sendo elas: 
    ```
    SECRET_KEY=
    DB_NAME=sistema_igreja.db
    ```
    Você deverá inserir na primeira a chave que escolher para a sua aplicação. Ela será utilizada pelo servidor para fazer validações, então não a compartilhe com nínguem;

4. Em seguida, altere o nome de *example.env* para *.env*;
5. Entre na pasta e procure o arquivo: *Sistema.bat*. Você pode executar esse arquivo ou então se prefirir enviá-lo para a área de trabalho clicando com o botão direito sobre ele e em seguida na opção **Enviar Para > Área de Trabalho (criar atalho)**;
6. Após isso o sistema irá iniciar o servidor local e ficará disponível na porta 8000 de sua máquina/servidor para que possa ser acessado por outros usuários conectados a sua rede. Se não sabe como identificar o seu ip local pode conferir [aqui](https://support.microsoft.com/pt-br/windows/encontre-seu-endere%C3%A7o-ip-no-windows-f21a9bbc-c582-55cd-35e0-73431160a1b9#Category=Windows_10);
7. Caso falhe tente criar um arquivo dentro do prório diretório copiando o conteúdo do *Sistema.bat* para esse novo arquivo e substituíndo o *.bat* por *.cmd* e tente rodar novamente;
8. Para acessar de outro computador, basta ir no seguinte link: *seu.ip.local.aqui:8000* e estará disponível para acesso;
<hr>

## <center> Utilização </center>

### Area Administrativa
#### Usuários:
Nesse sistema, já está cadastrado um usuário padrão com credenciais:
```
usuário: admin
senha: admin
```

É possível inserir novos usuários e alterar o cadastro do usuário **admin** dentro da área administrativa na aba de usuários, além de excluir usuários cadastrados.

Essa sessão conta ainda com uma aba de relatório de vendas, onde é possível acompanhar os lançamentos realizados por períodos ajustáveis, sendo ainda possível exportação de dados para excel.

#### Produtos:

Nessa aba, pode-se cadastrar os produtos que serão vendidos, inserindo seu **nome**, **valor**, **unidades** e também **uma imagem** que será exibida para os outros usuários que utilizarão o sistema. Também é possível desativar produtos para que não constem na área de vendas

Ainda nessa aba é possível verificar um **histórico**, onde consta todas as modificações realizadas e os usuários que efetuaram cada alteração.
<hr>

### Area Vendas

Nessa area é possível efetuar os lançamentos das vendas dos produtos. Importante ressaltar que há uma forma de pagamento denominada **DEVOLUÇÃO**. Essa forma foi registrada para que se registrem vendas **canceladas/incorretas** (adotamos essa forma, devido aos usuários finais não terem muita aptidão na utilização de sistemas)

Sendo assim, o fluxo da venda segue da seguinte forma: **Produtos e Quantidades > Forma de Pagamento > Conclusão da Venda**
<hr>
<hr>

## <center> Conclusão </center>

Esse sistema foi projetado para utilização simples e fazer um controle básico do caixa local, possibilitando o acompanhamento mais detalhado de entradas e saídas de produtos e as devoluções realizadas. 

Se encoutrou algum problema na utilização ou tem algum ponto de melhoria pode me contactar 😊