# Orminos — Persona Registry Tool

Orminos is a small CLI-driven system for **registering URLs to personas**, tracking **which persona a link belongs to**, and maintaining **versioned entries** for each registration. The tool is structured so that both **frontends (CLI layers)** and **backends (storage engines)** can evolve independently.

## What it does

* Normalizes and matches URLs to known personas.
* Prompts for persona selection when no match exists.
* Assigns and increments persona-version numbers.
* Records the registration in a **registry backend**.

## Architecture

See `Architecture/Architecture.md`

## Status

The system is under active development, with the goal of allowing multiple storage backends and multiple CLI/UI entrypoints without breaking existing behavior.

