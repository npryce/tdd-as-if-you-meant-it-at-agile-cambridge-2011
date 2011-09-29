
Nobody = ""

def who_wins():
    return Nobody


def test_when_nobody_wins():
    winner = who_wins()
    assert winner == Nobody

