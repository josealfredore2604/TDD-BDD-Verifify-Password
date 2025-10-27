# Verificación de Fortaleza de Contraseñas — TDD y BDD

La empresa **SecureApp** está desarrollando un módulo para verificar la fortaleza de contraseñas dentro de su sistema de registro de usuarios.
El propósito es garantizar que las contraseñas cumplan con los requisitos mínimos de seguridad antes de permitir el registro.
El sistema debe analizar la contraseña ingresada y devolver un mensaje que indique si la contraseña es **fuerte**, **débil** o **inválida**, según los criterios establecidos.

---

## Objetivo

Aplicar los enfoques **TDD (Test-Driven Development)** y **BDD (Behavior-Driven Development)** para guiar el desarrollo del módulo de verificación de contraseñas.
El proceso incluye la elaboración de pruebas unitarias, la implementación del código funcional y la definición de escenarios de comportamiento en lenguaje **Gherkin**.

---

## Enfoque TDD

1. Crear un archivo llamado **`test_password.py`**.
2. Escribir las pruebas unitarias antes de implementar el código.
3. Las pruebas deben verificar los siguientes comportamientos:

   * Cuando la contraseña cumple con todos los requisitos.
   * Cuando la contraseña no cumple con uno o más requisitos.
   * Cuando el campo de contraseña está vacío.
4. Implementar la función **`verify_password(password)`** en un archivo **`app.py`**, asegurando que todas las pruebas pasen correctamente.

---

## Enfoque BDD

1. Crear un archivo **`password.feature`** utilizando lenguaje **Gherkin**, describiendo el comportamiento esperado del sistema desde la perspectiva del usuario.
2. Incluir los pasos:

   * **Given** las condiciones iniciales del sistema.
   * **When** el usuario ingresa una contraseña.
   * **Then** el sistema muestra el resultado esperado.
3. Implementar los pasos correspondientes en Python utilizando **behave** o **pytest-bdd**, dentro de un archivo **`password_steps.py`**, de modo que la ejecución del escenario confirme el comportamiento correcto del sistema.

---

## Requerimientos Funcionales

* Si la contraseña tiene **al menos ocho caracteres**, **incluye una letra mayúscula** y **al menos un número**, debe devolver:

  ```
  Strong password
  ```

* Si no cumple con uno o más de estos criterios, debe devolver:

  ```
  Weak password
  ```

* Si el campo está vacío, debe devolver:

  ```
  Password required
  ```

---

## Archivos del Proyecto

* `app.py` → Implementación de la función principal `verify_password()`.
* `test_password.py` → Pruebas unitarias (TDD).
* `password.feature` → Escenario BDD escrito en Gherkin.
* `password_steps.py` → Implementación en Python de los pasos definidos en el escenario BDD.
