# Commit message examples

Illustrative only: real messages must describe the inspected changes. Strong profanity is intentional. A commit body is shown after a blank line.

1. `feat(auth): add fucking passkey support`
2. `fix(api): stop this bullshit retry loop`
3. `refactor(db): untangle the damn migration mess`
4. `perf(search): make this shitbox query fast`
5. `docs(readme): explain the bloody install steps`
6. `test(cache): cover the fucked-up expiry edge case`
7. `build(deps): bump the goddamn compiler version`
8. `ci(lint): stop the bollocks job from failing on tags`
9. `chore(release): ship the damn thing already`
10. `style(ui): fix the ugly-ass spacing`
11. `revert(api): undo that spectacularly bad shitshow`
12. `fix(auth): arreglar esta puta mierda del login`
13. `feat(export): añadir salida CSV, coño, de una vez`
14. `fix(api): pinche chingadera rejects expired tokens`
15. `refactor(db): limpiar este pinche desmadre de queries de mierda`
16. `perf(cache): speed up this shitty cache and its fucked-up lookups`
17. `fix(ui): coño, fix this goddamn layout before it breaks again`
18. `test(forms): cubrir esta cagada del formulario`
19. `docs(api): joder, aclarar el límite de paginación`
20. `fix(queue): qué quilombo, retry temporary jobs correctly`
21. `feat(cli): add a bloody useful dry-run mode`
22. `fix(parser): bollocks, handle the empty final line`
23. `perf(images): stop doing the same damn thumbnail work twice`
24. `chore(config): clean up this dog's breakfast of defaults`
25. `fix(deploy): this build is cactus, restore the health check`
26. `feat(logs): add a bloody handy request identifier`
27. `fix(auth): esta vaina no renueva el token, coño`
28. `refactor(ui): separate the damn date formatter from the component`
29. `test(router): cover the buggered fallback path`
30. `fix(upload): reject bullshit MIME types before storage`
31. `fix(cache): qué gonorrea de bug, evict stale entries`
32. `feat(search): filtrar por estado activo, juepucha`
33. `fix(session): qué ladilla, preserve the secure cookie`
34. `perf(db): this query was slower than hell; add the missing index`
35. `docs(setup): menuda mierda de instrucciones, document first run`
36. `fix(forms): la puta madre, validate the empty field`
37. `build(android): stop the goddamn Gradle task from swallowing errors`
38. `ci(test): make the flaky suite fail loudly, for fuck's sake`
39. `feat(profile): add avatar cropping, coño, por fin`
40. `fix(api): qué cagada de deploy, restore the health endpoint`
41. `refactor(auth): split token validation from that legacy shit`
42. `style(web): align the bloody menu without breaking mobile`
43. `revert(config): undo the pinche timeout change`
44. `fix(payment): prevent a fucked-up duplicate charge`
45. `perf(render): render the damn dashboard in half the time`
46. `test(import): cover the cabrón CSV with quoted commas`
47. `chore(deps): remove this useless pile of crap`
48. `fix(worker): this pije bug keeps eating jobs, ack after processing`
49. `feat(api)!: remove the old damn response envelope`

    BREAKING CHANGE: clients must read the payload from data instead of result.

50. `fix(auth): stop the fucking loop`
51. `fix(api): stop this fucking retry loop and its bullshit backoff`
52. `refactor(db): untangle this goddamn query mess, coño`
53. `feat(cli): add the damn dry run, no mames`
54. `fix(cache): qué mierda, evict the stale key before it fucks up the response`
55. `test(ui): bloody hell, cover the broken focus trap`

## Commit body examples

### Frustrated bug fix

```text
fix(auth): stop this fucking refresh loop

The expired access token kept triggering another refresh request. Reuse the
in-flight promise and stop this bullshit pile-up when refresh fails.
```

### Sarcastic refactor

```text
refactor(config): split the legacy crap into named settings

One flag used to mean three different things, because apparently that was a
good idea. Keep compatibility at the boundary and make the internals sane.
```

### Celebratory feature

```text
feat(search): add saved filters, coño, por fin

Persist each user's filter choices and restore them on return. No more
rebuilding the same damn query every morning.
```

### Performance win

```text
perf(images): stop decoding the same damn thumbnail twice

Reuse the decoded image within a request. The old path was doing extra work
for absolutely no fucking reason.
```

### Documentation frustration

```text
docs(deploy): explain the bloody environment variables

Document the required values and safe local defaults. The old instructions
left out the one setting that made the whole damn service boot.
```
