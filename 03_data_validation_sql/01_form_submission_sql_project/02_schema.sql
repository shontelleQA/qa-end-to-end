
-- Service Types table
CREATE TABLE service_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Submissions table with a foreign key to service_types
CREATE TABLE submissions (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    service_id INTEGER NOT NULL,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES service_types(id)
);
