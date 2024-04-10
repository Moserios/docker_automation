from automation.functions_db import *
from automation import data
import pytest


@pytest.mark.asyncio
@pytest.mark.e2e
def test_check_db_for_reminder():
    assert(check_database_for_data(data.r_list, data.r_item)) #, data.LOGIN
