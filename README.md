![wizzer logo](https://raw.githubusercontent.com/seekasra/wizzer/main/cover.png) 
[<img style="float: left; margin: 10px 10px 0px 0px" src="https://img.shields.io/github/last-commit/seekasra/wizzer.svg">](https://github.com/seekasra/wizzer/commits/master) [<img style="float: left; margin: 10px 10px 0px 0px" src="https://img.shields.io/github/license/seekasra/wizzer.svg">](https://github.com/seekasra/wizzer/blob/master/LICENSE)[![stability][0]][1] [![HitCount](http://hits.dwyl.com/seekasra/wizzer.svg)](http://hits.dwyl.com/seekasra/wizzer)

<br/>
# wizzer 
#### [What's wizzer?](#whats-wizzer)
#### [How to use?](#how-to-use)
#### [Credits](#credits)
---

### What's wizzer?
wizzer is a Python module to help programmers initialise their domain specific
variable(s)/configuration(s) using a wizard-like question answer chat scenario.
The need for this module began to develope when there was such need for
Intent-Based Networking (IBN). Where the user would express their intention and
expect the system to translate and trigger setup automatically.

** This is a pre-LLM era repository.

### How to use?
1. import _wizzer_ package.


```python
import wizzer
```

2. have your questions (configuration parameters) ready. accepted formats are arrays, dictionaries or a single string. You can also pass the questions to "convert module" to get back a ready to use dictionary. 

    - Here we have an array forexample:


```python
q1 = [
        'driver',
        'hostname',
        'username',
        'password',
        'port',
]
```

   - Now you can ask above attributes from the user. This will return a new dictinary with all answers filled-in as corresponding values.


```python
q = wizzer.ask(q1)
```

    What's the driver ?  iosxr
    What's the hostname ?  ios-xe-mgmt.cisco.com
    What's the username ?  developer
    What's the password ?  C1sco12345
    What's the port ?  8181


 - You can review the configurations by running:


```python
wizzer.review(q)
```

    driver :  iosxr
    hostname :  ios-xe-mgmt.cisco.com
    username :  developer
    password :  C1sco12345
    port :  8181


3. Here we have a dictionary forexample:


```python
q2 = {
        'driver': '',
        'hostname': '',
        'username': '',
        'password': '',
        'port': '',
}
```

- Now you can ask above attributes from the user. This will return a new dictinary with all answers filled-in as corresponding values.


```python
q = wizzer.ask(q2)
```

    What's the driver ?  iosxr
    What's the hostname ?  ios-xe-mgmt.cisco.com
    What's the username ?  developer
    What's the password ?  C1sco12345
    What's the port ?  8181


- You can review the configurations by running:


```python
wizzer.review(q2)
```

    driver :  iosxr
    hostname :  ios-xe-mgmt.cisco.com
    username :  developer
    password :  C1sco12345
    port :  8181


---
### credits
Icon in the wizzer logo by [Anatoly Dudko](https://thenounproject.com/tolyachudes/)

[0]: https://img.shields.io/badge/stability-experimental-orange.svg?style=flat-square
[1]: https://nodejs.org/api/documentation.html#documentation_stability_index
