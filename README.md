# API Testing Automation with Pytest & Requests

##  Project Overview

This repository demonstrates **professional automated API testing** using **Pytest** and **Requests**. It tests a public REST API (JSONPlaceholder) and showcases industry-standard practices including **environment configuration**, **positive and negative tests**, **data-driven testing**, and **comprehensive API test planning**.

**QA Skills Demonstrated:**
- Writing maintainable API tests using Requests
- Designing comprehensive API test strategies
- Implementing data-driven testing with Pytest
- Environment-specific configuration management
- Testing positive and negative scenarios
- Professional test reporting and documentation

---

##  API Test Plan

### Scope
This test suite covers the JSONPlaceholder API endpoints:
- **Users:** GET, POST, PUT, DELETE operations
- **Posts:** GET, POST, PUT, DELETE operations
- **Comments:** GET operations
- **Todos:** GET operations

### Test Levels
- **Positive Tests:** Verify successful API operations with valid data
- **Negative Tests:** Verify proper error handling with invalid data
- **Edge Cases:** Test boundary conditions and special scenarios
- **Performance Tests:** Verify response times meet requirements

### Test Environment
- **Base URL:** https://jsonplaceholder.typicode.com
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Response Format:** JSON
- **Authentication:** None (public API)

### Risk Assessment
- **High Priority:** User CRUD operations, Post CRUD operations
- **Medium Priority:** Comment retrieval, Todo retrieval
- **Low Priority:** Edge cases, performance metrics

### Test Data Strategy
- Use data-driven testing for multiple scenarios
- Maintain separate test data for different environments
- Validate response structure and content

---

##  Tech Stack

| Tool | Version | Purpose |
| :--- | :--- | :--- |
| **Python** | 3.9+ | Test scripting language |
| **Requests** | Latest | HTTP library for API interaction |
| **Pytest** | Latest | Test framework and runner |
| **Pytest-Parametrize** | Built-in | Data-driven testing |
| **Pytest-HTML** | Latest | HTML test reports |

---

##  Project Structure

```
api-testing-automation/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── pytest.ini                         # Pytest configuration
├── conftest.py                        # Pytest fixtures and configuration
├── config/                            # Configuration files
│   ├── __init__.py
│   ├── config.py                      # Base configuration
│   ├── dev.env                        # Development environment
│   ├── staging.env                    # Staging environment
│   └── prod.env                       # Production environment
├── api/                               # API client classes
│   ├── __init__.py
│   ├── base_api_client.py             # Base API client with common methods
│   ├── user_api.py                    # User API endpoints
│   ├── post_api.py                    # Post API endpoints
│   └── comment_api.py                 # Comment API endpoints
├── tests/                             # Test files
│   ├── __init__.py
│   ├── test_users_api.py              # User endpoint tests
│   ├── test_posts_api.py              # Post endpoint tests
│   ├── test_comments_api.py           # Comment endpoint tests
│   └── test_data_driven.py            # Data-driven test examples
├── fixtures/                          # Test data
│   ├── user_data.json                 # User test data
│   ├── post_data.json                 # Post test data
│   └── test_scenarios.json            # Scenario-based test data
└── reports/                           # Test execution reports (generated)
    └── index.html                     # HTML test report
```

---

##  Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ayoub-DataScientist/api-testing-automation.git
   cd api-testing-automation
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp config/dev.env .env
   ```

---

##  Running Tests

### Run all tests
```bash
pytest tests/
```

### Run tests with verbose output
```bash
pytest tests/ -v
```

### Run specific test file
```bash
pytest tests/test_users_api.py
```

### Run tests and generate HTML report
```bash
pytest tests/ --html=reports/index.html --self-contained-html
```

### Run tests with specific marker
```bash
pytest tests/ -m "smoke"
```

### Run data-driven tests
```bash
pytest tests/test_data_driven.py -v
```

---

##  Configuration Management

### Environment Variables

The project supports multiple environments (dev, staging, prod). Configure via `.env` file:

```env
BASE_URL=https://jsonplaceholder.typicode.com
TIMEOUT=5
VERIFY_SSL=true
LOG_LEVEL=INFO
```

### Using Different Environments

```bash
# Development
pytest tests/ --env=dev

# Staging
pytest tests/ --env=staging

# Production
pytest tests/ --env=prod
```

---

##  API Client Classes

The project uses API client classes to abstract HTTP operations and improve maintainability.

### Example: User API Client

```python
# api/user_api.py
from api.base_api_client import BaseAPIClient

class UserAPI(BaseAPIClient):
    """Client for User API endpoints."""
    
    def get_user(self, user_id: int):
        """Get a user by ID."""
        return self.get(f"/users/{user_id}")
    
    def create_user(self, user_data: dict):
        """Create a new user."""
        return self.post("/users", json=user_data)
    
    def update_user(self, user_id: int, user_data: dict):
        """Update an existing user."""
        return self.put(f"/users/{user_id}", json=user_data)
    
    def delete_user(self, user_id: int):
        """Delete a user."""
        return self.delete(f"/users/{user_id}")
```

### Example: Using the API Client in Tests

```python
# tests/test_users_api.py
def test_get_user(user_api):
    """Test retrieving a user."""
    response = user_api.get_user(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
```

---

##  Test Examples

### Positive Test Example

```python
def test_create_user_success(user_api):
    """Test successful user creation."""
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "username": "johndoe"
    }
    response = user_api.create_user(user_data)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
```

### Negative Test Example

```python
def test_get_nonexistent_user(user_api):
    """Test retrieving a non-existent user."""
    response = user_api.get_user(99999)
    assert response.status_code == 404
```

### Data-Driven Test Example

```python
@pytest.mark.parametrize("user_id,expected_status", [
    (1, 200),
    (2, 200),
    (99999, 404),
    (0, 404),
])
def test_get_user_data_driven(user_api, user_id, expected_status):
    """Test user retrieval with multiple data sets."""
    response = user_api.get_user(user_id)
    assert response.status_code == expected_status
```

---

##  Test Reporting

Tests generate HTML reports for easy review:

```bash
pytest tests/ --html=reports/index.html --self-contained-html
```

The report includes:
- Test execution summary
- Pass/fail status for each test
- Execution time
- Error details and response payloads

---

##  Key Learnings

This project demonstrates:
1. **API Client Abstraction:** Creating reusable API client classes
2. **Environment Configuration:** Managing different environments
3. **Data-Driven Testing:** Using Pytest parametrize for multiple scenarios
4. **Positive & Negative Tests:** Comprehensive test coverage
5. **Professional Practices:** Clean code, documentation, and reporting

---

##  Related Repositories

- [qa-portfolio-overview](https://github.com/Ayoub-DataScientist/qa-portfolio-overview) - Portfolio map and overview
- [web-ui-testing-playwright](https://github.com/Ayoub-DataScientist/web-ui-testing-playwright) - UI testing examples
- [test-automation-framework-from-scratch](https://github.com/Ayoub-DataScientist/test-automation-framework-from-scratch) - Advanced framework

---

##  License

This project is open source and available under the MIT License.
