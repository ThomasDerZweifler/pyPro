CREATE DATABASE IF NOT EXISTS mock;
DROP TABLE IF EXISTS endpoints;
CREATE TABLE endpoints (
    EP_id int primary key auto_increment,
    EP_timestamp timestamp,
    EP_description varchar(255),
    EP_flavor varchar(255),
    EP_method varchar(255),
    EP_path varchar(255) unique,
    EP_json blob
);
INSERT INTO endpoints (
	EP_timestamp,EP_description,EP_flavor,EP_method,EP_path,EP_json)
    VALUES (now(),'a description','a flavor', 'GET', 'path_two',
    '{result: {"key1":"value1"}{"key2":"value2"}}');
    