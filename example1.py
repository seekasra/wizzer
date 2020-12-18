"""example file"""

from wizzer import *

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

q = ask(q1)
review(q)
