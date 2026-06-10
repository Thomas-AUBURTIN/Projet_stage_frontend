import Proxy.proxy as pr
from unittest.mock import patch, Mock

def test_get_historique():
    fake_response = Mock()
    fake_response.json.return_value = [{"id": 1, "titre": "Test"}]
    fake_response.raise_for_status.return_value = None

    with patch("Proxy.proxy.requests.get", return_value=fake_response) as mock_get:
        data = pr.get_historique()

        mock_get.assert_called_once_with("http://127.0.0.1:8000/taches/")
        fake_response.raise_for_status.assert_called_once()
        assert data == [{"id": 1, "titre": "Test"}]

import Proxy.proxy as pr
from unittest.mock import patch, Mock

def test_post_question():
    fake_response = Mock()
    fake_response.json.return_value = {"response": "Test response"}
    fake_response.raise_for_status.return_value = None

    with patch("Proxy.proxy.requests.post", return_value=fake_response) as mock_post:
        response = pr.post_question("Test question")

        mock_post.assert_called_once_with(
            "http://127.0.0.1:8000/request_ollama/",
            json={"question": "Test question"}
        )
        assert response == fake_response
        assert response.json() == {"response": "Test response"}
