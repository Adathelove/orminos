# Orminos — Persona Registry Tool

Orminos is a small CLI-driven system for **registering URLs to personas**, tracking **which persona a link belongs to**, and maintaining **versioned entries** for each registration. The tool is structured so that both **frontends (CLI layers)** and **backends (storage engines)** can evolve independently.

## What it does

* Normalizes and matches URLs to known personas.
* Prompts for persona selection when no match exists.
* Assigns and increments persona-version numbers.
* Records the registration in a **registry backend**.

## Architecture

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

## Status

The system is under active development, with the goal of allowing multiple storage backends and multiple CLI/UI entrypoints without breaking existing behavior.

