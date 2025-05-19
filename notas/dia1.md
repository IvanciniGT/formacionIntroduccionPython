# Python

Lenguaje de programación.
Los lenguajes de programación los clasificamos usando distintas taxonomías:

## Lenguajes compilados vs Lenguajes interpretados

El punto es que nosotros escribiremos código en Python (o en cualquier otro).. y el programa que hemos hecho quién lo ejecuta? Sistema Operativo.

Pregunta. Los Sistema Operativos (Windows, Linux, MacOS) hablan python? NPI
hablan C? Menos
y Java? Nasti de plasti!!!
Ni puñetera idea de ningún lenguaje que no sea el suyo propio.
Si los SO hablan su propio lenguaje.. y nosotros escribimos DOCUMENTOS (programa) en un lenguaje X que no es ese lenguaje... cómo hace un SO para ejecutar nuestro programa (leer nuestro documento)?
- El SO.. no hace nada de eso.. le tiene que llegar aquello bien masticadito!
- Lo que sea que le llegue en su lenguaje, lo tiene que entender.

Necesitamos traducir los documentos (programas) que escribimos en un lenguaje X a un lenguaje que el SO entienda:
- Hacer una pretraducción del documento / Programa: COMPILACIÓN
   Beneficios:
   - Programas más rápidos al ejecutarse
   Contras:
   - Si mi programa se tiene que ejecutar en Windows, Linux y MacOS.. tengo que compilarlo (traduciéndolo) para cada uno de esos sistemas operativos. 
- Hacer una interpretación: Traducción en tiempo real: La realiza un INTERPRETE!
   Beneficios:
   - Si mi programa se tiene que ejecutar en Windows, Linux y MacOS.. a todos les mando lo misma.
   - Delego en el entorno el tener un Interprete que vaya traduciendo en tiempo real.
   Contras:
   - Programas más lentos al ejecutarse

COMPILADOS: JAVA, C#, C++
INTERPRETADOS: Python, Javascript, JAVA

JAVA es muy raro... Java es de los pocos lenguajes que son COMPILADOS e INTERPRETADOS a la vez.

.java -> compilación -> .class -> Interpretados por un intérprete : JVM
                           ^
                           bytecode

El interprete de Python más usado se llama (cython... está escrito en C)... otros interpretes serían: Jython, pypy, ironpython....

## Lenguajes de Alto nivel vs Lenguajes de bajo nivel

Básicamente lo cerca que está el lenguaje del lenguaje del ser humano o del lenguaje de la máquina.

                                                 alto nivel --------------------> bajo nivel
                                                                ^
                                                             Lenguaje de alto nivel

## Lenguajes de propósito general vs Lenguajes de propósito específico

Propósito general: Me sirven para montar cualquier tipo de programa. << PYTHON
Propósito específico: Me sirven para montar un tipo de programa en concreto.

## Lenguajes de tipado estático (fuerte) vs Lenguajes de tipado dinámico (débil)

Cuando creamos un programa, ese programa va a estar manejando DATOS.
Los DATOS podrán se de una naturaleza u otra... Distintos TIPOS DE DATOS.
En función del tipo de dato con el que estemos trabajando, podré hacer una operaciones u otras.

    13 de Octubre de 2016 <---- DATO DE TIPO FECHA
                                Valor Absoluto?         SI                  NO
                                La puedo elevar al cuadrado?                NO
                                Puedo saber en qué día de la semana cae?    SI
    3.198467              <---- DATO DE TIPO NUMERICO
                                Valor Absoluto?                             SI
                                La puedo elevar al cuadrado?                SI
                                Puedo saber en qué día de la semana cae?    NO
                                Ponerlo en mayúscula?                       NO
    "Hola Mundo"         <---- DATO DE TIPO CADENA
                                Valor Absoluto?                             NO
                                La puedo elevar al cuadrado?                NO
                                Puedo saber en qué día de la semana cae?    NO
                                Ponerlo en mayúscula?                       SI

Cualquier lenguaje de programación tiene tipos de datos? SI... TODOS !!!!!
En python, tenemos datos de tipo: str, bool, float, list, tuple, set, dict, int, complex

Los datos que vamos creando en un programa los colocamos en la memoria RAM.
Pensad en la memoria RAM como si fuera un cuaderno de cuadrícula.

Qué es una variable?
- Python, Java, JS: Una referencia a una dirección de memoria
     Se parece más a lo que en C denominamos un PUNTERO! 
     Una variable la entiendo como un post-it, que lo pego al lado de una casilla de la cuadrícula ( de la memoria RAM)

- C, Fortrán, ADA: Una casilla de la cuadrícula/ Cajoncito donde pongo algo.

```python
nombre = "Federico"
```

1. "Federico"                Python crea un dato de tipo TEXTO en memoria RAM (en algún sitio... npi de donde)
2. nombre                    Hemos cogido una variable (un post-it del taco de postit..) y en él hemos escrito
                             la palabra "nombre"
3. =                         Pego el post-it en la cuadrícula al lado del dato"Federico".
                             El = en programación se denomina operador de asignación.

                            No asigno el dato FEDERICO a la variable nombre.
                            Asigno la variable nombre al dato "Federico".

```python
nombre = "Arturito"
```

1. "Arturito"                Python crea un dato de tipo TEXTO en memoria RAM 
                             dónde? (en algún sitio... npi de donde)... Sé algo.
                             Donde estaba FEDERICO NO... en otro lao!
                             Llegados a este punto, cuántos datos tengo en RAM?
                                2: "Federico" y "Arturito"
2. nombre =                  Arrancamos el post-it de donde estaba pegao (al lado de "Federico")
                             Y lo movemos a otro lao (al lado de "Arturito")
                                Llegados a este punto, sigo teniendo 2 datos en RAM:
                                "Federico" y "Arturito"
                                Solo que al dato Federico ya no le apunta ninguna variable.
                                Está huérfano de variable. Python lo considera GARBAGE (BASURA)
                                Ya que el dato es irrecuperable.
                                En algún momento quizás o quizás no... npi, entre el GARBAGE COLLECTOR de Python y lo elimine... liberando memoria RAM.
                                JAVA, JS también trabajan así. En todos estos lenguajes existe el concepto de GARBAGE COLLECTOR.
                                En C, Fortrán, ADA no existe el concepto de GARBAGE COLLECTOR.... donde la basura me encargo yo de recogerla.

En todo lenguaje de programación manejamos datos de distintos tipos.
Hay lenguajes en los que las variables también tienen asignado un tipo de dato.
Es como que tengo postits de distintos colores.
- Los amarillos sirven para apuntar a datos de tipo TEXTO.
- Los rosas sirven para apuntar a datos de tipo NUMERICO.
- Los verdes sirven para apuntar a datos de tipo FECHA.
- Los azules sirven para apuntar a datos de tipo BOOLEANO.
En esos lenguajes, un post-it de color amarillo (una variable que puede apuntar a TEXTOS) no puede apuntar a un dato de tipo NUMERICO. POR DEFINICION. Hemos quebrantado la regla. AMARILLO -> TEXTO

Por contra hay lenguajes cuyas variable no tienen un tipo de dato asignado.
REPITO:
- LOS DATOS SIEMPRE TIENEN UN TIPO DE DATOS ASIGNADO
- LAS VARIABLES pueden o no tener un tipo de dato asignado.
  Caso de tenerlo, solo puedo usarlas para referenciar datos de ese tipo.

Los lenguajes cuyas variables TIENEN TIPO DE DATOS ASIGNADO son los de TIPADO ESTATICO (FUERTE)
Los lenguajes cuyas variables NO TIENEN TIPO DE DATOS ASIGNADO son los de TIPADO DINAMICO (DEBIL)

No es que el tipo de la variable cambie... es que no tiene un tipo de dato asignado la variable.

Qué es mejor? Lenguajes de tipado dinámico o lenguajes de tipado estático? AQUI NO DEPENDE.
SIEMPRE TIPADO ESTATICO (FUERTE) ES MEJOR QUE TIPADO DINAMICO (DEBIL)
Lo que pasa es que para ciertos tipos de programas, el tipado dinámico es más cómodo.... AUNQUE CLARAMENTE PEOR.

De hecho es tan peor, que invalida a ciertos lenguajes de programación para el desarrollo de ciertos tipos de programas.

```
function prepararInforme(titulo, datos);
```

Pregunta: Cómo me comunico con esa función? Qué le tengo que pasar? Qué me devuelve? NPI
- 2 opciones me quedan:
  - O leo la documentación de la función (caso que la hayan escrito)
  - O miro el código fuente de la función (caso que lo tenga)
  En serio???? 

Muy diferentes es:

```
function prepararInforme(titulo: String , datos: Array<Number>): PDF;
```
Aquí lo tengo claro!

Si... escribo un poquito más... tampoco tanto!
Pero a cambio me entero! Y lo mejor... LOS DEMÁS SE ENTERAN!

Es tan cutre el hecho de trabajar sin tipo en las variables, que en python tuvieron que crear un ROLLO/ARTIMAÑA para paliar el efecto de este desaguisado: En python existe una sintaxis para definir el tipo que DEBERÍA pasarse a una variable.

```python
def prepararInforme(titulo: str, datos: list) -> str:
    pass
```
Podré hacer lo que quiera.. python no lo chequea. ESA SINTAXIS BÁSICAMENTE ES UNA FORMA OFICIAL DE DOCUMENTAR EL CÓDIGO.
En JS, que le pasa lo mismo... de hecho se han inventado un lenguaje nuevo completamente paralelo a JS que se llama TYPESCRIPT.

Lo que hacemos es traducir de TS  -- TRANSPILAR -->  JS.

Compilar es cuando traduzco de un lenguaje de más alto nivel a un lenguaje de más bajo nivel.
Transpilar es cuando traduzco de un lenguaje a otro, de similar nivel de abstracción.

## Paradigmas de programación soportados por cada lenguaje

Un paradigme de programación es un nombre un tanto hortera que los desarrolladores le damos a la forma en la que estamos usando un lenguaje para expresar/comunicar unas ideas.
- Programación imperativa                   Cuando el lenguaje me permite ir escribiendo órdenes que deben procesarse en un orden
                                            secuencial. En ocasiones necesito romper esas secuencialidad y los lenguajes de programación tienen ciertas palabras (expresiones de control de flujo) que me permiten hacer ese trabajo: IF, FOR, WHILE....
- Programación procedural                   Cuando el lenguaje me permite agrupar una secuencia de órdenes (código imperativo) bajo un
                                            concepto que denominamos función / procedimiento / métodos / subrutina.
                                            También debe permitirme solicitar la ejecución de esa secuencia a futuro.
                                            - Crear funciones y ejecutarlas
                                            Beneficios?
                                            - Permite reutilizar código (Evita duplicar código)
                                            - Mejorar la estructura del código (mejorar la legibilidad)
                                            Inconvenientes? NO HAY...  La programación procedural es una evolución de la programación imperativa.
- Programación funcional                    Cuando el lenguaje me permite que una variable apunte a una función
                                            Y posteriormente ejecutar la función desde la variable. Entonces tenemos un lenguaje que soporta la programación funcional.
                                            El tema no es lo que es la programación funcional... que es una chorrada conceptual.
                                            El tema es lo que puedo llegar a hacer cuando el lenguaje soporta la programación funcional.
                                            Porque podemos por ejemplo:
                                            - Crear funciones que reciban funciones como parámetros
                                            - Crear funciones que devuelvan funciones como resultado
                                            Y aquí es donde la cabeza EXPLOTA ! 
                                            MUCHOS BENEFICIOS...
                                            Es una evolución de la programación procedural.
                                            ESTE TEMA ES COMPLEJO! Nos meteremos un poquito con ello
- Programación orientada a objetos          Hemos dicho que los programas manejan datos... y esos datos son de un determinado tipo.
                                            Todo lenguaje de programación tiene una serie de tipos de datos predefinidos:
                                            Texto, número, booleano, fecha, lista, diccionario...
                                            Hay lenguajes que me permiten crear mis propios tipos de datos, con sus propiedades(características) y sus métodos asociados(funciones que operan sobre esos datos).

                                                TIPO DE DATO            Qué lo caracteriza?       Qué puedo hacer?
                                                -----------------       -------------------------------------------------------
                                                Texto                   Secuencia de caracteres   aMayusculas() aMinusculas()
                                                                                                  longitud()

                                                Fecha                   Dia                       caesEnBisiesto()  
                                                                        Mes                       caesEnVerano()
                                                                        Año                       cuantosDiasHayHasta(otraFecha)

                                                Persona                 Nombre                    calcular la edad en días!
                                                                        Apellidos
                                                                        DNI
                                                                        Email
                                                                        Fecha de nacimiento

                                            Cuando el lenguaje me permite definir mis propios tipos de datos (CLASES) y crear posteriormente datos de esos tipos de datos (OBJETOS) decimos que tenemos un lenguaje que soporta la programación orientada a objetos.
                                            
                                            Beneficios?
                                            - Permite reutilizar código (Evita duplicar código)
                                            - Mejorar la estructura del código (mejorar la legibilidad)
                                            Inconvenientes? NO HAY...  La programación orientada a objetos es una evolución de la programación funcional.



> Felipe, pon una silla debajo de la ventana!              IMPERATIVA! 

## Otras características

- Multiplataforma
- Gran comunidad
- Gran cantidad de librerías
   Pandas (Tratamiento de datos) 
   Sklearn (Machine Learning)
   Tensorflow (Redes Neuronales)
   Keras (Redes Neuronales)
   Numpy (Cálculo numérico)

## Usos principales del lenguaje

- Tester/Q&A: Automatizar pruebas que antes hacía a mano:
  -  Abrir un navegador
  -  Ir a una página web
  -  Rellenar el formulario de login
  -  Y hacer una búsqueda.. y a ver si salen datos.
- SysAdmins: Automatizar (bash, .bat, powershell). PYTHON es un lenguaje maravilloso para hacer scripting (scripts)
- Matemáticas, Negocio, Estadística: Tratamiento de datos (grandes cantidades¿?)
    Qué tan eficiente es el uso de la memoria RAM por parte de PYTHON? RUINA GORDA !!!!!!!
    Qué tan rápido es un programa python al ejecutarse? LENTO COMO UNA TORTUGA COJA MONTADA ENCIMA DE UN CARACOL !!!!!

- Pero... he oído por ahí que los programas de Inteligencia Artificial, creación de redes neuronales, modelos matemáticos complejos, técnicas de optimización, etc... se hacen en PYTHON.
Realmente todo eso es verdad A LA VEZ ! No hay trampa..,. un poquito de trampa.
Todas esas librerías tan guays que hay en python, están escritas en C. 
    Pandas está escrito en C.
    Numpy está escrito en C.
    Sklearn está escrito en C.
    Tensorflow está escrito en C.
Desde python lo único que hago es llamar a esas librerías escritas en C.
    Y esas librerías son las que hacen el trabajo sucio.
    Y esas librerías son las que hacen un uso eficiente de la memoria RAM.
    Y esas librerías son las que hacen un uso eficiente de la CPU.
    Y esas librerías son las que hacen un uso eficiente de la GPU.
Y el resultado se lo pasan al TORTUGA PYTHON... que pa mostrar 4 datos por pantalla, pues se apaña el hombre!

Lo que pasa es que programar en C... agárrate! eso es duro!
Programar en Python... es mucho más sencillo.

Y hay mucha gente que quiere / necesita programar... y no tiene conceptos profundos de programación. Y está bien.
Driver de control de un... lo que sea (frenos de un coche, cámara térmica...) eso es duro... déjalo a una persona que sepa un huevo de programación.
Pero si lo quiero es pedirle a la computadora que:
- Ejecute 4 tareas una detrás de otra (AUTOMATIZACION)
- Que genere un programa capaz de predecir un dato (INTELIGENCIA ARTIFICIAL)
- Que ejecute unas pruebas (QA) (que no es sino 4 tareas... una detrás de otra)

En esos casos, ni necesito el lenguaje de programación más potente del mundo, ni el más rápido... ni saber un huevo de programación profunda. Y ESE ES EL HUECO DE PYTHON.