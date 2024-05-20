CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    word TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO categories (name) VALUES
    ("Базовый_набор"),
    ("IT"),
    ("Юриспруденция"),
    ("Новый_год"),
    ("Marvel"),
    ("Природа"),
    ("Еда"),
    ("Фильмы");



INSERT INTO words (category_id, word) VALUES
    (1, "fdsf"), (1, "dsfdsf"), (1, "dsfsdf"), (1, "dddsfdsf"), (1, "wewqewq"), (1, "ewqefds"), (1, "gdfgfdg"), (1, "gdfgdfg"), (1, "gfdgfdg"), (1, "fdgfdgfdg"),
    (2, "gfdgdfgdfg"), (2, "fgdbvcbvc"), (2, "ghfgjhgf"), (2, "jghyjyt"), (2, "nbvnvb"), (2, "serewr"), (2, "kuyk"), (2, "bvcbvc"), (2, "tttt"), (2, "jjjjjjj"),
    (3, "fdgqwe"), (3, "qwert"), (3, "hjklii"), (3, "vcbvcbvc"), (3, "luiloiu"), (3, "zxczxc"), (3, "dfdsfdsfsdf"), (3, "dfffffffffffff"), (3, "dyyyyyyyyyy"), (3, "rrrrrrrrrrrrrrd"),
    (4, "d"), (4, "d"), (4, "d"), (4, "d"), (4, "d"), (4, "d"), (4, "d"), (4, "d"), (4, "d"), (4, "d"),
    (5, "d"), (5, "d"), (5, "d"), (5, "d"), (5, "d"), (5, "d"), (5, "d"), (5, "d"), (5, "d"), (5, "d"),
    (6, "d"), (6, "d"), (6, "d"), (6, "d"), (6, "d"), (6, "d"), (6, "d"), (6, "d"), (6, "d"), (6, "d"),
    (7, "d"), (7, "d"), (7, "d"), (7, "d"), (7, "d"), (7, "d"), (7, "d"), (7, "d"), (7, "d"), (7, "d"),
    (8, "d"), (8, "d"), (8, "d"), (8, "d"), (8, "d"), (8, "d"), (8, "d"), (8, "d"), (8, "d"), (8, "d");

