import pytest

from pytest_schema import exact_schema
from src.title_service import TitleService


def titles_params_contains() -> str:
    param_list = [
        "All",
        "--",
        "247. Ode, Sacred to the Memory of Mrs. Oswald of Auchencruive"
    ]
    yield from param_list

@pytest.mark.smoke
@pytest.mark.titles
class TestTitleService:
    @pytest.fixture(autouse=True)
    def setup(self, title_service: TitleService):
        self.api = title_service

    def test_get_all_titles(self):
        response = self.api.get_all()
        expected_schema = {
            "titles": [ str ],
        }
        assert exact_schema(expected_schema) == response.json(), "Schema response mismatch"
        assert response.status_code == 200
        assert len(response.json()['titles']) > 0

    @pytest.mark.parametrize("title_param", titles_params_contains())
    def test_get_author_by_name_contains_match(self, title_param: str):
        response = self.api.get_contains(
            filter_param=title_param,
            fields=["author", "title"]
        )
        expected_schema = [
            {
                "author": str,
                "title": str
            }
        ]
        assert exact_schema(expected_schema) == response.json(), "Schema response mismatch"
        assert response.status_code == 200, "Response status code is wrogn"
        assert all(title_param.lower() in actual_author['title'].lower() for actual_author in response.json()), \
            "Not all items contains author name in response"

    def test_get_author_not_found_contains(self):
        response = self.api.get_contains(
            filter_param="NON EXISTING"
        )
        expected = {
            "status": 404,
            "reason": "Not found"
        }
        assert response.status_code == 404, "Response status code is wrogn"
        assert response.json() == expected, "Response body doesn't match"

    def test_get_author_not_found_exact_match(self):
        response = self.api.get_exact_match(
            filter_param="All",
        )
        expected = {
            "status": 404,
            "reason": "Not found"
        }
        assert response.status_code == 404, "Response status code is wrogn"
        assert response.json() == expected, "Response body doesn't match"

    def test_get_author_by_name_exact_match(self):
        param = "247. Ode, Sacred to the Memory of Mrs. Oswald of Auchencruive"
        response = self.api.get_exact_match(
            filter_param=param,
            fields=["author", "title", "lines"]
        )
        expected_schema = [
            {
                "author": str,
                "title": str,
                "lines": [str]
            }
        ]
        assert exact_schema(expected_schema) == response.json(), "Schema response mismatch"
        assert response.status_code == 200
        assert all(param in actual_author['title'] for actual_author in response.json())

