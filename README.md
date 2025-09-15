# SISTEMA DE GESTION PARQUE DE DIVERSIONES

### Se debe implementar un sistema de gestión para un parque de diversiones, donde el
flujo de las atracciones se organiza mediante una cola de pilas.
Cada elemento de la cola representa una atracción del parque (ejemplo: Montaña
Rusa, Carros Chocones, Rueda de la Fortuna, Casa del Terror).
Dentro de cada atracción, los visitantes se organizan en una pila (LIFO).
Límites iniciales por atracción

• Montaña Rusa → Capacidad: 3 visitantes por turno
• Carros Chocones → Capacidad: 2 visitantes por turno
• Rueda de la Fortuna → Capacidad: 2 visitantes por turno
• Casa del Terror → Capacidad: 2 visitantes por turno

## Flujo del sistema
1. Ingreso de visitantes: Se registran visitantes (adultos o niños) que entran al
sistema y se agregan a la primera atracción de la cola (Montaña Rusa).

2. Procesamiento por turnos:
o Cada atracción procesa hasta su capacidad máxima por turno.
o Los visitantes procesados pasan a la siguiente atracción en la cola.
o Los que no alcanzan a procesarse esperan en la pila de la atracción
actual.

3. Ejecución de turnos:
o Cada ejecución de turno debe mostrar un reporte indicando qué pasó en
cada atracción.
o Esto continúa hasta que todos los visitantes salgan del sistema.

## Reglas del sistema
1. Manejo de la cola de pilas
o La cola de atracciones sigue un orden FIFO.
o Se pueden agregar o quitar atracciones.
o Si se elimina una atracción, los visitantes en su pila deben redistribuirse
en las siguientes.
o Manejo de las pilas de visitantes
o Las pilas siguen un orden LIFO.Cada turno, la atracción procesa hasta su
capacidad máxima.
o Los visitantes procesados se agregan en la pila de la siguiente
atracción.

2. Ejecución de turnos
o El sistema debe permitir ejecutar turnos de forma controlada.
o Puede implementarse con una opción en el menú "Ejecutar Turno", que
muestre un reporte del movimiento de visitantes.
o Adicionalmente debe automatizarse con un ciclo que reporte cada turno
hasta que todos los visitantes salgan del parque.

## Operaciones requeridas
1. Agregar visitante al sistema (adulto o niño): Se registran visitantes (adultos o
niños) que entran al sistema y se agregan a la primera atracción de la cola
(Montaña Rusa).

2. Procesar visitantes en cada atracción según su límite de turno.
   
3. Ejecutar un turno:
o Procesar las atracciones desde la primera hasta la última.
o Reportar qué visitantes fueron procesados en ese turno.
o Reportar qué visitantes quedaron en espera por turno.

4. Eliminar una atracción y redistribuir visitantes.
o Ejemplo: Si la Rueda de la Fortuna se daña, los visitantes pasan
directamente a la Casa del Terror.

5. Agregar una nueva atracción al flujo.
o Ejemplo: Se activa promoción y se agrega una atracción Simulador 4D
con límite de 2 visitantes por turno.

6. Consultar estado del sistema.
o Mostrar cuántos visitantes están en cada atracción y en qué orden (en la
pila).
