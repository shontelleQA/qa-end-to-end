
-- TC01: Confirm valid submission stored
SELECT 
    *
FROM 
    submissions
WHERE 
    full_name = 'Nicole Nealy';


-- TC02: Check for missing phone number
SELECT 
    full_name, 
    phone
FROM 
    submissions
WHERE 
    email = 'chrisb@example.com';


-- TC03: Submissions with missing or blank email
SELECT 
    *
FROM 
    submissions
WHERE 
    email IS NULL 
    OR email = '';


-- TC04: Join to get service type name
SELECT 
    s.full_name, 
    s.email, 
    st.name AS service_type
FROM 
    submissions s
JOIN 
    service_types st 
    ON s.service_id = st.id;


-- TC05: Count of submissions per service type
SELECT 
    st.name AS service_type, 
    COUNT(*) AS total_submissions
FROM 
    submissions s
JOIN 
    service_types st 
    ON s.service_id = st.id
GROUP BY 
    st.name;
