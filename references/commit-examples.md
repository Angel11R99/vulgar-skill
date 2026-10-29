# Commit message examples

These examples are manually reviewed for technical truth, language consistency, grammar, regional fit, and Conventional Commits syntax. In real use, derive the claim from the diff; examples are not templates to apply blindly. Each regional example describes the same change: add the missing image files to the blog. The English examples do the same.

## One change, different voices

1. Dominican Spanish: `fix(blog): se agregaron las imágenes que faltaban, coño`
2. Mexican Spanish: `fix(blog): por fin se agregaron las pinches imágenes que faltaban`
3. Peninsular Spanish: `fix(blog): añadidas las jodidas imágenes que faltaban`
4. Argentine Spanish: `fix(blog): por fin se agregaron las imágenes que faltaban, la puta madre`
5. Colombian Spanish: `fix(blog): se agregaron las hijueputas imágenes que faltaban`
6. American English: `fix(blog): finally added the damn missing images`
7. British English: `fix(blog): added the bloody missing images at last`
8. Australian English: `fix(blog): finally added the bloody missing images`

## English subjects

9. `feat(auth): add the damn passkey option`
10. `fix(api): stop retrying requests after the deadline`
11. `refactor(db): untangle the goddamn migration dependencies`
12. `perf(search): cache the slow query result`
13. `docs(readme): clarify the bloody installation steps`
14. `test(cache): cover expiry at the damn boundary`
15. `build(deps): update the compiler version`
16. `ci(lint): run the bloody check on release tags`
17. `chore(release): publish the damn changelog`
18. `style(ui): fix the awkward spacing`
19. `revert(api): undo the broken pagination change`
20. `fix(auth): stop the fucking refresh loop`
21. `feat(export): add CSV output, finally`
22. `fix(api): use the damn middleware to reject expired tokens`
23. `refactor(db): split query construction from execution`
24. `perf(cache): avoid repeating the same expensive lookup`
25. `fix(ui): prevent the overflow from breaking the layout`
26. `test(forms): cover empty-field validation`
27. `docs(api): explain the pagination limit, for fuck's sake`
28. `fix(queue): retry jobs only after transient failures`
29. `feat(cli): add a bloody useful dry-run mode`
30. `fix(parser): handle the empty final line`
31. `perf(images): reuse each decoded thumbnail`
32. `chore(config): remove the dog's breakfast of defaults`
33. `fix(deploy): restore the missing health check`
34. `feat(logs): add a bloody handy request identifier`
35. `refactor(ui): separate date formatting from the component`
36. `test(router): cover the broken fallback path`
37. `fix(upload): reject unsupported MIME types before storage`
38. `fix(cache): evict stale entries before they poison responses`
39. `feat(search): add a filter for active records`
40. `fix(session): preserve the secure cookie on renewal`
41. `perf(db): add the missing index to the damn slow query`
42. `docs(setup): document the first-run environment variables`
43. `fix(forms): reject whitespace-only input`
44. `build(android): report errors from the Gradle task`
45. `ci(test): rerun the flaky suite only when requested`
46. `feat(profile): add avatar cropping, finally`
47. `fix(api): restore the health endpoint after the deployment change`
48. `refactor(auth): split token validation from legacy parsing`
49. `style(web): align the menu on small screens`
50. `revert(config): undo the timeout change`
51. `fix(payment): prevent duplicate charges after retries`
52. `perf(render): render the dashboard without repeating the damn query`
53. `test(import): cover CSV fields containing quoted commas`
54. `chore(deps): remove the obsolete package`
55. `fix(worker): acknowledge jobs only after processing succeeds`
56. `feat(api)!: remove the old response envelope`

    `BREAKING CHANGE: clients must read the payload from data instead of result.`

## Spanish subjects

57. `fix(auth): corregido el maldito error de autenticación`
58. `feat(gallery): implementada la galería de imágenes, por fin`
59. `fix(images): se agregaron las imágenes que faltaban, coño`
60. `refactor(api): eliminadas las dependencias obsoletas de una puta vez`
61. `perf(cache): optimizada la consulta que iba jodidamente lenta`
62. `docs(api): aclarado el límite de paginación, coño`
63. `test(forms): cubierta la validación del campo vacío`
64. `build(android): corregida la tarea de Gradle que se tragaba los errores`
65. `ci(lint): ejecutada la comprobación también en las etiquetas de versión`
66. `chore(release): publicado el maldito registro de cambios`
67. `style(ui): corregido el espaciado del menú`
68. `revert(api): revertido el cambio de paginación que rompía los enlaces`
69. `fix(auth): detenido el puto ciclo de renovación`
70. `feat(export): agregada la salida CSV, por fin`
71. `fix(api): rechazados los tokens vencidos antes de procesarlos`
72. `refactor(db): separada la construcción de consultas de su ejecución`
73. `perf(cache): evitadas las búsquedas duplicadas, de una vez`
74. `fix(ui): corregido el desbordamiento que rompía el diseño`
75. `test(forms): cubierta la validación del campo vacío, coño`
76. `docs(api): explicado el límite de paginación para que no haya más líos`
77. `fix(queue): reintentados solo los trabajos con fallos temporales`
78. `feat(cli): agregada una opción de simulación, carajo`
79. `fix(parser): gestionada la última línea vacía`
80. `perf(images): reutilizadas las miniaturas ya decodificadas`
81. `chore(config): eliminados los valores predeterminados obsoletos`
82. `fix(deploy): restaurada la comprobación de estado que faltaba`
83. `feat(logs): agregado un identificador de petición, por fin`
84. `refactor(ui): separado el formato de fechas del componente`
85. `test(router): cubierta la ruta alternativa que fallaba`
86. `fix(upload): rechazados los tipos MIME no admitidos antes de guardar`
87. `fix(cache): eliminadas las entradas vencidas antes de que jodan la respuesta`
88. `feat(search): agregado el filtro de registros activos`
89. `fix(session): conservada la cookie segura al renovar la sesión`
90. `perf(db): agregada la maldita entrada que faltaba en el índice`
91. `docs(setup): documentadas las variables necesarias para el primer arranque`
92. `fix(forms): rechazadas las entradas que solo contienen espacios`
93. `build(android): mostrados los errores de la tarea de Gradle`
94. `ci(test): repetida la suite inestable solo cuando se solicita`
95. `feat(profile): agregada la opción de recortar el avatar, por fin`
96. `fix(api): restaurado el endpoint de estado tras el cambio de despliegue`
97. `refactor(auth): separada la validación de tokens del análisis heredado`
98. `style(web): alineado el menú en pantallas pequeñas`
99. `revert(config): deshecho el cambio de timeout`
100. `fix(payment): evitados los cobros duplicados tras los reintentos`
101. `perf(render): eliminada la consulta jodidamente repetida del panel`
102. `test(import): cubierta la importación de campos CSV con comillas`
103. `chore(deps): eliminado el paquete obsoleto de una puta vez`
104. `fix(worker): confirmados los trabajos solo después de procesarlos`

## Venezuelan Spanish: choose by meaning, not by catchphrase

These examples use different Venezuelan expressions because they describe different situations. `Qué ladilla` is appropriate for something tedious or annoying; it is not a universal regional stamp.

- Annoying repeated test failure: `test(ci): corregida esa ladilla de prueba que fallaba al azar`
- Broken deployment: `fix(deploy): restaurado el servicio que se fue a la verga`
- Added missing files: `fix(blog): agregadas las imágenes que faltaban, coño`
- Successful interface improvement: `feat(ui): por fin quedó fina la navegación móvil`
- Configuration failure: `fix(config): corregida la vaina que impedía iniciar el servicio`
- Failed merge: `fix(merge): resuelto el conflicto antes de que se jodiera todo`
- Serious defect, strong tone: `fix(api): corregida esa cagada que tumbaba el endpoint`
- Slow database query: `perf(db): acelerada la consulta de mierda que congelaba el panel`

Avoid mechanically repeating one expression across unrelated commits, for example:

```text
fix(api): corregido el bug, qué ladilla
fix(deploy): arreglado el deploy, qué ladilla
feat(ui): agregado el menú, qué ladilla
```

The repetition gives every change the same annoyed tone and makes the phrase feel pasted on. Select wording that matches each change, and vary sentence structure as well as vocabulary.

## Correct versus incorrect

Same evidence: missing image files were added to a blog.

Correct Spanish: `fix(blog): se agregaron las malditas imágenes que faltaban`

Correct English: `fix(blog): finally added the damn missing images`

Incorrect mixed-language description: `fix(blog): arreglar this fucking imágenes`

Incorrect invented action: `fix(blog): fixed the fucking image upload system` — adding image files does not establish that upload behavior was repaired.

Incorrect disconnected profanity: `fix(blog): added the images, coño joder mierda` — the exclamations do not form a natural sentence.

Incorrect action and grammar: `fix(images): fuck upload the missing images` — this is not idiomatic English and changes the action.

## Commit body examples

### Frustrated fix

```text
fix(auth): stop the damn refresh loop

An expired access token triggered another refresh request. Reuse the
in-flight promise and stop the retry pile-up when refresh fails.
```

### Spanish refactor

```text
refactor(config): separados los valores heredados en opciones claras

Una misma bandera controlaba tres comportamientos distintos. Se conserva
la compatibilidad en la interfaz y se simplifica la lógica interna.
```

### Celebratory feature

```text
feat(search): add saved filters, coño, por fin

Persist each user's filter choices and restore them on return. No more
rebuilding the same query every morning.
```

### Performance improvement

```text
perf(images): reuse each decoded thumbnail

The request now decodes an image once and reuses it. That removes the
same damn work from the repeated render path.
```

### Documentation

```text
docs(deploy): document the bloody environment variables

List the required values and safe local defaults so the service starts
without guesswork.
```
