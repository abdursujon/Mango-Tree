"""
API for the mango tree project
"""

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from .db import MangoTreeDB


__all__ = [
    "MangoTree",
    "MangoTreeService",
    "MangoTreeException",
    "MissingSummary",
    "InvalidMangoTreeId",
]


# Dataclasses auto generate __init__, __repr__ and __eq__ for classes that mainly hold data, therefore we skip boilerplate code
@dataclass
class MangoTree:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    # this makes the next method belongs to class rather thatn to an object
    @classmethod
    def from_dict(cls, data):
        # creates something similar to {"summary": "Water", "owner": "Ali", "state": "todo", "id": 1}
        return MangoTree(**data)

    # returns something similar to {"summary": "Water", "owner": "Ali", "state": "todo", "id": 3}
    def to_dict(self):
        return asdict(self)


class MangoTreeException(Exception):
    pass


class MissingSummary(MangoTreeException):
    pass


class InvalidMangoTreeId(MangoTreeException):
    pass


class MangoTreeService:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = MangoTreeDB(db_path, ".mango_tree_db")

    def add_to_do(self, mango_tree: MangoTree) -> int:
        """Add a to do, return the id of added to do"""
        if not mango_tree.summary:
            raise MissingSummary

        if mango_tree.owner is None:
            mango_tree.owner = ""

        id = self._db.insert_values(mango_tree.to_dict())
        return id

    def get_to_do(self, mango_tree_id: int) -> MangoTree:
        """Return a to do with a matching id."""
        db_item = self._db.read_by_id(mango_tree_id)
        if db_item is not None:
            return MangoTree.from_dict(db_item)
        else:
            raise InvalidMangoTreeId(mango_tree_id)

    def list_all_to_do(self, owner=None, state=None):
        """Return a list of all to do items saved in mango tree"""
        all_to_do = self._db.read_all()

        if (owner is not None) and (state is not None):
            return [
                MangoTree.from_dict(each_item)
                for each_item in all_to_do
                if (each_item["owner"]) == owner and each_item["state"] == state
            ]
        elif owner is not None:
            return [
                MangoTree.from_dict(each_item)
                for each_item in all_to_do
                if each_item["owner"] == owner
            ]
        elif state is not None:
            return [
                MangoTree.from_dict(each_item)
                for each_item in all_to_do
                if each_item["state"] == state
            ]
        else:
            return [MangoTree.from_dict(each_item) for each_item in all_to_do]

    def count_number_of_task(self) -> int:
        """Returns count of how many items in mango tree db"""
        return self._db.count_items()

    def update_to_do(self, mango_tree_id: int, mango_tree_update: MangoTree) -> None:
        """Updates an existing to do"""
        if self._db.update_by_id(mango_tree_id, mango_tree_update.to_dict()) == 0:
            raise InvalidMangoTreeId(mango_tree_id)

    def start(self, mango_tree_id: int):
        """Set a to do state to 'in prog'."""
        self.update_to_do(mango_tree_id, MangoTree(state="in prog"))

    def finish(self, mango_tree_id: int):
        """Set a to do state to 'done'."""
        self.update_to_do(mango_tree_id, MangoTree(state="done"))

    def delete_to_do(self, mango_tree_id: int) -> None:
        """Remove a to do from db with given mango_tree_id."""
        if self._db.delete_by_id(mango_tree_id) == 0:
            raise InvalidMangoTreeId(mango_tree_id)

    def delete_all_to_do(self) -> None:
        self._db.delete_all()

    def close_db(self):
        self._db.close_db_connection()

    def path(self):
        return self._db_path
