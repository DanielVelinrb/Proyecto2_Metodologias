# Arquitectura del Producto - Calculadora en Terminal de Python

## 1. Interfaz de Usuario (UI)

**Responsabilidades:**

- Interacción con el usuario a través de la línea de comandos.
- Presentación de la calculadora y sus funcionalidades.
- Captura de las entradas del usuario y muestra de los resultados.

**Tecnología:**

- Biblioteca estándar de Python para entrada/salida (por ejemplo, input() y print())
- Biblioteca de Python para realziar calculo(raiz, log, sen, cos, tan).

## 2. Controlador (Controller)

**Responsabilidades:**

- Recibe las solicitudes y operaciones ingresadas por el usuario.
- Valida las entradas del usuario.
- Coordina las llamadas a los módulos de cálculo correspondientes.

**Tecnología:**
  Python estándar para la programación estructurada.

## 3. Módulo Base de Cálculos (Core Calculation Module)

**Responsabilidades:**

- Realiza operaciones matemáticas básicas (suma, resta, multiplicación y división).
- Ejecuta operaciones trigonométricas.

**Tecnología:**

- Implementado en Python estándar sin necesidad de bibliotecas externas.

## 4. Módulo de Cálculos Avanzados (Advanced Calculation Module)

**Responsabilidades:**

- Realiza operaciones avanzadas como raíces, exponenciales y logaritmos.

**Tecnología:**

- Implementado en Python estándar sin necesidad de bibliotecas externas.

## 5. Módulo de Resolución de Ecuaciones (Equation Solving Module)

**Responsabilidades:**

- Resuelve sistemas de ecuaciones de segundo grado.

**Tecnología:**

- Implementado en Python estándar sin necesidad de bibliotecas externas.

## 6. Manejo de Errores y Excepciones (Error Handling)

**Responsabilidades:**

- Maneja errores y excepciones que puedan ocurrir durante la entrada del usuario o el cálculo.
- Proporciona mensajes de error claros al usuario.

**Tecnología:**

- Utiliza las capacidades de manejo de excepciones incorporadas en Python.

## 7. Gestión del Flujo de la Aplicación (Application Flow Control)

**Responsabilidades:**

- Coordina el flujo general de la aplicación.
- Decide cuándo mostrar los resultados, cómo manejar los errores y cuándo finalizar la ejecución según la decisión del usuario.

**Tecnología:**

- Implementado en Python estándar con estructuras de control de flujo como if, while y funciones.

## 8. Persistencia de Datos (Data Persistence)

**Responsabilidades:**

- Opcionalmente, almacena y recupera datos como registros de cálculos anteriores o configuración.

**Tecnología:**

- Puedes utilizar bibliotecas de Python como sqlite3 para bases de datos SQL o pickle para el almacenamiento de datos en archivos, si es necesario
