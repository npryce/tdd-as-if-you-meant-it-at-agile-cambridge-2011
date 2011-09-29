
Nobody = ""


def test_when_nobody_wins():
    def who_wins():
        return Nobody
    
    winner = who_wins()
    assert winner == Nobody

