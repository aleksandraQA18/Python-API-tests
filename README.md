# JSONPlaceholder API Tests

This repository contains automated tests for the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake REST API. The tests are written in Python using [pytest](https://pytest.org/) and validate CRUD operations for posts and users.

## Features

- Functional and integration tests for `/posts` and `/users` endpoints
- Schema validation of API responses
- Test data generation using [Faker](https://faker.readthedocs.io/)
- Fixtures for reusable test setup
- Logging for easier debugging

## Project Structure

```
.
├── factory/           # Data factories for test payloads
├── lib/               # API client classes
├── schemas/           # Response schemas for validation
├── tests/             # Test cases and pytest fixtures
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/jsonplaceholder-api-tests.git
   cd jsonplaceholder-api-tests
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running Tests

To run all tests:

```
pytest -v
```

### Notes

- The tests use the public JSONPlaceholder API, which does **not persist changes**. POST, PUT, and DELETE requests will return successful responses, but data will not actually change on the server.
- Schemas are used to validate the structure of API responses.
