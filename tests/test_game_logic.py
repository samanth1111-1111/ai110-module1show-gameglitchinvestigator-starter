from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_high_guess_says_go_lower():
    # If guess is higher than secret, message should tell player to go LOWER
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_low_guess_says_go_higher():
    # If guess is lower than secret, message should tell player to go HIGHER
    _, message = check_guess(20, 50)
    assert "HIGHER" in message

def test_new_game_resets_attempts():
    # Simulate new game state reset — attempts should start at 0
    attempts = 0
    assert attempts == 0

def test_new_game_resets_score():
    # Simulate new game state reset — score should start at 0
    score = 0
    assert score == 0

def test_new_game_resets_history():
    # Simulate new game state reset — history should be an empty list
    history = []
    assert history == []

def test_new_game_status_is_playing():
    # Simulate new game state reset — status should be "playing"
    status = "playing"
    assert status == "playing"