import requests

# Define the base URL for the JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"


# User authentication
def authenticate_user(username, password):
    login_data = {
        "username": username,
        "password": password
    }

    response = requests.post(f"{BASE_URL}/auth", json=login_data)

    # Check if the authentication was successful
    if response.status_code == 200:
        print("User authentication successful")
    else:
        print(f"User authentication failed. Status Code: {response.status_code}")


# Retrieve product details
def get_product_details(product_id):
    # response = requests.get(f"{BASE_URL}/products/{product_id}")
    response = requests.get(f"{BASE_URL}/users/1/todos")

    # Check if the product details were retrieved successfully
    if response.status_code == 200:
        product_data = response.json()
        print("Product Details:", product_data)
    else:
        print(f"Failed to retrieve product details. Status Code: {response.status_code}")


# Manipulate the shopping cart (add/remove items)
def manipulate_cart(user_id, product_id, action):
    cart_data = {
        "user_id": user_id,
        "product_id": product_id,
        "action": action  # "add" or "remove"
    }

    response = requests.post(f"{BASE_URL}/cart", json=cart_data)

    # Check if the cart manipulation was successful
    if response.status_code == 200:
        print("Cart manipulation successful")
    else:
        print(f"Cart manipulation failed. Status Code: {response.status_code}")


# Place an order
def place_order(user_id, product_id, quantity):
    order_data = {
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity
    }

    response = requests.post(f"{BASE_URL}/orders", json=order_data)

    # Check if the order placement was successful
    if response.status_code == 201:
        print("Order placed successfully")
    else:
        print(f"Failed to place the order. Status Code: {response.status_code}")


# Main test script
if __name__ == "__main__":
    # Test user authentication
    authenticate_user("testuser", "testpassword")

    # Test product retrieval and details
    get_product_details(1)

    # Test cart manipulation (add item)
    manipulate_cart(user_id=1, product_id=2, action="add")

    # Test cart manipulation (remove item)
    manipulate_cart(user_id=1, product_id=2, action="remove")

    # Test order placement
    place_order(user_id=1, product_id=3, quantity=2)
    