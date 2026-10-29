import pytest

def test_passing():
    assert [] == []
    assert (2, 3, 9) == (2, 3, 9)
    assert {} == {}
    assert () == ()
    assert 2 == 2
    assert True == True
    assert False == False 
    assert chr(4) == chr(4)

@pytest.mark.skip()
def test_failing():
    assert True == False 

@pytest.mark.xfail()
def test_failing_two():
    assert True == False

# Expected fail but ran and passed
@pytest.mark.xfail()
def test_failing_three():
    assert True == True

@pytest.mark.xpass()
def test_failing_four():
    assert True == True

# Expected pass but failed example 
@pytest.mark.xpass()
def test_failing_five():
    assert True == False

@pytest.mark.xpass()
def test_failing_seven():
    assert True == True