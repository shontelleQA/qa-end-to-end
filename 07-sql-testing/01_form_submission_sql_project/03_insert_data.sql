
-- Insert service types
INSERT INTO service_types (id, name) VALUES
(1, 'Support'),
(2, 'Billing'),
(3, 'Technical');

-- Insert dummy submissions
INSERT INTO submissions (id, full_name, email, phone, service_id, message, created_at) VALUES
(1, 'Nicole Nealy', 'nicole@example.com', '555-1234', 1, 'Need help with account login.', '2025-05-01 10:15:00'),
(2, 'Chris Bailey', 'chrisb@example.com', NULL, 2, 'Question about recent billing error.', '2025-05-02 12:30:00'),
(3, 'Dana Smith', 'dana.smith@example.com', '555-8765', 3, 'App keeps crashing during upload.', '2025-05-03 14:45:00'),
(4, 'Riley Johnson', 'rileyj@example.com', '', 1, 'Unable to reset password.', '2025-05-04 09:20:00'),
(5, 'Alex Morgan', 'alex.morgan@example.com', NULL, 2, 'Invoice not showing in dashboard.', '2025-05-05 11:10:00');
