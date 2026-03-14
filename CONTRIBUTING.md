# Contribuir a MCTables

¡Gracias por querer colaborar! Para mantener el proyecto organizado, por favor sigue estas guías:

## Pasos para colaborar
1. Haz un **Fork** del repositorio.
2. Crea una **rama** para tu mejora (`git checkout -b mejora-algoritmo-reloj`).
3. Realiza tus cambios y asegúrate de que el código Python sea limpio.
4. **Importante:** Ejecuta Pylint antes de subir nada: `pylint --rcfile=.pylintrc $(git ls-files '*.py')`.
5. Envía un **Pull Request**.

## Estilo de código
- Usamos **Pylint** para asegurar la calidad. No se aceptarán PRs que no pasen el check verde de GitHub Actions.
- Si necesitas añadir excepciones al linter, discútelo primero en un Issue.
- Para el código LaTeX, intenta que los comandos sean lo más genéricos posible.
