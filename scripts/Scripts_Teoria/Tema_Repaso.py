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

letters = set( [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ] )


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

# Problema 1-1
Sol_P1 = [ val for val in itertools.permutations( "ABCDEFGHIJ", 4 ) ]


# Problema 1-2
Sol_P2 = [ val for val in itertools.combinations( D , 3 ) ]


# Problema 1-3
Sol_P3 = [ val for val in itertools.permutations( E , 4 ) ]


# Problema 1-4
Sol_P4 = [ val for val in itertools.permutations( set( range(1, 51) ) , 2 ) ]


# Problema 1-5
Sol_P5 = [ val for val in itertools.combinations( set( range(1, 12) ) , 5 ) ]

# Problema 1-6
Sol_P6 = math.factorial( 13 )


# Problema 1-10
Sol_P10 = [ val for val in itertools.combinations_with_replacement( set( [ "AMARILLO", "AZUL", "NARANJA", "ROJO" ] ) , 2 ) ]


# Problema 1-12
Sol_P12 = []
Sol_P12_1 = [ val for val in itertools.combinations( set( range(1,11) ) , 3 ) ]
Sol_P12_2 = [ val for val in itertools.combinations( set( [ "E1", "E2", "E3", "E4", "E5", "E6" ] ) , 2 ) ]


for val_1 in Sol_P12_1:
    for val_2 in Sol_P12_2:
        Sol_P12.append( list( val_1 ) + list( val_2 )  )




# Problema 2-2
Sol_P2_2 = [ val for val in itertools.permutations( set( [ "P1", "P2", "P3", "P4", "P5", "P6" ] ) , 6 ) ]


# Problema 2-3 - Caso A
Sol_P2_3 = [ val for val in itertools.permutations( set( [ "P1", "P2", "P3", "N" ] ) , 4 ) ]


# Problema 2-4
Sol_P2_4 = [ val for val in itertools.combinations( set( range(1, 16) ) , 2 ) ]


# Problema 2-5
Sol_P2_5 = [ val for val in itertools.permutations( set( [ "A", "A",
                                                          "B", "B", "B", "B", 
                                                          "C", "C", "C", "C" ] ) , 3 ) ]



# Problema 2-6
Sol_P2_6_let = [ val for val in itertools.product( letters , repeat=3 ) ]
Sol_P2_6_Number = [ val for val in itertools.product( set( range(0, 10) ) , repeat=3 ) ]

" Be Careful, the result have more than 1 million of elements "
Sol_P2_6 = []
for val_1 in Sol_P2_6_let:
    for val_2 in Sol_P2_6_Number:
        Sol_P2_6.append( list( val_1 ) + list( val_2 )  )


# Problema 2-7
Sol_P2_7 = [ val for val in itertools.combinations( set( [ "E1", "E2", "E3", "E4",
                                                           "E5", "E6", "E7", "E8" ] ) , 2 ) ]



# Problema 2-4
Sol_P2_4 = [ val for val in itertools.combinations( set( range(1, 7) ) , 0 ) ]

