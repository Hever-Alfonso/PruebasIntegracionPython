
# Introducción a Pruebas de Integración (Python) — 4 partes

Este repositorio contiene un ejercicio práctico en **Python** para evidenciar 4 tipos de integración:

1) **Por capas** (Controller → Service → Repository in-memory)  
2) **Modular** (un módulo usa a otro)  
3) **Con API externa** (cliente HTTP real contra servidor simulado)  
4) **Con base de datos** (SQLite en memoria)

En las cuatro actividades estamos haciendo pruebas de integración. Lo único que cambia es quién se está comunicando con quién.

## Requisitos
- Python 3.11+
- `pip install -r requirements.txt`

## Ejecutar
```bash
pytest -q
```
O por parte:
```bash
pytest -q tests/test_part1_layers.py
pytest -q tests/test_part2_modules.py
pytest -q tests/test_part3_external_api.py
pytest -q tests/test_part4_database.py
```

## Pregunta
- Explique qué componentes se están integrando en este código y justifique por qué este es un caso de prueba de integración y no una prueba unitaria.
- Proponga una aserción adicional que fortalezca la prueba de cada tipo de integración.
- Proponer un fallo posible.

## Notas de diseño

**Parte 1 — Pregunta:** Si cambias el formato de salida del controlador, ¿qué otras capas tendrías que adaptar?

Si el controlador (`UserController`) empezara a devolver, por ejemplo, un `dict` en vez de un simple texto, habría que cambiar:
- El controlador mismo (ahí está el cambio).
- Quien lo use (por ejemplo una página web o una app que lo consuma).
- Los tests, porque comparan contra un texto exacto.

El servicio (`UserService`) y el repositorio (`InMemoryUserRepository`) no cambiarían, porque ellos no saben nada del formato de salida; eso lo decide solo el controlador. Por eso separar en capas es útil: el cambio se queda solo en una parte.

**Parte 2 — Pregunta:** ¿Por qué `test_order_calculator_uses_discount_engine` es una prueba de integración (y no solo unitaria)?

Porque el test usa el `DiscountEngine` real, no uno inventado (mock). Junta dos piezas de verdad (`OrderCalculator` y `DiscountEngine`) y revisa que trabajen bien juntas. Si solo se probara `OrderCalculator` con un `DiscountEngine` falso, sería una prueba unitaria: probaría una sola pieza, no la unión de las dos.

**Parte 3 — Pregunta:** ¿Cuál es la diferencia entre mockear la librería HTTP y levantar un servidor simulado?

- **Mockear la librería HTTP:** se engaña a la función que hace la llamada (`httpx.get`) para que devuelva una respuesta inventada, sin usar la red de verdad. Es rápido, pero no prueba si el cliente realmente sabe hablar por HTTP.
- **Levantar un servidor simulado** (lo que hace este proyecto con `pytest_httpserver`): se prende un servidor de verdad en la máquina local, y el cliente le habla por HTTP de verdad (aunque sea local). Esto sí prueba la comunicación real: la URL, los códigos de respuesta, el JSON, etc.

Por eso el servidor simulado es una prueba de integración, y el mock de la librería es más una prueba unitaria.

