class UserAuthentication:
    """Encapsulates user authentication logic"""

    def __init__(self):
        self.__users = {}  # Private - stores user data
        self.__logged_in = None
        self.__max_login_attempts = 3

    def register(self, username, password):
        """Public method - handles registration"""
        if username in self.__users:
            return False, "Username already exists"
        if len(password) < 6:
            return False, "Password too short"

        # Encapsulated - password hashing hidden
        self.__users[username] = {
            "password": self.__hash_password(password),
            "attempts": 0,
            "locked": False
        }
        return True, "Registration successful"

    def login(self, username, password):
        """Public method - handles login with security checks"""
        if username not in self.__users:
            return False, "User not found"

        user = self.__users[username]

        # Encapsulated security logic
        if user["locked"]:
            return False, "Account locked. Contact support."

        if user["attempts"] >= self.__max_login_attempts:
            user["locked"] = True
            return False, "Too many failed attempts. Account locked."

        if self.__verify_password(password, user["password"]):
            user["attempts"] = 0
            self.__logged_in = username
            return True, f"Welcome, {username}!"
        else:
            user["attempts"] += 1
            remaining = self.__max_login_attempts - user["attempts"]
            return False, f"Invalid password. {remaining} attempts remaining"

    def logout(self):
        """Public method - logout"""
        if self.__logged_in:
            username = self.__logged_in
            self.__logged_in = None
            return f"Goodbye, {username}!"
        return "No user logged in"

    # PRIVATE METHODS - Implementation details hidden
    def __hash_password(self, password):
        """Simulate password hashing"""
        return "".join(chr(ord(c) + 1) for c in password)

    def __verify_password(self, password, hashed):
        """Simulate password verification"""
        return self.__hash_password(password) == hashed


# Usage
auth = UserAuthentication()

# Public interface is simple
print(auth.register("alice", "secret123"))  # (True, 'Registration successful')
print(auth.login("alice", "wrong"))  # (False, 'Invalid password...')
print(auth.login("alice", "secret123"))  # (True, 'Welcome, alice!')
print(auth.logout())  # Goodbye, alice!

# ❌ Can't access internal data directly
# print(auth.__users)  # AttributeError
# print(auth.__hash_password("test"))  # AttributeError