from src.blockwise import build_model


def test_build_model():
    assert build_model()["status"] == "release"
