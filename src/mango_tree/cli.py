# typer turns python functions into terminal command
import typer
import mango_tree
from typing import List 
from contextlib import contextmanager
import os
import pathlib
from rich.table import Table
from io import StringIO
import rich 

def get_path():
    db_path_env = os.getenv("MANGO_TREE_DB_DIR", "")
    if db_path_env:
        db_path = pathlib.Path(db_path_env)
    else:
        db_path = pathlib.Path.home() / "mango_tree_db"
    return db_path


@contextmanager
def mango_tree_db():
    db_path = get_path()
    db = mango_tree.MangoTreeService(db_path)
    try:
        yield db
    finally:
        db.close_db()


app = typer.Typer(add_completion=False)

@app.command()
def version():
    """Return version of mango_tree application"""
    print(mango_tree.__version__)


@app.command()
def add(
    summary: List[str], owner: str = typer.Option(None, "-o", "--owner")
):
    """Add a to do to mango tree db."""
    summary = " ".join(summary) if summary else None
    
    with mango_tree_db() as db:
        db.add_to_do(mango_tree.MangoTree(summary, owner, state="todo"))


@app.command()
def delete(mango_tree_id: int):
    """Remove a to do from the database with given id."""
    with mango_tree_db() as db:
        try:
            db.delete_to_do(mango_tree_id)
        except mango_tree.InvalidMangoTreeId:
            print(f"Error: Invalid to do id {mango_tree_id}")



@app.command("list")
def list_task(
    owner: str = typer.Option(None, "-o", "--owner"),
    state: str = typer.Option(None, "-s", "--state"),
):
    """
    List all tasks 
    """
    with mango_tree_db() as db:
        the_mango_tree = db.list_all_to_do(owner=owner, state=state)
        table = Table(box=rich.box.SIMPLE)
        table.add_column("ID")
        table.add_column("state")
        table.add_column("owner")
        table.add_column("summary")
        for to_do in the_mango_tree:
            owner = "" if to_do.owner is None else to_do.owner
            table.add_row(str(to_do.id), to_do.state, owner, to_do.summary)
        out = StringIO()
        rich.print(table, file=out)
        print(out.getvalue())



@app.command()
def update(
    mango_tree_id: int,
    owner: str = typer.Option(None, "-o", "--owner"),
    summary: List[str] = typer.Option(None, "-s", "--summary"),
):
    """Modify a to do in db with given id with new info."""
    summary = " ".join(summary) if summary else None
    with mango_tree_db() as db:
        try:
            db.update_to_do(
                mango_tree_id, mango_tree.MangoTree(summary, owner, state=None)
            )
        except mango_tree.InvalidMangoTreeId:
            print(f"Error: Invalid to do id {mango_tree_id}")


@app.command()
def start(mango_tree_id: int):
    """Set a to do state to 'in prog'."""
    with mango_tree_db() as db:
        try:
            db.start(mango_tree_id)
        except mango_tree.InvalidMangoTreeId:
            print(f"Error: Invalid to do id {mango_tree_id}")


@app.command()
def finish(mango_tree_id: int):
    """Set a to do state to 'done'."""
    with mango_tree_db() as db:
        try:
            db.finish(mango_tree_id)
        except mango_tree.InvalidMangoTreeId:
            print(f"Error: Invalid to do id {mango_tree_id}")


@app.command()
def config():
    """List the path to the mango_tree db."""
    with mango_tree_db() as db:
        print(db.path())


@app.command()
def count():
    """Return number of mango_tree in db."""
    with mango_tree_db() as db:
        print(db.count_number_of_task())


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    mango_tree is a small command line task tracking application.
    """
    if ctx.invoked_subcommand is None:
        list_task(owner=None, state=None)