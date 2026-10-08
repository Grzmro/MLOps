from settings import Settings


def test_settings_loaded_from_env_test():
    settings = Settings()

    assert settings.APP_NAME == "test-app"
    assert settings.ENVIRONMENT == "test"
    assert settings.API_KEY == "fake-api-key"
