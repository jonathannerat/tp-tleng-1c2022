# TP TLENG 1c2022

El programa fue probado con Python v3.10.5, y depende de la librería `ply` v3.11.

El mismo se puede correr sin argumentos para procesar entrada por `stdin`, y escribir la salida por `stdout`, o con
hasta 2 argumentos opcionales, especificando los archivos de entrada y de salida:

```sh
./genjson [ INPUT_FILE [ OUTPUT_FILE ] ]
```

También se provee un archivo `Makefile` con una tarea `test` para procesar las entradas incluidas en este proyecto.
Estos se encuentran en la carpeta `data`, y el resultado de procesar cada archivo se escribe con el mismo nombre, en la
misma carpeta, pero con la extensión `.out`:

```sh
make test
```
