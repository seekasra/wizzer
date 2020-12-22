# -*- coding: utf-8 -*-
"""example file"""
import wizzer

q1 = [
        'hostname',
        'Username',
        'Interface Config',
        'Static Route',
        'Routing protocol',
]

q2 = {
        'hostname': '',
        'Username': '',
        'Interface Config': '',
        'Static Route': '',
        'Routing protocol': '',
}

questions = wizzer.ask(q1)
wizzer.review(questions)
