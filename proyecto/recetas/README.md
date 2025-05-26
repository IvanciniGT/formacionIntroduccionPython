# Proyecto de gestión de recetas

La idea es tener una herramienta de linea de comandos desde la que podamos:
- Crear recetas
- Listar recetas
- Buscar recetas
- Editar recetas
- Eliminar recetas

Básicamente, un CRUD de recetas.
(CRUD=Create, Read, Update, Delete)

Las recetas deben tener persistencia en un archivo YAML.
Necesitamos un menú de opciones para que el usuario pueda elegir qué acción realizar.

---

## Estructura de componentes de la app

main - Interacción con el usuario
clase: Recetas
    propiedades
    métodos: crear receta, listar recetas, buscar receta, editar receta, eliminar receta

^ ASI NO !!!!
---

En el mundo del desarrollo de software, es importante seguir algunas reglas a la hora de crear / Estructurar programas.

Hay algunos PRINCIPIOS muy conocidos en el mundo del desarrollo de software, que nos ayudan a crear programas más robustos, escalables y mantenibles: SOLID, SoC, DRY, KISS, YAGNI, etc.

Los principios no son REGLAS, que si no sigo me muero!

SoC (Separación de Concerns): Cada módulo o componente de un sistema debe tener una responsabilidad UNICA bien definida y no mezclarse con otras responsabilidades.

Normalmente cuando creamos/diseñamos clases, tenemos distintos tipos de clases.
- Entidades/Modelos: Representar datos del dominio de la aplicación. Su única responsabilidad es representar los datos. No contienen lógica /o muy poca.. y directamente vinculada a los datos.
- Repositorios: Encargados de la persistencia de los datos. Se encargan de guardar, recuperar, actualizar y eliminar entidades del sistema.
- Servicio: Encargados de la lógica de negocio.
- Controladores: Exponen la funcionalidad de los servicios de alguna forma concreta.

Es importante seguir una estructura de este estilo, de forma que si cada clase tiene una responsabilidad bien definida, nuestro programa será más fácil de entender, mantener y evolucionar.



   MODELO/ENTIDAD Receta. Esta clase SOLO ALBERGA DATOS (Define el concepto de Receta). No tiene lógica.
    Una receta consta de un nombre, tiempo de preparación, ingredientes y pasos....
   REPOSITORIO RecetasRepository. Esta clase se encarga de la persistencia de las recetas. Guarda, recupera, actualiza y elimina recetas.
     .save(receta)
     .delete(receta)
     .find_by_name(nombre)
     .find_all()
     Esto son cosas que a día de hoy vamos a hacer contra un fichero YAML... pero que el día de mañana podría hacer contra una base de datos.... o un fichero json.
   SERVICIO: RecetasService: Métemos la lógica de negocio... La funcionalidad base que queremos en nuestra app:
    - crear_receta
    - listar_recetas
    - buscar_receta
    - editar_receta
    - eliminar_receta
    Esas funciones se solapan mucho con las del repositorio, pero no son exactamente lo mismo.
    Por ejemplo, cuando creo una receta, evidentemente la guardaré en el repositorio, .save(receta), pero también haré otras cosas, como validar que la receta tiene un nombre correcto, que no existe ya una receta con ese nombre, o quizás quiero enviar un correo electrónico a una lista de suscriptores para avisarles de que hay una nueva receta.

    CONTROLADOR: RecetasConsoleUI: Menú... Formularios que se van completando en linea de comandos.

    Qué pasa si el día de mañana quiero montar una app cuya interfaz no sea de consola... sino por ejemplo de escritorio... como el word.



---

A esta conclusión hemos llegado gracias a aplicar el SOC (Separación de Concerns).

- class Receta
- class RecetasRepository
- class RecetasService
- class RecetasConsoleApp


Hay otro principio llamado Principio de Inversión de la Dependencia. Ese principio se enmarca dentro de los principios SOLID.

SOLID son 5 principios:
- S: Single Responsibility Principle (SRP) - Principio de Responsabilidad Única
- O: Open/Closed Principle (OCP) - Principio de Abierto/Cerrado
- L: Liskov Substitution Principle (LSP) - Principio de Sustitución de Liskov
- I: Interface Segregation Principle (ISP) - Principio de Segregación de Interfaces
- D: Dependency Inversion Principle (DIP) - Principio de Inversión de Dependencias          *** MAS IMPORTANTE
    Una clase NUNCA DEBE DEPENDER DE OTRA CLASE


Nuestro RecetasConsoleApp, va a usar un RecetasService...
Y el RecetasService necesita de un RecetasRepository para poder hacer su trabajo.

Si monto un RecetasRepository que trabaje con YAML, un dato que necesitará manejar ese RecetasRepository es la carpeta del HDD donde se guardan los ficheros YAML.
En cambio si monto un RecetasRepository que trabaje con una base de datos, necesitaré un usuario de BBDD, una contraseña, una dirección de red de dónde leches está la BBDD, etc.

No quiero que mi RecetasService dependa de un RecetasRepository concreto, el de YAML... el de BBDD... de ninguno concreto... Le debe dar igual el Repository que yo use... De hecho el día de mañana debería ser capaz de cambiar uno por otro (YAML-> BBDD) sin que mi RecetasService se entere de nada. (ESTO SERIA APLICACION DEL PRINCIPIO DE SUSTITUCION DE LISKOV)
Aquí nos sale un concepto: ABSTRACCIÓN / INTERFACES.

Una interfaz es un tipo de objeto del que sólo conozco lo que puede hacer... pero no el cómo lo hace.
En python no existe el concepto de interfaz.. Pero.. podemos más o menos simularlo.


# Qué es un RecetasRepository?

Un algo... que me permite guardar, recuperar y eliminar recetas.
.save(receta)
.find_by_name(nombre)
.find_all()
.delete(receta)

Cómo se implementan esos métodos (qué código ejecutan?) Ah... pues eso depende del tipo de repositorio que use.
... Si guardo en ficheros... o si guardo en BBDD... o si guardo en RAM.... YO QUE SE !
Lo que si sé es que cualquier Repositorio de Recetas me debe permitir hacer esas cosas.

En este caso, estamos convirtiendo a nuestro RecetasRepository en una INTERFAZ.

Y de esa interfaz podremos tener varias clases que la implementen:
- RecetasRepositoryYAML
- RecetasRepositoryBBDD
- RecetasRepositoryJSON

Y al servicio, le importa un huevo el tipo concreto de repositorio que use.... mientras sea un RecetasRepository, le vale.


El principio de inversión de la dependencia nos dice que una clase no puede depender de otra clase concreta, sino que ambas deben depender de una abstracción (una interfaz).


   RecetasRepositoryYAML <--- RecetasService      ASI NO!!!
   clase (código)             clase(código)

   La flecha es lo que llamamos una dependencia.
   El ppo de inversión de la dependencia me dice que a ninguna clase le pueden llegar flechas... Que de las clases solo pueden salir flechas.
   A las interfaces es a las que les pueden llegar flechas.


                      implementa                necesita
   RecetasRepositoryJSON ---> RecetasRepository <--- RecetasService      ASI SI !!!
   clase (código)               interfaz             clase(código)

----

# Soy un fabricante de bicicletas:

- BTwin : Decathlon

Soy Decathlon y tengo una marca de bicicletas llamada BTwin.
Voy a fabricar las RUEDAS? NO
Y los frenos? NO
Y el sillín? NO
Y el marco? NO

Y que pinto yo?
Yo voy a definir cómo quiero la bicicleta.
Defino un modelo de bicicleta que voy a crear: (CLASES- TIPOS CONCRETOS)
- Esa bici llevará unas michelín APSJQHD9284.
- Un freno shimano XKSIFH-39375r783

Qué tal sería esto? RUINA.
Qué pasa si Michelin desaparece del mercado? O si se vuelve muy caro? o si por lo que sea ya no quiero trabajar con él.

Defino un modelo de bicicleta que voy a crear: INTERFACES (ESPECIFICACIONES)
- Esa bici llevará unas ruedas de tal diámetro, tal ancho,...
- Un freno con tales características.
- Un sillín que tenga tales dimensiones, que sea de tal material, que tenga tal forma...
  y que la barrita de abajo para engancharse al cuadro mida tanto...

Me importa el sillín concreto que monte? NO, mientra el nuevo cumpla con las especificaciones que he definido.

Eso es lo me da la capacidad de hacer arreglos a la bici.. y de tener facilidad de acceso a repuestos.


---


clase Receta // MODELO (clase sin lógica... sin funciones... solo datos)

interfaz RecetasRepository

clase RecetasRepositoryYAML (RecetasRepository):

interfaz RecetasService

clase RecetasServiceImpl(RecetasRepository):

interfaz RecetasApp

class RecetasConsoleApp(RecetasApp):

ESOS SON NUESTROS COMPONENTES !

Los mínimos... luego crearemos algunas cosillas más.