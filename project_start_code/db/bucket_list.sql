DROP TABLE IF EXISTS bucketlists;
DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE destinations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id)
);

CREATE TABLE bucketlists(
    id SERIAL PRIMARY KEY,
    destination_id INT REFERENCES destinations(id)
)
