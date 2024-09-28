Feature: Login happy path

    @happyPath
    Scenario: Happy path
        Given Open browser
        When Ingresa username "qualityadmin" y password "pass1"
        Then Inicio exitoso