"""
DB for the mango tree project
"""

import sqlite3
from pathlib import Path


class MangoTreeDB:
    def __init__(self, db_directory_path: Path, db_file_prefix: str):
        db_directory_path.mkdir(parents=True, exist_ok=True)
        db_file_path = db_directory_path / f"{db_file_prefix}.sqlite"
        self._connection = sqlite3.connect(db_file_path)
        self._connection.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self) -> None:
        with self._connection:
            self._connection.execute(
                """
                CREATE TABLE IF NOT EXISTS mango_tree(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    summary TEXT,
                    owner TEXT,
                    state TEXT
                )
                """
            )

    def insert_values(self, mango_tree_fields: dict) -> int:
        with self._connection:
            cursor = self._connection.execute(
                "INSERT INTO mango_tree (summary, owner, state) VALUES (:summary, :owner, :state)",
                mango_tree_fields,
            )
        return cursor.lastrowid

    def read_by_id(self, mango_tree_id: int) -> dict | None:
        row = self._connection.execute(
            "SELECT id, summary, owner, state FROM mango_tree WHERE id = ?",
            (mango_tree_id,),
        ).fetchone()
        return dict(row) if row else None

    def read_all(self) -> list[dict]:
        rows = self._connection.execute(
            "SELECT id, summary, owner, state FROM mango_tree"
        ).fetchall()
        return [dict(row) for row in rows]

    def update_by_id(self, mango_tree_id: int, modified_fields: dict) -> int:
        allowed_column_names = {"summary", "owner", "state"}
        fields_to_update = {
            column_name: value
            for column_name, value in modified_fields.items()
            if value is not None and column_name in allowed_column_names
        }

        if not fields_to_update:
            return 0

        set_clause = ", ".join(
            f"{column_name} = :{column_name}" for column_name in fields_to_update
        )
        with self._connection:
            cursor = self._connection.execute(
                f"UPDATE mango_tree SET {set_clause} WHERE id = :id",
                {**fields_to_update, "id": mango_tree_id},
            )
        return cursor.rowcount

    def delete_by_id(self, mango_tree_id: int) -> int:
        with self._connection:
            cursor = self._connection.execute(
                "DELETE FROM mango_tree WHERE id = ?", (mango_tree_id,)
            )
        return cursor.rowcount

    def delete_all(self) -> None:
        with self._connection:
            self._connection.execute("DELETE FROM mango_tree")

    def count_items(self) -> int:
        return self._connection.execute("SELECT COUNT(*) FROM mango_tree").fetchone()[0]

    def close_db_connection(self) -> None:
        self._connection.close()
