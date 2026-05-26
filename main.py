import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MateLanchesApp:
    def __init__(self):
        self.janela = ctk.CTk()
        self.janela.title("🍔 Mate Lanches")
        self.janela.geometry("1200x700")

        self.cardapio = {
            "X-Burguer": 18,
            "X-Salada": 20,
            "X-Bacon": 24,
            "X-Tudo": 30,
            "Hot Dog": 15,
            "Batata Frita": 12,
            "Batata Cheddar": 18,
            "Nuggets": 16,
            "Pizza Brotinho": 25,
            "Coxinha": 8,
            "Pastel": 10,
            "Açaí": 22,
            "Milkshake": 20,
            "Sorvete": 12,
            "Refrigerante": 7,
            "Suco Natural": 9,
            "Água": 4,
            "Combo Família": 65,
            "Onion Rings": 14,
            "Brownie": 11
        }

        self.carrinho = {}

        self.build_ui()
        self.janela.mainloop()

    # ---------------- UI ----------------
    def build_ui(self):
        self.frame_left = ctk.CTkFrame(self.janela)
        self.frame_left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.frame_right = ctk.CTkFrame(self.janela, width=350)
        self.frame_right.pack(side="right", fill="y", padx=10, pady=10)

        ctk.CTkLabel(
            self.frame_left,
            text="🍔 Mate Lanches",
            font=("Arial", 28, "bold")
        ).pack(pady=10)

        self.scroll = ctk.CTkScrollableFrame(self.frame_left)
        self.scroll.pack(fill="both", expand=True)

        self.build_cardapio()
        self.build_carrinho()

    def build_cardapio(self):
        for nome, preco in self.cardapio.items():
            frame = ctk.CTkFrame(self.scroll)
            frame.pack(fill="x", pady=5)

            ctk.CTkLabel(
                frame,
                text=f"{nome} - R$ {preco:.2f}",
                font=("Arial", 16)
            ).pack(side="left", padx=10)

            ctk.CTkButton(
                frame,
                text="Adicionar",
                command=lambda n=nome: self.add_item(n)
            ).pack(side="right", padx=5)

    def build_carrinho(self):
        ctk.CTkLabel(
            self.frame_right,
            text="🛒 Carrinho",
            font=("Arial", 22, "bold")
        ).pack(pady=10)

        self.texto = ctk.CTkTextbox(self.frame_right, height=300)
        self.texto.pack(pady=10)

        self.total_label = ctk.CTkLabel(
            self.frame_right,
            text="Total: R$ 0.00",
            font=("Arial", 18, "bold")
        )
        self.total_label.pack()

        self.entry_pagamento = ctk.CTkEntry(
            self.frame_right,
            placeholder_text="Valor pago"
        )
        self.entry_pagamento.pack(pady=10)

        ctk.CTkButton(
            self.frame_right,
            text="💳 Finalizar Compra",
            command=self.finalizar
        ).pack(pady=5)

        ctk.CTkButton(
            self.frame_right,
            text="🗑 Limpar Carrinho",
            command=self.limpar
        ).pack(pady=5)

    # ---------------- Carrinho ----------------
    def add_item(self, nome):
        if nome in self.carrinho:
            self.carrinho[nome]["qtd"] += 1
        else:
            self.carrinho[nome] = {
                "preco": self.cardapio[nome],
                "qtd": 1
            }

        self.update()

    def limpar(self):
        self.carrinho.clear()
        self.update()

    def update(self):
        self.texto.delete("1.0", "end")

        total = 0

        for nome, info in self.carrinho.items():
            subtotal = info["preco"] * info["qtd"]
            total += subtotal

            self.texto.insert(
                "end",
                f"{nome} x{info['qtd']} - R$ {subtotal:.2f}\n"
            )

        self.total_label.configure(text=f"Total: R$ {total:.2f}")

    # ---------------- FINALIZAÇÃO ----------------
    def finalizar(self):
        if not self.carrinho:
            messagebox.showwarning("Aviso", "Carrinho vazio!")
            return

        total = sum(i["preco"] * i["qtd"] for i in self.carrinho.values())
        self.escolher_pagamento(total)

    def escolher_pagamento(self, total):
        self.popup = ctk.CTkToplevel(self.janela)
        self.popup.title("Forma de Pagamento")
        self.popup.geometry("300x250")
        self.popup.grab_set()

        ctk.CTkLabel(
            self.popup,
            text="Escolha a forma de pagamento:",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        self.metodo = ctk.StringVar(value="Pix")

        ctk.CTkRadioButton(
            self.popup,
            text="Pix",
            variable=self.metodo,
            value="Pix"
        ).pack(pady=5)

        ctk.CTkRadioButton(
            self.popup,
            text="Crédito",
            variable=self.metodo,
            value="Crédito"
        ).pack(pady=5)

        ctk.CTkRadioButton(
            self.popup,
            text="Débito",
            variable=self.metodo,
            value="Débito"
        ).pack(pady=5)

        ctk.CTkButton(
            self.popup,
            text="Confirmar",
            command=lambda: self.confirmar_pagamento(total)
        ).pack(pady=15)

    def confirmar_pagamento(self, total):
        self.popup.destroy()

        try:
            pago = float(self.entry_pagamento.get())
        except:
            messagebox.showerror("Erro", "Valor inválido")
            return

        if pago < total:
            messagebox.showerror("Erro", "Pagamento insuficiente")
            return

        troco = pago - total
        metodo = self.metodo.get()

        pedido = {
            "data": str(datetime.now()),
            "itens": self.carrinho,
            "total": total,
            "pago": pago,
            "troco": troco,
            "pagamento": metodo
        }

        if os.path.exists("pedidos.json"):
            with open("pedidos.json", "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except:
                    dados = []
        else:
            dados = []

        dados.append(pedido)

        with open("pedidos.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        messagebox.showinfo(
            "Finalizado",
            f"Pagamento: {metodo}\nTotal: R$ {total:.2f}\nTroco: R$ {troco:.2f}"
        )

        self.limpar()
        self.entry_pagamento.delete(0, "end")


MateLanchesApp()