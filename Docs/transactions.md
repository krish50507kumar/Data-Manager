# Transaction Engine (Internal)

The framework includes a built-in state management system to ensure data integrity during complex engineering jobs. 

## Core Components
* **Savepoints (`_Savepoint`)**: Markers in the execution stack that track changes (`deltas`) made to the dataset.
* **State Recording (`_Record`)**: Before a transformation modifies the underlying data, the framework records the pre-mutation state of specific columns or the entire table. This provides the foundational logic required to undo operations or roll back to a safe state if a validation step fails.