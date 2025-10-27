Feature: Verificación de fortaleza de contraseñas
  Como usuario del sistema
  Quiero que mi contraseña sea verificada
  Para asegurarme de que cumple con los criterios de seguridad

  Scenario: Contraseña fuerte
    Given que el usuario ingresa una contraseña válida
    When la contraseña es "Secure123"
    Then el sistema debe devolver "Strong password"

  Scenario: Contraseña débil
    Given que el usuario ingresa una contraseña válida
    When la contraseña es "abc"
    Then el sistema debe devolver "Weak password"

  Scenario: Campo vacío
    Given que el usuario no ingresa ninguna contraseña
    When la contraseña es ""
    Then el sistema debe devolver "Password required"
