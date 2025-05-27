# JSON

Lenguaje para marcar/estructurar información

```json
numero = 23
```
```json
texto = 'hola'
```
```json
logico = true
```
```json
 {
  "nombre": "Juan",
  "edad": 23,
  "casado": false,
  "hijos": null,
  "hobbies": ["futbol", "natacion"],
  "direccion": {
    "calle": "Calle Falsa",
    "numero": 123
  }
}
```
```json
[
  {
    "nombre": "Juan",
    "edad": 23
  },
  {
    "nombre": "Maria",
    "edad": 25
  }
]
```
```json
[1,2,3,4,5,6]
```

# YAML

Yaml es otro lenguaje para marcar/estructurar información.
De hecho es un superset de JSON.
Dicho de otra forma, cualquier documento JSON es un documento YAML válido.

Lo que pasa es que yaml es mucho más potente que JSON y encima es más legible.

- Docker compose usa YAML para definir contenedores
- Kubernetes usa YAML para definir pods, deployments, etc.
- La red en una máquina Ubuntu se define en un archivo YAML
- Ansible usa YAML para definir playbooks
- Gitlab CI/CD y GitHub Actions usa YAML para definir workflows de integración continua / despliegue continuo

---

 XML
HTML
YAML
  
  Markup Language: Lenguaje de Marcado <tag>...</tag>

Con YAML hicieron una cachondada con el nombre.

YAML podríamos pensar que viene de Yet Another Markup Language, pero no es así.
Es un acrónimo recursivo que significa 
Y    A     M      L
YAML Ain't Markup Language. No busques marquitas por aquí que no hay.

---

Antes os comenté que cuando pedimos al sistema operativo que ejecute un programa, el sistema operativo genera lo que se llama un proceso.

Para que ese proceso se pueda comunicar con el exterior o que el exterior se pueda comunicar con el proceso, los sistemas operativos ofrecen multiples mecanismos de comunicación.
Uno de esos mecanismos es la apertura de canales de comunicación.
Por defecto todo proceso en todo sistema operativo tiene asociados 3 canales:
-  un canal de entrada estándar que se llama stdin (standard input)    0
-  un canal de salida estándar que se llama stdout (standard output)   1
-  un canal de error estándar que se llama stderr (standard error)     2

      FICHERO
        | v |
  +-----+ v +------+
  |    PROCESO     |
 -+                +-
>>> 0              >>> 1 Salida normal de comunicación
 -+                +-
  |                |
  +-----+ v +-------+
        | v |
          2 Salida de error



Cualquier proceso (programa corriendo en un SistemaOperativo) en cualquier SistemaOperativo acaba siempre con un código de salida/respuesta. Ese código es un número entre 0 y mucho.
Si un programa sale con código 0, significa que todo ha ido bien. (Windows, MacOS, Linux, etc.)
Si un programa sale con código distinto de 0, significa que algo ha ido mal. (Windows, MacOS, Linux, etc.)
Habitualmente los programas usan esos códigos para indicar distintos tipos de errores.
En linux, unix, podemos saber el código de salida del último comando ejecutado con la variable especial echo $?