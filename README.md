
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

Si `UserController.get_user_full_name` dejara de retornar un `str` y pasara a retornar, por ejemplo, un `dict`/JSON, habría que adaptar:
- El propio `UserController` (el cambio en sí).
- Cualquier consumidor del controlador (capa web/API o CLI) que dependa del formato anterior.
- Los tests de integración que comparan contra strings literales.

`UserService` y `InMemoryUserRepository` no necesitarían cambios: su contrato es interno y el controlador decide cómo exponer el dato hacia afuera. Esto ilustra el valor de separar capas: el cambio queda contenido en el controlador y en quien lo consume.

**Parte 2 — Pregunta:** ¿Por qué `test_order_calculator_uses_discount_engine` es una prueba de integración (y no solo unitaria)?

La prueba no aísla `OrderCalculator` con un doble de prueba (mock/stub) para `DiscountEngine`: instancia el `DiscountEngine` real y lo inyecta en `OrderCalculator`, verificando el resultado combinado de `final_total`. Esto significa que:
- Ejercita la colaboración real entre dos unidades, no el comportamiento de una sola clase aislada.
- Verifica el contrato entre ambas (qué valor retorna `discount_for` y cómo lo consume `final_total`); si ese contrato se rompiera, una prueba unitaria con mock no lo detectaría.
- El resultado esperado depende de la lógica de ambos módulos combinados (regla de descuento + cálculo de impuesto).

Una prueba unitaria de `OrderCalculator` reemplazaría `DiscountEngine` por un doble con un valor fijo, probando solo la aritmética en aislamiento. Aquí se prueba que las piezas reales funcionan correctamente juntas.

