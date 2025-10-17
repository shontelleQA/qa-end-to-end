import requests

# === Base setup ===
base_url = "https://gorest.co.in/public/v2"
token = "c9af22406a462900443e2ea4f29fd1dd35a09359559c7c51e11d0cc8fcb54687"  # Your real token
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# === Test function ===


def test_create_user_missing_email():
    payload = {
        "name": "Negative Test User",
        "gender": "female",
        # "email" is intentionally missing to trigger validation error
        "status": "active"
    }
    response = requests.post(
        f"{base_url}/users", headers=headers, json=payload)

    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

    # Assertions
    assert response.status_code == 422, f"Expected 422 Validation Error, got {response.status_code}"
    response_body = response.json()
    assert any("email" in error.get("field", "")
               for error in response_body), "No email error in response"


# === Manual run trigger ===
if __name__ == "__main__":
    test_create_user_missing_email()
    print("✅ Negative Create User Test Completed Successfully.")
    # Note: This test is expected to fail if the API does not handle the missing email case correctly.
    # Make sure to check the API documentation for the expected behavior.
    # If the test fails, it indicates that the API is not validating the email field as expected.
