#!/usr/bin/python3
from gpiozero import CPUTemperature

cpu = CPUTemperature()
print(cpu.temperature)

