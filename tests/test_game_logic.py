from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "� Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")
def test_hint_message_correctness():
    # FIX: Added test to verify hint messages guide correctly, using Copilot to generate the test case
    # Specifically test that the hint messages guide the player correctly
    # For guess > secret, should say "Go LOWER!"
    result_high = check_guess(60, 50)
    assert result_high[0] == "Too High"
    assert "LOWER" in result_high[1]
    
    # For guess < secret, should say "Go HIGHER!"
    result_low = check_guess(40, 50)
    assert result_low[0] == "Too Low"
    assert "HIGHER" in result_low[1]