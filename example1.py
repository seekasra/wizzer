"""example file"""

from wizzer import Wizzer

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
questions = wizzer.ask(q1)
wizzer.review(questions)
