#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:03:13 2021

@author: jesus
"""

import itertools
import math

Omega = set( [1,2,3,4,5,6,7,8,9,10] )
A = set( [1,2,3,4,5] )
B = set( [1,4,5] )
C = set( [4,6,7,8] )
D = set( [ "VERDE", "AMARILLO", "AZUL", "ROSA", "NARANJA", "ROJO" ] )

E = set( [ "B", "Y", "T", "E" ] )

E = set( range(1, 51) )

A & B   # intersección (&: and/y)
A | B   # unión (|: or/o)
A - C   # diferencia 
Omega-C # complementario.


b = [ val for val in itertools.product( "ABCD", repeat = 4 ) ]

c = [ val for val in itertools.permutations( "ABCDEFGHIJ", 4 ) ]

d = [ val for val in itertools.combinations( "ABCD", 4 ) ]

e = [ val for val in itertools.combinations_with_replacement( "ABCD", 2 ) ]


f = [ val for val in itertools.product( D, repeat = 4 ) ]


"  Soluciones Problemas Propuesto Tema 0 "

# Problema 1
Sol_P1 = [ val for val in itertools.permutations( "ABCDEFGHIJ", 4 ) ]


# Problema 2
Sol_P2 = [ val for val in itertools.combinations( D , 3 ) ]


# Problema 3
Sol_P3 = [ val for val in itertools.permutations( E , 4 ) ]


# Problema 4
Sol_P4 = [ val for val in itertools.permutations( set( range(1, 51) ) , 2 ) ]


# Problema 5
Sol_P5 = [ val for val in itertools.combinations( set( range(1, 12) ) , 5 ) ]

# Problema 6
Sol_P6 = math.factorial( 13 )



# Problema 10
Sol_P10 = [ val for val in itertools.combinations_with_replacement( set( [ "AMARILLO", "AZUL", "NARANJA", "ROJO" ] ) , 2 ) ]



# Problema 12
Sol_P12 = []
Sol_P12_1 = [ val for val in itertools.combinations( set( range(1,11) ) , 3 ) ]
Sol_P12_2 = [ val for val in itertools.combinations( set( [ "E1", "E2", "E3", "E4", "E5", "E6" ] ) , 2 ) ]


for val_1 in Sol_P12_1:
    for val_2 in Sol_P12_2:
        Sol_P12.append( list( val_1 ) + list( val_2 )  )




