import time
from collections import defaultdict

class RateLimiters:
    def __init__(self, limit=5, window=60):
        self.limit = limit         # Max requests per window
        self.window = window       # Window size in seconds
        self.users = defaultdict(lambda: {"count": 0, "start_time": time.time()})

    def is_allowed(self, user_id):
        current_time = time.time()
        user_data = self.users[user_id]

        # If window has passed, reset
        if current_time - user_data["start_time"] > self.window:
            user_data["count"] = 0
            user_data["start_time"] = current_time

        if user_data["count"] < self.limit:
            user_data["count"] += 1
            return True
        return False

    def remaining_requests(self, user_id):
        user_data = self.users[user_id]
        elapsed = time.time() - user_data["start_time"]
        if elapsed > self.window:
            return self.limit
        return self.limit - user_data["count"]


# TESTING FUNCTION #

rate_limiter = RateLimiters(limit=5, window=60)

test_users = ["user1", "user2"]

# Simulate rapid requests
for i in range(7):
    for user in test_users:
        allowed = rate_limiter.is_allowed(user)
        remaining = rate_limiter.remaining_requests(user)
        print(f"User {user}, Request {i+1}: {'Allowed' if allowed else 'Blocked'}, Remaining: {remaining}")
    time.sleep(0.5)  # simulate half-second between requests

# Wait 60 seconds to test auto-reset
print("\nWaiting for 60 seconds to reset window...\n")
time.sleep(60)

for user in test_users:
    allowed = rate_limiter.is_allowed(user)
    remaining = rate_limiter.remaining_requests(user)
    print(f"User {user},Window after reset: {'Allowed' if allowed else 'Blocked'}, Remaining: {remaining}")
