# wizzer
![wizzer logo](https://raw.githubusercontent.com/seekasra/wizzer/main/cover.png)

[<img style="float: left; margin: 0px 10px 0px 0px" src="https://img.shields.io/github/last-commit/seekasra/wizzer.svg">](https://github.com/seekasra/wizzer/commits/master) [<img style="float: left;" src="https://img.shields.io/github/license/seekasra/wizzer.svg">](https://github.com/seekasra/wizzer/blob/master/LICENSE)
<br/>

### What's wizzer?
wizzer is a Python module to help programmers initialise their domain specific
variable(s)/configuration(s) using a wizard-like question answer chat scenario.
The need for this module began to develope when there was such need for
Intent-Based Networking (IBN). Where the user would express their intention and
expect the system to translate and trigger setup automatically.
### How to use?
1 - import _wizzer_ package.


```python
import wizzer
```

2 - have your questions (configuration parameters) ready. accepted formats are arrays, dictionaries or a single string.
<br/> 2.1 - Here we have an array forexample:


```python
q1 = [
        'driver',
        'hostname',
        'username',
        'password',
        'port',
]
```

2.1.1 - Now you can ask above attributes from the user. This will return a new dictinary with all answers filled-in as corresponding values.


```python
q = wizzer.ask(q1)
```

    What's the driver ?  iosxr
    What's the hostname ?  ios-xe-mgmt.cisco.com
    What's the username ?  developer
    What's the password ?  C1sco12345
    What's the port ?  8181


2.1.2 - You can review the configurations by running:


```python
wizzer.review(q)
```

    driver :  iosxr
    hostname :  ios-xe-mgmt.cisco.com
    username :  developer
    password :  C1sco12345
    port :  8181


2.2 - Here we have a dictionary forexample:


```python
q2 = {
        'driver': '',
        'hostname': '',
        'username': '',
        'password': '',
        'port': '',
}
```

2.2.1 - Now you can ask above attributes from the user. This will return a new dictinary with all answers filled-in as corresponding values.


```python
q = wizzer.ask(q2)
```

    What's the driver ?  iosxr
    What's the hostname ?  ios-xe-mgmt.cisco.com
    What's the username ?  developer


---
### credits
Icon in the wizzer logo by [Anatoly Dudko](https://thenounproject.com/tolyachudes/)
