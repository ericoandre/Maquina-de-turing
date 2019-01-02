#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from turingGui import *

root = Tk()

countrynames = ('Soma','Divisao', 'Antecessor','Sucessor')

cnames = StringVar(value=countrynames)

sentmsg = StringVar()
statusmsg = StringVar()
ent = StringVar()


def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]

        if name == "Soma":
            sentmsg.set("Entrada ex: 11111+11")
        else:
            sentmsg.set("Entrada ex: 111")


def iniciar():
	fita = ent.get()
	idxs = lbox.curselection()
	if fita != "":
		operacao = countrynames[idxs[0]]

		if operacao == "Divisao":
			divisaosomaBinario(ent.get())
		elif  operacao == "Antecessor":
			antecessorBinario(ent.get())
		elif operacao == "Sucessor":
			sucessorBinario(ent.get())
		elif operacao == "Soma":
			somaBinario(ent.get())

		archivo = open("fita.txt","r")
		lista = archivo.read()
		archivo.close()

		sentmsg.set(lista)


# Cria grades 
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

root.title("Turing")

# itens e formes 
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Digite A Entrada da Fita:")

send = ttk.Button(c, text='Inicia', command=iniciar, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)
entrada = Entry(c, textvariable=ent, width=30).grid(column=1, row=1, sticky=W, padx=20)


# posicao dos itens da tela
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=0, pady=5)

send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5,  sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)


lbox.bind('<<ListboxSelect>>', sendGift)
root.bind('<Return>', iniciar)

# Funcao de zebra para o liste box
for i in range(0,len(countrynames),2):
    lbox.itemconfigure(i, background='#f0f0ff')


sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)


root.mainloop()