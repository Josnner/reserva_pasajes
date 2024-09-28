Feature: Register user
    Como user
    Quiero registrarme en la pagina
    Para poder reservar pasajes

    @HappyPathRegister
    Scenario: HappyPathregister
        Given Usuario navega en la pagina
        When Usuario llena introduce sus datos
        Then Usuario registrado