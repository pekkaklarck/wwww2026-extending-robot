*** Settings ***
Library         LibraryWithListener.py

*** Test Cases ***
Passing
    Log    Hello, world!
    Set status    new

Failing
    Set status    newer
    Fail    Something bad happened!

Passing again
    Log    Hello, again!
    Keyword

*** Keywords ***
Keyword
    No Operation
