CREATE TABLE gufcEvents(
    id SERIAL PRIMARY KEY NOT NULL,
    created TIMESTAMP NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    title VARCHAR(255) NOT NULL,
    descript VARCHAR(500) NOT NULL,
    cost DECIMAL(18, 2) NOT NULL,
    physical_addr VARCHAR(255) NOT NULL,
);