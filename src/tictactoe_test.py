
Nobody = "Nobody"
FirstPlayer = "FirstPlayer"
SecondPlayer = "SecondPlayer"

Top = 0
Left = 0
Middle = 1
Bottom = 2
Right = 2

def there_is_a_line(moves):
    return moves in [
        [(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Top, Right)],
        [(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Middle, Right), (Bottom, Right)]]


def test_there_is_a_line_by_first_player_at_the_top():
    assert there_is_a_line([(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Top, Right)])

def test_there_is_not_a_line_by_first_player_at_the_top():
    assert not there_is_a_line([(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Bottom, Right)])

def test_there_is_a_line_by_second_player_at_the_bottom():
    assert there_is_a_line(
        [(Top, Left), (Bottom, Left), (Top, Middle), (Bottom, Middle), (Middle, Right), (Bottom, Right)])


def who_wins(moves):
    if there_is_a_line(moves):
        if len(moves) == 5:
            return FirstPlayer
        else:
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
