from pathlib import Path
from unittest.mock import patch
from streamlit.testing.v1 import AppTest


def test_page_1_affiche_historique():
    fake_historique = [
        {"question": "Bonjour", "reponse": "Salut"}
    ]

    page_path = Path(__file__).resolve().parents[1] / "page_2.py"

    with patch("Proxy.proxy.get_historique", return_value=fake_historique):
        at = AppTest.from_file(str(page_path))
        at.run()

        assert not at.exception
        assert at.title[0].value == "Démo st.chat_message"
        assert at.chat_message[0].avatar == "user"
        assert at.chat_message[1].avatar == "assistant"
