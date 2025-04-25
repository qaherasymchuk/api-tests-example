import os

import pytest
from loguru import logger

from src.author_service import AuthorService
from src.title_service import TitleService


@pytest.fixture(name="configure_logger", scope="package", autouse=True)
def configure_logger_fixture():
    test_output_log_file = f"{os.environ.get('TEST_LOG_DIR_PATH')}/test_output.log"
    if os.path.exists(test_output_log_file):
        os.remove(test_output_log_file)
    logger.add(
        f"{os.environ.get('TEST_LOG_DIR_PATH')}/test_output.log",
        format="{time} {level} {message}",
        level=os.environ.get("TEST_LOG_LEVEL", "INFO"),
        rotation="10 MB"
    )


@pytest.fixture(scope="package")
def author_service() -> AuthorService:
    yield AuthorService()


@pytest.fixture(scope="package")
def title_service() -> TitleService:
    yield TitleService()
