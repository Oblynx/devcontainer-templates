"This module is only relevant if you run asyncio tests with pytest. Otherwise, delete this file."

import pytest


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"
