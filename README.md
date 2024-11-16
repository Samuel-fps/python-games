# python-games

## Descripción

Este repositorio contiene una colección de juegos desarrollados en Python.
El principal objetivo es aprender nuevas habilidades en el desarrollo de
videojuegos simples, además de crear diversos juegos, tanto clásicos como nuevos.

Puedes contribuir, modificar y compartir los juegos bajo los términos de la
Licencia Pública General GNU v3.

## Requisitos

Para ejecutar los juegos, necesitas tener instalado:

- Python 3.12
- Bibliotecas adicionales (por definir)

## Cómo ejecutar los juegos

1. Clona el repositorio en tu máquina local:

   git clone <https://github.com/Samuel-fps/python-games.git>

2. Navega a la carpeta del juego que quieres ejecutar:

   cd nombre_del_juego

3. Si es necesario, instala las dependencias:

   pip install -r requirements.txt

4. Ejecuta el juego:

   python nombre_del_juego.py

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar los juegos o
añadir nuevas funcionalidades, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commits (git commit -am 'Añadí nueva funcionalidad').
4. Sube tus cambios a tu fork (git push origin feature/nueva-funcionalidad).
5. Crea un pull request para que revisemos tus cambios.

Por favor, asegúrate de que tus contribuciones estén bajo la licencia GNU GPL v3.

## Convenciones de Commit

Los mensajes de commit deben seguir la convención de *Conventional Commits*,
que está estructurada en la siguiente forma:

\<tipo>(<ámbito>): \<mensaje>

### Tipos de Commit

- **feat**: Se utiliza cuando se agrega una nueva funcionalidad al proyecto.
- **fix**: Se utiliza para correcciones de errores.
- **docs**: Se utiliza para cambios en la documentación.
- **style**: Se usa cuando se realizan cambios en el estilo del código, como
  formato o estructura, sin modificar la funcionalidad.
- **refactor**: Se utiliza cuando se realiza un cambio en el código que mejora
  la estructura o legibilidad, sin modificar la funcionalidad.
- **perf**: Se usa cuando se realizan cambios que mejoran el rendimiento.
- **test**: Se usa cuando se añaden o modifican pruebas.
- **chore**: Se utiliza para tareas generales de mantenimiento, como
  actualizaciones de dependencias o cambios de configuración.

### Ámbito

El ámbito es opcional, pero útil cuando se desea especificar a qué parte del
proyecto se refiere el cambio. En este repositorio, el ámbito puede ser el
nombre de un juego en particular o un componente general como "space-invaders",
"tetris", "puzzle", etc.

Ejemplos:

- **feat(tetris): add new level mechanics**
  - Agrega una nueva mecánica de niveles al juego de Tetris.
  
- **fix(tetris): fix collision detection bug**
  - Corrige un error en la detección de colisiones en el juego de Tetris.
  
- **chore(space-invaders): update game assets**
  - Actualiza los recursos visuales de space-invaders.

### Ejemplos de Mensajes de Commit

- **feat(tetris): add power-up feature**
  - Agrega una nueva característica de potenciadores en el juego Tetris.
  
- **fix(puzzle): fix bug with scoring system**
  - Corrige un error con el sistema de puntuación en el juego Puzzle.
  
- **chore(space-invaders): refactor game loop for better performance**
  - Refactoriza el bucle principal de space-invaders para mejorar el rendimiento.

### Cómo Usar Conventional Commits

1. **Inicio de un nuevo commit**: Utiliza el tipo de commit adecuado según el
   cambio que hayas realizado.
2. **Incluye el ámbito**: Si el commit está relacionado con un juego específico
   o un componente general, incluye el nombre del juego o del componente en el
   mensaje (por ejemplo, "tetris" o "juegos").
3. **Mensaje claro y conciso**: Escribe un mensaje breve pero informativo que
4. describa el cambio realizado.

Para más detalles sobre las convenciones de commit, puedes consultar la
documentación oficial de [Conventional Commits](https://www.conventionalcommits.org/).

## Licencia

Este proyecto está licenciado bajo la Licencia Pública General GNU v3. Puedes
usar, modificar y distribuir el código bajo los términos de esta licencia. Sin
embargo, no está permitido el uso comercial del código.

Ver el archivo LICENSE para más detalles.

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme a través de mi perfil
 de GitHub o por correo electrónico.

---

¡Gracias por visitar este repositorio y espero que disfrutes los juegos!
