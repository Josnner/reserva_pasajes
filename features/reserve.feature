Feature: Reservar pasaje
    Como usuario
    Quiero reservar un pasaje
    para irme a Paris

    @happyReserve
    Scenario: happyReserve
        Given Open browser reserve
        When Fill in the fields
        Then Can flight