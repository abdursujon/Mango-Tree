import pytest 
from mango_tree import MangoTree

@pytest.mark.parametrize(
        "id, task, expected_completion_time, id_exp, task_exp, time_exp", 
        [
            (1, "something", "10H", 1, "something", "10H"),
            (2, "", "", 2, "", ""),
        ]
)
def test_field_access(id, task, expected_completion_time, id_exp, task_exp, time_exp):
    m = MangoTree(id, task, expected_completion_time)
    assert m.id == id_exp
    assert m.task == task_exp
    assert m.expected_completion_time == time_exp