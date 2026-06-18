# Changelog

## v0.2.0 - 2026-06-19

### Added

#### Package Management & Distribution

* Added `pyproject.toml` with `setuptools` build configuration.
* Converted the project into an installable Python package named `data-manager-framework`.
* Adopted the `src/` project layout.
* Added `requirements.txt` with pinned dependencies for reproducible environments.

#### Pipeline Runner

* Added a centralized `Runner` class for orchestrating multi-job pipelines.
* Implemented sequential execution of jobs and their associated contexts.
* Added logging support for pipeline and job execution tracking.

#### Transaction & State Management

* Added `_Savepoint` for tracking transactional checkpoints.
* Added `_Record` helper for capturing changes before data mutations.
* Implemented column-level delta tracking through `_record_column()`.
* Implemented table snapshot support through `_record_table()`.
* Established the foundation for savepoint-based rollback functionality.

#### Analytics & Development Tooling

* Added support for testing with `pytest`.
* Added Jupyter Notebook support for experimentation and analysis.
* Added machine learning dependencies via `scikit-learn`.
* Added visualization dependencies via `matplotlib` and `seaborn`.

### Internal

* Refactored framework architecture toward a centralized pipeline execution model.
* Introduced transaction-aware storage design for future rollback and recovery features.
