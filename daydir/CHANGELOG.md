# Changelog

## [0.2.0] - 2025-11-28

### Added

* Initial persona_db monolithic implementation (`f16746b`)
* Extract DB utilities into `db.py` (`61af3d5`)
* Extract `icu_date()` into `date_utils.py` (`4786bd5`)
* Persona matching scaffold extracted into `persona_match.py` (`d9df104`)
* Bash completion for CLI (`5309e92`)
* Begin Phyle-driven persona loading scaffold (`c53d640`, `e519e47`)
* Extract argument parsing into `cli_parser.py` (`63a4d6b`)
* Extract registration workflow into `registry_ops.py` (`51bb09e`)
* Extract output formatting into `cli_output.py` (`614e308`)
* Add persona/date collision detection, platform abstractions (`5dd464c`)
* UTF-8 emoji-safe DB + output (`6139cdc`)
* Resilient DB loading for malformed files (`89369a7`)
* Pre-save same-day collision confirmation flow (`429654b`)
* Add `--today` daily listing (`8ee5584`)
* Add repo-relative environment bootstrap `starter.sh` (`40a2ac8`)
* Rename `persona_db` → `registry.py`, update completions (`ed541e4`)
* Split today flow into core/output modules (`3ac8197`)
* Add today-picker interactive selection (`d96dfed`)
* Add auto URL capture from active Safari tab (`d96dfed`)

## [0.1.0] - 2025-11-28

* initial version
