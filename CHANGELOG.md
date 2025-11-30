# Changelog

## [0.3.0] - 2025-11-29

### Features

* Introduce full daydir driver CLI (path/inspect/mkdir/init/schema) (`5fc63aa`)
* Add daydir naming (`YYYY-MM-DD-EEE`) (`72ec95a`)
* Add daydir path computation scaffolds (`72ec95a`, `3e1c028`)
* Add validation subsystem (storage_root, daydir name, combined path) (`9116071`, `ff1f4bf`)
* Add daydir CLI override harness (`5fc63aa`)
* Add completions for daydir driver (`5fc63aa`)
* Add daydir schema draft (`5fc63aa`)
* Add settings bootstrap and validation (`75520eb`)
* Add logger subsystem with color-coded output (`db51f56`)
* Add backend abstraction layer (`204834a`)
* Add JSON backend + adapter scaffolds (`a3f563b`, `b3b9344`)
* Add day-directory backend scaffolding and later read/load implementations (`72ec95a`, `2a6834e`, `1bb35d0`)
* Add initial test scaffolding (pytest conftest, validate tests) (`ceb8311`, `ff1f4bf`)

### Refactors

* Integrate validate_daydir_path into pathing (`3e1c028`)
* Restructure daydir pathing to override-first model (`5fc63aa`)
* Move persona resolution logic into persona/ package (`4f8288c`, `c58dfbd`)
* Update backend entrypoint to toggle daydir backend (`eb33f06`)
* Rewire registry_ops to use backend load/save (`f951f2c`, `9116071`)
* Split today logic and consolidate naming/pathing responsibilities (`3e1c028`)

### Fixes

* Fix CHANGELOG rewrite consistency (`95058e1`)
* Improve validate_storage_root error handling (`9116071`)
* Improve test cleanup logic (`ff1f4bf`)

## [0.2.0] - 2025-11-28] - 2025-11-28

### Features

* Introduce initial monolithic CLI (`persona_db.py`) (`f16746b`)
* Add bash completion script for CLI (`5309e92`)
* Begin Phyle-driven persona loading scaffold (intentionally broken intermediate stage) (`c53d640`)
* Implement Phyle-based loader fix, removing static dict (`e519e47`)
* Add URL registration workflow (`registry_ops.py`) (`51bb09e`)
* Add persona/date collision detection, normalization, platform opener (`5dd464c`)
* Add pre-save same-day collision confirmation flow (`429654b`)
* Add `--today` daily listing (`8ee5584`)
* Add repo-relative environment bootstrap (`starter.sh`) initial version (`40a2ac8`)
* Add interactive today-picker and Safari auto-URL capture (`d96dfed`)

### Refactors

* Extract DB utilities into `db.py` (`61af3d5`)
* Extract `icu_date()` into `date_utils.py` (`4786bd5`)
* Extract persona matching scaffold (`d9df104`)
* Extract `cli_parser.py` for argument parsing (`63a4d6b`)
* Extract output formatting into `cli_output.py` (`614e308`)
* Extract persona resolution into `resolve_persona.py` (`731a3c6`)
* Split today logic into core/output (`3ac8197`)
* Rename `persona_db.py` → `registry.py`, update completions (`ed541e4`)
* Update starter.sh to new completion path (`d96dfed`)

### Fixes

* Preserve UTF‑8 emoji in DB + CLI output (`6139cdc`)
* Make load_db resilient to empty/malformed JSON (`89369a7`)

## [0.1.0] - 2025-11-28

* 2025-11-28
* initial version
