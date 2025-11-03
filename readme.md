# Mobile-Project - API

<h3>**Projeto voltado à disciplina de "Programação para Dispositivos Móveis em Android".</h3>

## Descrição do Sistema - Gerenciador de Preços com Tarifa Dinâmica para Aplicativo Mobile:

O Gerenciador de Preços com Tarifa Dinâmica é uma solução inteligente voltada à gestão e atualização automática de preços em tempo real, baseada em variáveis contextuais e operacionais. Desenvolvido para integração direta com um aplicativo mobile, o sistema permite que empresas ajustem suas tarifas de forma flexível e estratégica, aumentando a competitividade e otimizando receitas conforme a demanda, disponibilidade e condições de mercado.

<hr/>

<h3>1. Objetivo</h3>

O objetivo principal do sistema é automatizar a definição de preços de produtos ou serviços, substituindo modelos fixos por um mecanismo dinâmico e responsivo. A precificação passa a por mudanças definias pelo usuário, tais como:

1. Horário de maior ou menor demanda;

2. Volume de solicitações simultâneas;

3. Estoque ou capacidade operacional disponível;

4. Localização geográfica e perfil do usuário;

5. Custos variáveis (energia, logística, etc.);

6. Condições externas (clima, trânsito, eventos locais).

Com isso, o gerenciador proporciona preços mais justos e equilibrados, beneficiando tanto o consumidor quanto o fornecedor.

<hr />

<h3>2. Funcionamento Geral</h3>

Camada IoT (Wokwi / ESP32)<br/>
No ambiente de simulação Wokwi, o ESP32 + MicroPython coleta dados mediante servidor, por chamada de API central, para exibição e atualização pré-definida pelo manager atualizando automaticamente os parâmetros que influenciam o valor do produto.<br/>
Ex: Incidência de impostos que somam ao preço final, aumento do custo do produto, etc...

Camada de Backend (CRUD + API)
O servidor backend oferece um sistema CRUD completo:

Create: cadastro de produtos e regras tarifárias;

Read: leitura e listagem de produtos cadastrados;

Update: atualização manual de preços;

Delete: exclusão de registros e configurações antigas.
Esse backend processa os dados recebidos do aplicativo, gerenciado pelo manager, e aplica as fórmulas de precificação dinâmica, atualizando os valores disponíveis na base de dados que serão apresentados na etiqueta.

Camada Mobile (Aplicativo)
O aplicativo mobile consome a API do sistema e exibe os preços atualizados em tempo real.
Nele, o usuário pode visualizar:

1. O produto disponível,

2. O valor dinâmico calculado no momento,

3. Realizar alterações dos valores dos produtos, alimentando a base de dados que, por sua vez, será consultada pela etiqueta e esta atualizada.

Essa camada garante a interface intuitiva e a interação direta com o usuário final (neste caso, o manager), representando a face visível do sistema, e permitindo o gerenciamento dos valores dos produtos na palma da mão.

```scss
[ Aplicativo Mobile ] -> Administradores 
        ↓ (envio de dados)
[ API / Backend CRUD ] 
        ↓ (atualização de preço)
[ Banco de Dados Dinâmico ]
        ↓ (consulta)
[ Wokwi / ESP32 ] -> Etiqueta
```

<h3>3. Beneficios do Sistema</h3>

1. **Automação** > Atualiza preços automaticamente conforme condições coletadas pelo ESP32 (simulado).

2. **Flexibilidade** > CRUD permite alterar regras, produtos e tarifas de forma simples e sem intervenção técnica.

3. **Realismo e Teste com Uso do Wokwi** > O hardware exibe dinamicamente as variações de preço, tornando o sistema perceptível ao usuário final.

4. **Interatividade** > Total controle na mão do administrador (manager) do estabelecimento, permitindo alterar preços instantaneamente à sua vontade.

5. **Escalabilidade** > Pode ser expandido para cenários reais com dispositivos físicos e integração em nuvem.

<h3>4. Tecnologias Envolvidas</h3>

- **IoT:** ESP32 simulado no **Wokwi**  
- **Linguagem embarcada:** MicroPython  
- **Backend/API:** Python3 **Flask** com **CRUD**  
- **Banco de Dados:** SQLAlchemy  
- **Aplicativo Mobile:** React Native (Em desenvolvimento) 
- **Comunicação:** HTTP/HTTPS via **REST API** (com tunelamento NGROK)

<h3>5. Iniciar o Projeto</h3>

- **Etiqueta Dinâmica**: Presente no Wokwi -> https://wokwi.com/projects/442944732466660353</br>
É importante alterar o host do projeto vide tunelamento NGROK

- **Clone o repositório**: Serviço para simular o Backend e Bando de Dados

```bash
#Codigo git clone entra depois

cd MOBILE_API

pip3 install -r requirements.txt

python3 main.py
```

- **Expor API local**: Necessário para conectar com o WOKWI</br>
Caso não o obtenha, visite: https://ngrok.com/

```bash

ngrok http 5000 --scheme=http

#Saída esperada:
#Forwarding                    http://exemplo.ngrok-free.app -> http://localhost:5000

#descrição:
#Forwarding                    http://<host> -> http://localhost:5000      

```
- **INTERFACE MOBILE AINDA EM DESENVOLVIMENTO, VOLTE AMANHA**