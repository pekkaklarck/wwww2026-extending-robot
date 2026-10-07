*** Settings ***
Library           Advanced.py    state=initial

*** Variables ***
${PASSWORD: Secret}     %{ROBOT_PASSWORD=pwd123}

*** Test Cases ***
Library state
    State should be    initial
    Set state    new
    State should be    new

Library state 2
    State should be    new

Custom keyword names
    Hello!
    🤖

Embedded arguments
    This is good example
    This is bad example
    This is ugly example

Restricting arguments with Literal
    Move    UP
    Move    left
    Move    bad

Restricting arguments with Enum
    Turn    UP
    Turn    left
    Turn    bad

Custom argument conversion
    Workshop    7.10.2026
    Workshop    bad

Secrets
    Login    robot    ${PASSWORD}
