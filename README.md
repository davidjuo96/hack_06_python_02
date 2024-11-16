David Urdaneta - Social Oplesk - Programa Fullstack - Grupo 9
---

# Solución de Hacks - 2da parte

## Tecnologías utilizadas
[![My Skills](https://skillicons.dev/icons?i=py)](https://skillicons.dev)


## Tabla de contenidos
- [Instrucciones de Instalación](#instrucciones-de-instalación)
- [Descripción de los Hacks](#descripción-de-los-hacks)
- [Pruebas](#pruebas)


## Instrucciones de Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/davidjuo96/hack_06_python_02
   ```

2. **Instalar Requerimientos**  
   ```bash
   pip install -r requirements.txt
   ```
   
## Descripción de los Hacks

| **Hack** | **Descripción** |
|----------|-----------------|
| **H-1**  | Modificar palabras para alterar su estructura:<br>- `"fooziman"` → `"fOozIman"`<br>- `"qux"` → `"qUx"`<br>- `"eq"` → `"eq"` |
| **H-2**  | Simplificar palabras eliminando algunas letras:<br>- `"fooziman"` → `"fzmn"`<br>- `"barziman"` → `"brzmn"`<br>- `"qux"` → `"qx"` |
| **H-3**  | Reemplazar vocales por otros caracteres y aplicar otras modificaciones:<br>- `"a"` → `"@"`, `"e"` → `"3"`, `"i"` → `"!"`, `"o"` → `"0"`, `"u"` → `"v"`<br>- Ejemplos:<br> `"fooziman"` → `"F00z1m@N"`<br> `"barziman"` → `"B@rz1m@N"`<br> `"3q"` → `"3Q"`<br> `"qu"` → `"Qv"`<br> `"qux"` → `"QvX"` |
| **H-4**  | Eliminar la primera y ultima letra de cada palabra para un caso en específico:<br>- `"fooziman"` → `"oozima"`<br>- `"barziman"` → `"arzima"`<br>- `"qux"` → `"qux"` |
| **H-5**  | Dividir las palabras y añadir guiones:<br>- `"fooziman"` → `"fo-zi-ma-"`<br>- `"barziman"` → `"ba-zi-an"`<br>- `"qux"` → `"qu-"`<br>- `"eq"` → `"eq"` |
| **H-6**  | Generar una lista de números y guiones, usando `for`:<br>- Entrada: `["a", "b", "c", "d", "e"]` → Salida: `["1", "-", "3", "-", "5"]`<br>- Entrada: `[]` → Salida: `["0"]` |
| **H-7**  | Generar una lista de números, usando `while`:<br>- Entrada: `["a", "b", "c", "d", "e"]` → Salida: `["1", 2, "3", 4, "5"]`<br>- Entrada: `[]` → Salida: `[0]` |
| **H-8**  | Revertir y enumerar elementos en una lista para dos casos en específico:<br>- Entrada: `["a", "b", "c", "d", "e"]` → Salida: `["e-5", "d-4", "c-3", "b-2", "a-1"]`<br>- Entrada: `["a", "b", "c"]` → Salida: `["c-3", "b-2", "a-1"]`<br>- Entrada: `["a", "b", "c", "d"]` → Salida: `["4", "3", "2", "1"]`<br>- Entrada: `["a", "b"]` → Salida: `["2", "1"]` |
| **H-9**  | Modificar valores en un diccionario, usando `for`:<br>- Entrada: `{"foo": "fookziman", "bar": "barziman"}`<br>- Salida: `{"Foo": "Fooziman"}` |
| **H-10** | Cambiar las claves y valores en una lista de diccionarios:<br>- Entrada: `[{"a": "b"}, {"c": "d"}, {"e": "f"}]`<br>- Salida: `[{"1": "2"}, {"3": "4"}, {"5": "6"}]` |

## Pruebas

Para verificar cada hack, se utilizan pruebas con `pytest`:

- Ejecutar todas las pruebas:

  ```bash
  python -m pytest test_hack.py -v
  ```

- Ejecutar una prueba específica:  
  ```bash
  python -m pytest test_hack.py::test_hack_1 -v
  ```
