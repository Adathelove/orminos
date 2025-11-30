# Architecture

Orminos is organized around a **pluggable backend interface**:

* **JSON backend** — current default (compatibility layer).
* **Day-Directory backend** — new backend storing each day’s registry in its own folder.
* Backends implement a single `RegistryBackend` interface (`load()` / `save()`).

Frontends include:

* The **original CLI** for registering URLs.
* The **daydir driver** (path, inspect, mkdir, init, schema) for navigating and preparing backend storage.

## Persona system

Personas are defined through lightweight files and normalization rules:

* URLs are normalized and matched against known patterns.
* If no match is found, the CLI asks the user to identify the persona.
* Each registration gets a monotonically increasing version number.