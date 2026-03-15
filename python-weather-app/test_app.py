from app import get_weather

def test_weather():
    assert get_weather() == "It's always sunny in the terminal!"