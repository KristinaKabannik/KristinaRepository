import pytest
import logging
from homework_10 import log_event

@pytest.mark.parametrize("username, status, expected_log", [
    ("user1", "success", logging.INFO),  # Test for success login
    ("user2", "expired", logging.WARNING),  # Test for expired login
    ("user3", "failed", logging.ERROR),  # Test for failed login
])
def test_log_event(username, status, expected_log, caplog):

    # with pytest.raises(expected_log):
    #     log_event(username, status)
    with caplog.at_level(logging.INFO):  # Установлюємо рівень захоплення логів
        log_event(username, status)


        # Перевіряємо, чи правильно було зафіксовано рівень логування
        assert len(caplog.records) > 0, "Логи додались в 'login_system.log'"
