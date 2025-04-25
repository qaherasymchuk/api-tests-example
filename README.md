# Poetry API Tests

This project includes automated tests for the Poetry API's **Author** and **Title** services. Tests are written in Python using `pytest` and validate API responses for correctness, structure, and expected behavior.

Pylint check:  
[![PyLint check](https://github.com/qaherasymchuk/api-tests-example/actions/workflows/run_pylint_check.yml/badge.svg)](https://github.com/qaherasymchuk/api-tests-example/actions/workflows/run_pylint_check.yml)

Test runs:  
[![UI tests](https://github.com/qaherasymchuk/api-tests-example/actions/workflows/run_api_tests.yml/badge.svg)](https://github.com/qaherasymchuk/api-tests-example/actions/workflows/run_api_tests.yml)


## Test Coverage

### 🧪 `test_author_service.py`

| Test Case Name                          | Description                                                                                   | Validations Used                                                               |
|----------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| test_get_all_authors                   | Verifies full list of authors is returned with correct schema and order                       | ✅ Status code = 200<br>✅ JSON schema<br>✅ Full expected author list match      |
| test_get_author_by_name_contains_match | Checks partial matches return correct results with expected fields                            | ✅ Status code = 200<br>✅ JSON schema<br>✅ Each result contains query string    |
| test_get_author_not_found_contains     | Ensures searching a non-existent author returns 404 and correct error body                    | ✅ Status code = 404<br>✅ Exact JSON body                                       |
| test_get_author_not_found_exact_match  | Ensures exact match with non-existent name returns 404                                        | ✅ Status code = 404<br>✅ Exact JSON body                                       |
| test_get_author_by_name_exact_match    | Checks exact match returns full author data with lines, titles, and names                     | ✅ Status code = 200<br>✅ JSON schema<br>✅ Author name matches exactly          |

---

### 🧪 `test_title_service.py`

| Test Case Name                          | Description                                                                                   | Validations Used |
|----------------------------------------|-----------------------------------------------------------------------------------------------|------------------|
| test_get_all_titles                    | Verifies all titles are returned and list is not empty                                        | ✅ Status code = 200<br>✅ JSON schema<br>✅ Length > 0 |
| test_get_author_by_name_contains_match | Checks partial match on title returns valid results                                           | ✅ Status code = 200<br>✅ JSON schema<br>✅ Each result contains query string |
| test_get_author_not_found_contains     | Verifies title search with no match returns 404 and correct error format                      | ✅ Status code = 404<br>✅ Exact JSON body |
| test_get_author_not_found_exact_match  | Checks exact match title search with no result returns 404                                    | ✅ Status code = 404<br>✅ Exact JSON body |
| test_get_author_by_name_exact_match    | Verifies full details (author, title, lines) for exact title match are returned               | ✅ Status code = 200<br>✅ JSON schema<br>✅ Exact title match |

---

## Validation Strategy

### ✅ **Schema Validation**

Used in: All successful API responses

- **Tool**: `pytest_schema.exact_schema`
- **Why**: Ensures that the structure of the response is **exactly** what is expected — no missing or unexpected fields. This makes the API contract clear and robust, preventing issues when consuming the API downstream.

### ✅ **Status Code Checks**

Used in: Every test

- **Why**: HTTP status codes confirm whether the server responded as expected (200 for success, 404 for not found). This is the most basic and critical validation.

### ✅ **Content Validations**

- **Exact match checks**: Used to ensure correct authors/titles are returned when using strict search.
- **Partial match assertions (`contains`)**: Validates that every response item actually contains the search term in its respective field.
- **Why**: These validations make sure the search functionality of the API is working correctly, both for fuzzy and exact match modes.

---

## Notes

- Tests use dependency injection via pytest fixtures.
- Both Author and Title services use identical API structures and validation logic.
- Hardcoded values are intentional to simulate known dataset responses and keep assertions strict.

