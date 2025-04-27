import requests

# === Base setup ===
base_url = "https://gorest.co.in/public/v2"
# <- real token here
token = "c9af22406a462900443e2ea4f29fd1dd35a09359559c7c51e11d0cc8fcb54687"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# === Test function ===


def test_create_user():
    payload = {
        "name": "Automated User",
        "gender": "female",
        "email": "automateduser123@example.com",
        "status": "active"
    }
    response = requests.post(
        f"{base_url}/users", headers=headers, json=payload)

    # Print for easy debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")

    # Assertions
    assert response.status_code == 201, f"Expected 201 Created, got {response.status_code}"
    response_body = response.json()
    assert response_body["name"] == "Automated User", "Name mismatch"
    assert response_body["email"] == "automateduser123@example.com", "Email mismatch"


# === Manual run trigger ===
if __name__ == "__main__":
    test_create_user()
    print("✅ Create User Test Completed Successfully.")
