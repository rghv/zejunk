#!/usr/bin/env python

#This is a silly greeter

class SillyGreeter (object):
    '''
    Silly greeter class
    '''
    __greetMsg = "DEFAULT GREET MSG"
    def __init__ (self, msg):
        if msg:
            self.__greetMsg = msg

    def ret_greet(self):
        return self.__greetMsg

if __name__ == '__main__':
    s = SillyGreeter(" HOLA! ")
    print s.ret_greet()

