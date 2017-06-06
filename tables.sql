CREATE TABLE items (
    id serial primary key,
    author_id int references user,
    body text,
    created timestamp
);