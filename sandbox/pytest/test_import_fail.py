from app.core.config import get_settings


def test_setting_upload():
    assert get_settings().app_mode == "mock"
