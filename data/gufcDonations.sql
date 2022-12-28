CREATE TABLE gufcDonations(
    id INT PRIMARY KEY NOT NULL,
    d_created TIMESTAMP NOT NULL,
    amount DECIMAL(18, 2) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(13),
    zip_code VARCHAR(5) NOT NULL
);
