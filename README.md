# 🍔 Mate Lanches

Aplicativo de PDV (ponto de venda) para uma lanchonete fictícia, feito em Python com interface gráfica usando **CustomTkinter**. Permite navegar pelo cardápio, montar um carrinho, escolher a forma de pagamento (Pix, Crédito ou Débito) e salvar o histórico de pedidos em um arquivo `pedidos.json`.

## ✨ Funcionalidades

- Cardápio com 20 itens e preços pré-definidos
- Carrinho de compras com cálculo automático de subtotal e total
- Cálculo de troco a partir do valor pago
- Escolha da forma de pagamento (Pix / Crédito / Débito)
- Histórico de pedidos persistido em `pedidos.json`
- Interface escura usando tema `dark` do CustomTkinter

## 📋 Requisitos

- **Python 3.10+** (recomendado)
- **Tkinter**
- Dependência externa: [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)

## 🚀 Instalação

### 1. Clone ou baixe o projeto

```bash
git clone <url-do-repositorio>
cd mate-lanches
```

### 2. Crie um ambiente virtual

**Windows (PowerShell / CMD):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

Usando `pip`:
```bash
pip install customtkinter
```

Ou usando [`uv`](https://github.com/astral-sh/uv) (mais rápido):
```bash
uv pip install customtkinter
```

## ▶️ Como executar

Com o ambiente virtual ativado, rode:

```bash
python main.py
```

A janela do aplicativo (1200x700) deve abrir com o cardápio à esquerda e o carrinho à direita.

## 🧾 Como usar

1. Clique em **Adicionar** ao lado de um item para incluí-lo no carrinho.
2. O total é atualizado automaticamente.
3. Digite o **Valor pago** no campo da direita.
4. Clique em **💳 Finalizar Compra** e escolha a forma de pagamento.
5. Confirme — o pedido será salvo em `pedidos.json` e o troco será exibido.
6. Use **🗑 Limpar Carrinho** para começar um novo pedido.

## 📁 Estrutura

```
mate-lanches/
├── main.py          # Aplicação principal (UI + lógica)
├── pedidos.json     # Histórico de pedidos (criado em runtime)
└── README.md
```

## 🛠 Tecnologias

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — UI moderna baseada em Tkinter
- `json` e `datetime` (biblioteca padrão) — para persistência e timestamps
