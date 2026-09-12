#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:45:43 2026

@author: ime_rasenberg
"""

# Simulation of a falling body on Earth
ACCELERATION_G = 9.8 # m/s^2
TIME = 5.0 # seconds
def calculate_displacement(g, t):
    return 0.5 * g * (t ** 2)

print(f"Displacement after {TIME}s: {calculate_displacement(ACCELERATION_G, TIME)} meters")