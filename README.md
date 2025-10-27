# Verificación de Fortaleza de Contraseñas

Este proyecto implementa un módulo para verificar la fortaleza de contraseñas dentro de un sistema de registro de usuarios.  
Está desarrollado aplicando los enfoques **TDD (Test-Driven Development)** y **BDD (Behavior-Driven Development)** utilizando **Python**, **pytest** y **behave**.

---

## Tecnologías utilizadas

- **Python 3.12**
- **pytest** → para pruebas unitarias (TDD)
- **behave** → para pruebas de comportamiento (BDD)
- **venv** → entorno virtual de Python

---

## Estructura del proyecto

```

.
├── app.py
├── Enunciado.md
├── features
│   ├── password.feature
│   └── steps
│       └── password_steps.py
├── **pycache**
├── test_password.py

````

---

## Cómo ejecutar el proyecto

### 1. Crear y activar el entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate     # En Linux o macOS
# .venv\Scripts\activate      # En Windows
````

### 2. Instalar las dependencias necesarias

```bash
pip install pytest behave
```

### 3. Ejecutar las pruebas unitarias (TDD)

```bash
pytest
```

### 4. Ejecutar las pruebas de comportamiento (BDD)

```bash
behave
```

---

## Descripción general

El sistema analiza una contraseña y devuelve uno de los siguientes mensajes:

* **"Strong password"** → cuando la contraseña tiene al menos 8 caracteres, una letra mayúscula y un número.
* **"Weak password"** → cuando no cumple con uno o más de los criterios.
* **"Password required"** → cuando el campo está vacío.

---

## Archivos principales

* `app.py` → Contiene la función `verify_password()`.
* `test_password.py` → Pruebas unitarias bajo TDD.
* `features/password.feature` → Escenarios en lenguaje Gherkin (BDD).
* `features/steps/password_steps.py` → Implementación de los pasos BDD en Python.
* `Enunciado.md` → Documento con la descripción completa del ejercicio.

---

## Resultados esperados

Al ejecutar `pytest` y `behave`, todos los casos deben pasar correctamente mostrando un comportamiento coherente con los criterios definidos para la validación de contraseñas.
