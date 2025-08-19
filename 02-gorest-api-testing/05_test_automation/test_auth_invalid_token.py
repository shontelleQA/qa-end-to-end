import requests

# === Base setup ===
base_url = "https://gorest.co.in/public/v2"
# Intentionally using an invalid token
invalid_token = "invalid_token_here"
headers = {
    "Authorization": f"Bearer {invalid_token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# === Test function ===


def test_create_user_invalid_token():
    payload = {
        "name": "Unauthorized User",
        "gender": "female",
        "email": "unauthorizeduser123@example.com",
        "status": "active"
    }
    response = requests.post(
        f"{base_url}/users", headers=headers, json=payload)

    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

    # Parse response correctly
    response_body = response.json()

    # Assertions
    assert response.status_code == 401, f"Expected 401 Unauthorized, got {response.status_code}"
    assert "message" in response_body, "Missing 'message' in error response"
    assert response_body[
        "message"] == "Invalid token", f"Unexpected error message: {response_body['message']}"


# === Manual run trigger ===
if __name__ == "__main__":
    test_create_user_invalid_token()
    print("✅ Invalid Token Test Completed Successfully.")
