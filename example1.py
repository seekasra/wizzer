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

q = wizzer.ask(q1)
wizzer.review(q)

