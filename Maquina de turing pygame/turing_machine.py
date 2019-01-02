'''
Created on 28 de jan de 2017

@author: erico
'''
import time

class Tape(object):
    blank_symbol = "#"    
    def __init__(self, tape_string = ""): 
        tape_string = ">#"+tape_string
        self.__tape = {}
        for i in range(len(tape_string)):
            self.__tape[i] = tape_string[i]

    def __str__(self):
        s = ""
        for k,x in self.__tape.items():
            s += x
        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

class TuringMachine(object):
    
    def __init__(self,tape = "", blank_symbol = " ",initial_state = "",final_states = None,transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
    
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)

        self.fitaType=""

    def getEstado(self):
        return self.__current_state

    def getCabeca(self):
        return self.__head_position

    def getFita(self): 
        return str(self.__tape)
    
    def getPassos(self):
        char_under_head = self.__tape[self.__head_position]
        
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]


            self.string = str(self.__tape)
            if self.__head_position < len(self.string):         
                if self.__head_position != 0:
                    self.fitaType = str(self.__current_state)+","+self.string[:self.__head_position]+"["+self.string[self.__head_position]+"]"+self.string[self.__head_position+1:]
                else:
                    self.fitaType =  str(self.__current_state)+",["+self.string[self.__head_position]+"]"+self.string[self.__head_position+1:]
            elif self.__head_position >= len(self.string):
                self.fitaType = str(self.__current_state)+","+self.string[:self.__head_position]+"[#]"

           
            if y[1] == "R":
                self.__head_position += 1
            elif y[1] == "L":
                self.__head_position -= 1
            else:
                self.__tape[self.__head_position] = y[1]
            self.__current_state = y[0]


            self.string = str(self.__tape)
            if self.__head_position < len(self.string):         
                if self.__head_position != 0:
                    self.fitaType = str(self.__current_state)+","+self.string[:self.__head_position]+"["+self.string[self.__head_position]+"]"+self.string[self.__head_position+1:]
                else:
                    self.fitaType =  str(self.__current_state)+",["+self.string[self.__head_position]+"]"+self.string[self.__head_position+1:]
            elif self.__head_position >= len(self.string):
                self.fitaType = str(self.__current_state)+","+self.string[:self.__head_position]+"[#]"


            time.sleep(1)
            return self.fitaType


    def getFinal(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False
        