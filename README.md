# Examen_Final_DSWyP_2017_2_mae_isw
Desarrollo del Examen Final de DSWyP 2017 2 mae isw

## Pregunta 1 (3 puntos)
- Aplicar el patrón Abstract Factory para evitar exponer clases concretas (WhiteFinish, FastProcessor, etc) en el cliente (Client.java);
- El nuevo Client.java debe mostrar la misma información, y el método main no debe exceder 10 líneas de código.

Ver diagrama UML [diagrama UML](https://drive.google.com/open?id=1ialCoxl07sG1so0ZWkfvtlsDF5ejakLK)
El nuevo Client (ahora en Python y usando el abstract factory) está en Pregunta01

## Pregunta 2 (3 puntos)
- Indicar los patrones actualmente implementados.
* Factory Pattern
* Observer Pattern
* 

- Soportar la red social Pinterest.
- Aplicar el patrón Adapter de clase y objeto.

## Pregunta 3 (3 puntos)
- Aplicar el patrón Strategy.
- Implementar el algoritmo de complejidad lineal (NO se puede usar la función distinct).

## Pregunta 4 (3 puntos)
- Aplicar el patrón Bridge.

Ver diagrama con patrón Bridge [Diagrama UML](https://drive.google.com/open?id=1ddafh0OKTpUw0k56fJzEdLcAi6EaFNUc)

## Pregunta 5 (2 puntos)
- Aplicar el patrón Flyweight.

## Pregunta 6 (3 puntos)
- Aplicar el patrón Decorator sabiendo que a un sandwich se le puede agregar cualquier combinación de: Egg, Chicken, Beef, Bacon, Turkey.

[UML pregunta 6](https://drive.google.com/open?id=1XzartB99cBhRiWIrbkwVmkOSpg-EhQOa)
Ver código pregunta06

## Pregunta 7 (1 punto)
Proponga un ejemplo del patrón Observer (NO visto en clase ni en las exposiciones, ni TAMPOCO bajado de la web).

## Pregunta 8 (1 punto)
Proponga un ejemplo del patrón State (NO visto en clase ni en las exposiciones, ni TAMPOCO bajado de la web).

## Pregunta 9 (1 punto)
Proponga un ejemplo del patrón Chain of Responsibility (NO visto en clase ni en las exposiciones, ni TAMPOCO bajado de la web).

## Pregunta 10 (1 punto)
Proponga un ejemplo del patrón Memento (NO visto en clase ni en las exposiciones, ni TAMPOCO bajado de la web).

* __Ejemplo de Patrón Memento__: Cuando trabajamos un documento en Word, podemos reestablecer un contenido anterior mediante el comando "Atrás" o "Ctrl - z", en el UML la clase DocWord representa el documento en word y actúa de Originator, la clase DocContentMemento sirve para encapsular el contenido del Word y actúa como Memento para ser apilado en la clase responsable de mantener a los Mementos que es la clase CareTaker. La clase Pregunta10Client es el consumidor.

[UML Pregunta10](https://drive.google.com/open?id=1xAtr3R4-OtD4BMG7Bh_SOIxSpyM02vaH)
Ver código en Pregunta10
