"""example file"""

from Wizzer import Wizzer

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

wizzer = Wizzer()
q = wizzer.ask(q1)
wizzer.review(q)
