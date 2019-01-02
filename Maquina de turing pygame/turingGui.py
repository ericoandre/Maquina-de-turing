'''
Created on 28 de jan de 2017

@author: erico
'''

import pygame
from turing_machine import TuringMachine
import os, time


def divisaosomaBinario(entrada):
    inicio = "s"
    parada = {"h"}
    #estados = {"s","r","t","u","v","x","h"}

    Transicao = {
        ("s",">"):("s","R"),
        ("s","#"):("r","R"),
        ("r","#"):("h","L"),
        ("r","0"):("r","R"),
        ("r","1"):("t","R"),
        ("t","0"):("u","R"),
        ("t","1"):("u","R"),
        ("t","#"):("x","L"),
        ("u","0"):("u","R"),
        ("u","1"):("u","R"),
        ("u","#"):("v","L"),
        ("v","0"):("v","#"),
        ("v","1"):("v","#"),
        ("v","#"):("x","L"),        
        ("x","0"):("x","L"),
        ("x","1"):("x","L"),
        ("x","#"):("h","#")
    }

    maquina(entrada,inicio,parada,Transicao)
def antecessorBinario(entrada):
    inicio = "s"
    parada = {"h"}
    #estados = {"s","r","t","u","v","x","h"}

    Transicao = {
        ("s",">"):("s","R"),
        ("s","#"):("r","R"),

        ("r","0"):("r","R"),
        ("r","1"):("t","R"),
        ("r","#"):("h","L"),

        ("t","0"):("t","R"),
        ("t","1"):("t","R"),
        ("t","#"):("u","L"),

        ("u","0"):("v","1"),
        ("u","1"):("v","0"),
        ("v","1"):("u","L"),
        ("v","0"):("x","L"),

        ("x","0"):("x","L"),
        ("x","1"):("x","L"),
        ("x","#"):("h","#")
    }

    maquina(entrada,inicio,parada,Transicao)
def sucessorBinario(entrada):
    inicio = "s"
    parada = {"h"}
    #estados = {"s","t","p","q","h"}
    #estadosSH = {"z","a","a0","b0","c0","c0","a1","b1","c1","c1"}

    Transicao = {
        ("s",">"):("s","R"),
        ("s","#"):("t","R"),

        #("s","#"):("r","R"),
        #("r","#"):("h","L"),#Verifica se vazio para
        #("r","0"):("t","R"),
        #("r","1"):("t","R"),

        ("t","0"):("t","R"),
        ("t","1"):("t","R"),
        ("t","#"):("p","L"),
        ("p","#"):("z","1"),
        ("p","0"):("q","1"),
        ("p","1"):("q","0"),
        ("q","0"):("p","L"),
        ("q","1"):("h","L"),

        #Shift Transicao
        ("z","0"):("z","R"),
        ("z","1"):("z","R"),
        ("z","#"):("a","L"),

        ("a","0"):("a0","#"),
        ("a","1"):("a1","#"),
        
        ("a0","#"):("b0","R"),
        ("b0","#"):("c0","0"),
        ("c0","0"):("c0","L"),
        ("c0","#"):("a","L"),

        ("a1","#"):("b1","R"),
        ("b1","#"):("c1","1"),
        ("c1","1"):("c1","L"),
        ("c1","#"):("a","L"),

        ("a",">"):("h","R")
    }

    maquina(entrada,inicio,parada,Transicao)
def somaBinario(entrada):
    inicio = "s"
    parada = {"h"}
    #estados = {"s","t","p","q","h"}
    #estadosSH = {"z","a","a0","b0","c0","c0","a1","b1","c1","c1","a+","b+","c+","c+"}

    Transicao = {
        ("s",">"):("s","R"),
        ("s","#"):("t","R"),

        ("t","0"):("t","R"),
        ("t","1"):("t","R"),
        ("t","+"):("j","R"),
        ("t","#"):("h","L"),#final 1

        ("j","0"):("j","R"),
        ("j","1"):("g","R"),
        ("j","#"):("n","L"),

        ("n","0"):("k","#"),#apaga os zeros e o sinal de +        
        ("k","#"):("n","L"),#apaga os zeros e o sinal de +             
        ("n","+"):("h","#"),#apaga os zeros e o sinal de + final 2        

        ("g","0"):("g","R"),
        ("g","1"):("g","R"),
        ("g","#"):("u","L"),


        # antecessor
        ("u","0"):("v","1"),
        ("u","1"):("v","0"),
        ("v","1"):("u","L"),
        ("v","0"):("x","L"),

        ("x","0"):("x","L"),
        ("x","1"):("x","L"),
        ("x","+"):("p","L"),
        

        # sucessor
        ("p","#"):("z","1"),
        ("p","0"):("q","1"),
        ("p","1"):("q","0"),
        ("q","0"):("p","L"),
        ("q","1"):("m","L"),

        ("m","0"):("m","L"),
        ("m","1"):("m","L"),    
        ("m","#"):("s","#"),    
        

        #Shift Transicao
        ("z","0"):("z","R"),
        ("z","1"):("z","R"),
        ("z","+"):("z","R"),
        ("z","#"):("a","L"),

        ("a","0"):("a0","#"),
        ("a","1"):("a1","#"),
        ("a","+"):("a+","#"),
        
        ("a0","#"):("b0","R"),
        ("b0","#"):("c0","0"),
        ("c0","0"):("c0","L"),
        ("c0","#"):("a","L"),

        ("a1","#"):("b1","R"),
        ("b1","#"):("c1","1"),
        ("c1","1"):("c1","L"),
        ("c1","#"):("a","L"),

        ("a+","#"):("b+","R"),
        ("b+","#"):("c+","+"),
        ("c+","+"):("c+","L"),
        ("c+","#"):("a","L"),

        ("a",">"):("s","R")
    }

    maquina(entrada,inicio,parada,Transicao)

def maquina(esntrrada,inicio,parada,Transicao):
    t = TuringMachine(esntrrada, initial_state = inicio, final_states = parada, transition_function=Transicao)
    fita =  t.getFita()
    estado = "s"
    cabesaX = 1

    background = pygame.image.load("tumblr-hipster-backgrounds-wallpapers.jpg")

    pygame.init()

    n = len(fita)+3
    width = 900
    height = 300
    BRANCO = [(255,255,255), (47,47,47) ]
    sq_sz = (width-40)// n
    altura_y = height //2

    surface = pygame.display.set_mode((width, height))
    font = pygame.font.SysFont("Arial", sq_sz)
    clock = pygame.time.Clock()

    estadoFita = ""

    while True:

        if not t.getFinal():
            passos = t.getPassos()
            fita =  t.getFita()
            cabesaX = t.getCabeca()
            estado = t.getEstado()
            estadoFita = str(estado+","+passos[2::])

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        surface.blit(background, (0, 0))


        #surface.fill([75,10,120])
        ind = 0
        for row in range(n):
            pygame.draw.rect(surface, BRANCO[ind], (((row)*sq_sz)+25, (altura_y-sq_sz), sq_sz, sq_sz),0)
            if row < len(fita):
                text = font.render(fita[row], True, (0, 0, 0))
            else:
                text = font.render("#", True, (0, 0, 0))
            surface.blit(text, (((row)*sq_sz)+25, (altura_y-sq_sz), sq_sz, sq_sz))
            ind = (ind + 1) % 2

        altura = 2
        text2 = font.render(estado, True, (255, 255, 255))
        pygame.draw.rect(surface, (0,0,0), (((cabesaX)*sq_sz)+25, (altura_y-sq_sz), sq_sz, sq_sz),1)		
        pygame.draw.rect(surface, (0,0,0), (((cabesaX)*sq_sz)+25, (altura_y), sq_sz, sq_sz),0)	
        surface.blit(text2, (((cabesaX)*sq_sz)+30, altura_y-10, sq_sz, sq_sz)   )

        pygame.display.flip()
        pygame.display.update() 
        time_passed = clock.tick(30)

        if t.getFinal():
            time.sleep(5)
            archivo = open("fita.txt","w")
            vecinos = str (estadoFita)
            archivo.write(vecinos)
            archivo.close()
            break

    pygame.quit()