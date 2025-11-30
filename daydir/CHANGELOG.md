# Changelog

## [0.2.0] - 2025-11-28

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
