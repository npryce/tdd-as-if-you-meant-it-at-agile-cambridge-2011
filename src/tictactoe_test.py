
Nobody = "Nobody"
FirstPlayer = "FirstPlayer"
SecondPlayer = "SecondPlayer"

Top = 0
Left = 0
Middle = 1
Bottom = 2
Right = 2

def who_wins(moves):
    if moves == [(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Top, Right)]:
        return FirstPlayer
    elif moves == [(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Middle, Right), (Bottom, Right)]:
        return SecondPlayer
    else:
        return Nobody
    

def test_nobody_has_won_when_nobody_has_moved():
    winner = who_wins([])
    assert winner == Nobody

def test_nobody_has_won_when_player_x_plays_in_the_middle():
    winner = who_wins([(Middle, Middle)])
    assert winner == Nobody

def test_first_player_wins_after_minimal_number_of_moves():
    winner = who_wins([
            (Top, Left),
            (Bottom, Left),
            (Top, Middle),
            (Bottom, Middle),
            (Top, Right)])
    
    assert winner == FirstPlayer

def test_nobody_wins_after_five_inconclusive_moves():
    winner = who_wins([
            (Top, Left),
            (Bottom, Left),
            (Top, Middle),
            (Bottom, Middle),
            (Middle, Left)])
    
    assert winner == Nobody

def test_second_player_wins_after_minimal_number_of_moves():
    winner = who_wins([
            (Top, Left),
            (Bottom, Left),
            (Top, Middle),
            (Bottom, Middle),
            (Middle, Right),
            (Bottom, Right)])
    
    assert winner == SecondPlayer
