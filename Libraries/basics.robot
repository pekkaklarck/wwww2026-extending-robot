*** Settings ***
Library           basics.py

*** Test Cases ***
Simple keyword
    Simple keyword

Arguments
    One argument    Robot
    Default values    Robot
    Default values    Robot    Hi
    Default values    Robot    greeting=Hi
    Varargs
    Varargs    a
    Varargs    a    b    c    d

Argument conversion
    Argument conversion    2026-10-07 10:00    7 hours

Status
    Should be positive    1
    Should be positive    1.3
    Should be positive    -1

Logging
    Log using print
    Log using API

Returning values
    ${value} =    Return something
    Should be equal    ${value}    something
