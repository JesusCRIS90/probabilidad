#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:03:13 2021

@author: jesus
"""

Omega = set( [1,2,3,4,5,6,7,8,9,10] )
A = set( [1,2,3,4,5] )
B = set( [1,4,5] )
C = set( [4,6,7,8] )

A & B   # intersección (&: and/y)
A | B   # unión (|: or/o)
A - C   # diferencia 
Omega-C # complementario.