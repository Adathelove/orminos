# PLAN.md — Orminos System Plan

**Version: 1.0 (2025-11-29)**
**Authoritative architecture & direction**

---

# 1. Purpose

Orminos is a **persona-centric registry system** designed to track:

* **Which persona** a given URL/chat/session belongs to
* **Which version** of that persona was active
* **What happened on a given day** (daily segmentation)
* **How to quickly find past interactions across days and personas**

It is *not* an event logging system.
It is a **persona organization layer** with daily structure.

Orminos must:

* Work with different frontends (CLI today, UI later)
* Support multiple storage backends (JSON → DayDir → DB → remote)
* Evolve without breaking workflows
* Maintain validated, recoverable state at all times

---

# 2. Core Philosophy

### **Frontends evolve. Backends stay replaceable.**

Frontends must never depend on how storage is implemented.

### **Storage is storage; UI is UI; logic is logic.**

Separation of concerns is mandatory.

### **Strict validation and explicit failure.**

Invalid states must prevent writes and must log diagnostics.

### **Daily segmentation is canonical.**

Future backends may store however they want, but days remain the conceptual structure.

### **Rule-based persona detection.**

Pattern-based. Deterministic. No AI learning unless intentionally later.

---

# 3. High-Level Architecture

```
+-------------------------------------------------------------+
|                           Frontends                         |
|      - registry.py (legacy CLI)                             |
|      - daydir driver (new CLI)                              |
|      - future UI / TUI                                      |
+-------------------------------------------------------------+
|                         Registry Layer                       |
|      - registry_ops (pure logic)                             |
|      - persona resolution, normalization                      |
|      - versioning                                             |
+-------------------------------------------------------------+
|                         Backend Layer                        |
|      - RegistryBackend protocol                               |
|      - JSON backend (legacy)                                 |
|      - DayDir backend (future primary)                       |
|      - (future) SQLite / remote / encrypted                  |
+-------------------------------------------------------------+
|                    Validation + Settings                     |
|      - settings loader (validated)                           |
|      - path/name validation                                  |
|      - override model                                        |
+-------------------------------------------------------------+
|                              Utilities                       |
|      - logger subsystem                                      |
|      - date/naming utilities                                 |
|      - completion scripts                                    |
|      - test scaffolding                                      |
+-------------------------------------------------------------+
```

---

# 4. Strategic Paths (Corrected & Unified)

Two original directions:

### **Path A — Monolithic JSON World**

* Keep the legacy `registry.json`
* Slowly add abstractions
* Replace when ready

### **Path B — Day Directory World**

* Each day has a folder
* Contains its own `registry.json`
* Strong validation and safe I/O

### **Final Direction: A + B Merge**

* **JSON backend stays for compatibility**
* **DayDir backend is the future system**
* Backend interface allows seamless switching

---

# 5. Backend Plan

## 5.1 Current Backends

### **JSON Backend (Legacy)**

* Mirrors original behavior
* Still default until DayDir stabilizes

### **DayDir Backend (New)**

* Per-day folder: `YYYY-MM-DD-EEE`
* Per-day registry.json
* Strong validation and override model

## 5.2 Future Backends (Optional)

* SQLite
* Remote HTTP API
* Encrypted storage
* Hybrid approaches

## 5.3 Backend Guarantees

All backends must:

* Implement RegistryBackend protocol
* Provide same dictionary semantics
* Never surprise frontends
* Support migration when needed

---

# 6. Frontend Plan

Frontends must remain independent of backend shape.

### **Current frontends**

1. **Legacy CLI** (registry.py)
2. **DayDir Driver CLI** (path/inspect/mkdir/init/schema)

### **Future frontends (Optional)**

* TUI
* Local web UI
* Query-oriented UI

---

# 7. Persona System

### **Current:**

* Normalize URL
* Pattern-based match
* Prompt if unknown
* Maintain persona versions

### **Your clarifications:**

* No AI persona inference
* URL matching is acceptable but hacky and temporary
* Future metadata may include emoji, color, synonyms

### **Long-term goals:**

* Rich metadata
* Synonyms and normalization hints
* View persona history across days

---

# 8. Day Directory Model (Future Primary Backend)

### **Behavior:**

* A folder per day: `YYYY-MM-DD-EEE`
* Inside: registry.json
* Validation of root, folder name, combined path

### **Override-first rule (your correction):**

```
If DAYDIR_OVERRIDE_ROOT is set → use it.
Else use settings.storage_root.
No other source of truth.
```

### **Creation Rules:**

* Backend creates **daydir itself** if needed
* Parent directories are never implicitly created
* Validators never modify filesystem

### **Safety:**

* No writes on invalid state
* Strong logging
* System usable even when misconfigured

---

# 9. Validation Layer

* Validates storage_root
* Validates daydir names
* Validates combined paths
* Prevents traversal and implicit creation
* Always logs failures

---

# 10. Logging Layer

* Uniform, color-coded output
* info/debug/warn/fail/abort/success/exception
* All subsystems funnel through it
* Essential for debugging broken states

---

# 11. Settings Layer

* Validated on load
* Single consistent config
* Override-first model
* JSON-based for now

---

# 12. Testing Plan

Current:

* pytest scaffold
* validation tests
* logger tests

Future:

* daydir backend correctness
* path/override correctness
* persona workflows
* backend interface stability

---

# 13. Development Roadmap (A5.x → A8.x)

### **A5.x — DayDir Stabilization**

* Finalize override-first
* Harden validation
* Confirm registry.json schema

### **A6.x — Frontend Integration**

* Add DayDir awareness to legacy CLI
* Unify help text & wording

### **A7.x — Persona Enrichment**

* Metadata file
* Synonyms
* Normalization hints
* Tests

### **A8.x — Backend Convergence**

* Make DayDir default
* JSON becomes legacy but available
* Migration tooling (optional)

### **Future (Optional)**

* DB backend
* UI layer
* History browsing
* Metadata expansion
* External integrations

---

# 14. End State Vision

A **modular**, **validated**, **persona-centric**, **time-structured** system capable of:

* Tracking personas across days
* Identifying persona for any URL/chat
* Maintaining versioned persona history
* Supporting multiple frontends/backends
* Failing safely
* Evolving cleanly without breaking users
* Remaining transparent and debuggable

---

# 15. One-Sentence Summary

> **Build a modular, backend-agnostic persona registry organized by day, with the DayDir backend as the long-term model, governed by strict validation, structured logging, and independent frontends.**

