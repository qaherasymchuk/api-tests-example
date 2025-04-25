import pytest

from pytest_schema import exact_schema
from src.author_service import AuthorService


def authors_params_contains() -> str:
    param_list = [
        "Anne B",
        "Ma",
        "Anne Bradstreet"
    ]
    yield from param_list

@pytest.mark.smoke
@pytest.mark.authors
class TestAuthorService:
    @pytest.fixture(autouse=True)
    def setup(self, author_service: AuthorService):
        self.api = author_service

    def test_get_all_authors(self):
        response = self.api.get_all()
        expected_schema = {
            "authors": [ str ],
        }
        assert exact_schema(expected_schema) == response.json(), "Schema response mismatch"
        assert response.status_code == 200
        assert response.json()['authors'] == [
            "Adam Lindsay Gordon",
            "Alan Seeger",
            "Alexander Pope",
            "Algernon Charles Swinburne",
            "Ambrose Bierce",
            "Amy Levy",
            "Andrew Marvell",
            "Ann Taylor",
            "Anne Bradstreet",
            "Anne Bronte",
            "Anne Killigrew",
            "Anne Kingsmill Finch",
            "Annie Louisa Walker",
            "Arthur Hugh Clough",
            "Ben Jonson",
            "Charles Kingsley",
            "Charles Sorley",
            "Charlotte Bronte",
            "Charlotte Smith",
            "Christina Rossetti",
            "Christopher Marlowe",
            "Christopher Smart",
            "Coventry Patmore",
            "Edgar Allan Poe",
            "Edmund Spenser",
            "Edward Fitzgerald",
            "Edward Lear",
            "Edward Taylor",
            "Edward Thomas",
            "Eliza Cook",
            "Elizabeth Barrett Browning",
            "Emily Bronte",
            "Emily Dickinson",
            "Emma Lazarus",
            "Ernest Dowson",
            "Eugene Field",
            "Francis Thompson",
            "Geoffrey Chaucer",
            "George Eliot",
            "George Gordon, Lord Byron",
            "George Herbert",
            "George Meredith",
            "Gerard Manley Hopkins",
            "Helen Hunt Jackson",
            "Henry David Thoreau",
            "Henry Vaughan",
            "Henry Wadsworth Longfellow",
            "Hugh Henry Brackenridge",
            "Isaac Watts",
            "James Henry Leigh Hunt",
            "James Thomson",
            "James Whitcomb Riley",
            "Jane Austen",
            "Jane Taylor",
            "John Clare",
            "John Donne",
            "John Dryden",
            "John Greenleaf Whittier",
            "John Keats",
            "John McCrae",
            "John Milton",
            "John Trumbull",
            "John Wilmot",
            "Jonathan Swift",
            "Joseph Warton",
            "Joyce Kilmer",
            "Julia Ward Howe",
            "Jupiter Hammon",
            "Katherine Philips",
            "Lady Mary Chudleigh",
            "Lewis Carroll",
            "Lord Alfred Tennyson",
            "Louisa May Alcott",
            "Major Henry Livingston, Jr.",
            "Mark Twain",
            "Mary Elizabeth Coleridge",
            "Matthew Arnold",
            "Matthew Prior",
            "Michael Drayton",
            "Oliver Goldsmith",
            "Oliver Wendell Holmes",
            "Oscar Wilde",
            "Paul Laurence Dunbar",
            "Percy Bysshe Shelley",
            "Philip Freneau",
            "Phillis Wheatley",
            "Ralph Waldo Emerson",
            "Richard Crashaw",
            "Richard Lovelace",
            "Robert Browning",
            "Robert Burns",
            "Robert Herrick",
            "Robert Louis Stevenson",
            "Robert Southey",
            "Robinson",
            "Rupert Brooke",
            "Samuel Coleridge",
            "Samuel Johnson",
            "Sarah Flower Adams",
            "Sidney Lanier",
            "Sir John Suckling",
            "Sir Philip Sidney",
            "Sir Thomas Wyatt",
            "Sir Walter Raleigh",
            "Sir Walter Scott",
            "Stephen Crane",
            "Thomas Campbell",
            "Thomas Chatterton",
            "Thomas Flatman",
            "Thomas Gray",
            "Thomas Hood",
            "Thomas Moore",
            "Thomas Warton",
            "Walt Whitman",
            "Walter Savage Landor",
            "Wilfred Owen",
            "William Allingham",
            "William Barnes",
            "William Blake",
            "William Browne",
            "William Cowper",
            "William Cullen Bryant",
            "William Ernest Henley",
            "William Lisle Bowles",
            "William Morris",
            "William Shakespeare",
            "William Topaz McGonagall",
            "William Vaughn Moody",
            "William Wordsworth"
        ]

    @pytest.mark.parametrize("author_param", authors_params_contains())
    def test_get_author_by_name_contains_match(self, author_param: str):
        response = self.api.get_contains(
            filter_param=author_param,
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
        assert all(author_param.lower() in actual_author['author'].lower() for actual_author in response.json()), \
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
            filter_param="Anne B",
        )
        expected = {
            "status": 404,
            "reason": "Not found"
        }
        assert response.status_code == 404, "Response status code is wrogn"
        assert response.json() == expected, "Response body doesn't match"

    def test_get_author_by_name_exact_match(self):
        param = "Anne Bradstreet"
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
        assert all(param in actual_author['author'] for actual_author in response.json())

