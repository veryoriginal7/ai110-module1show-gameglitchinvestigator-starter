from ..logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_guess_with_string_secret():
    # Test with secret as string (glitchy behavior)
    outcome, message = check_guess(5, "10")
    assert outcome == "Too Low"  # 5 < 10
    assert "HIGHER" in message

    outcome, message = check_guess(15, "10")
    assert outcome == "Too High"  # 15 > 10
    assert "LOWER" in message

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None

def test_parse_guess_float():
    ok, value, err = parse_guess("42.0")
    assert ok == True
    assert value == 42
    assert err is None

def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok == False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok == False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok == False
    assert value is None
    assert err == "Enter a guess."
