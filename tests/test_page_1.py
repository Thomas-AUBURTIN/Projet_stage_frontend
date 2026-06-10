from pathlib import Path
import sys
import types
from unittest.mock import patch
from streamlit.testing.v1 import AppTest



def test_page_1_runs():
    page_path = Path(__file__).resolve().parents[1] / "page_1.py"
    at = AppTest.from_file(str(page_path))
    at.run()
    assert not at.exception