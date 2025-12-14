CREATE_POKEMON_TABLE = '''CREATE TABLE IF NOT EXISTS pokemon (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    number INTEGER NOT NULL,
                                    type1 TEXT NOT NULL,
                                    type2 TEXT,
                                    ability1 TEXT NOT NULL,
                                    ability2 TEXT,
                                    hidden_ability TEXT
                                )'''


CREATE_STATS_TABLE = '''CREATE TABLE IF NOT EXISTS stats( 
                            number INTEGER PRIMARY KEY,
                            hp INTEGER,
                            atk INTEGER,
                            def INTEGER,
                            spatk INTEGER,
                            spdef INTEGER,
                            speed INTEGER,
                            FOREIGN KEY(number) REFERENCES pokemon(number)
                            )'''

POPULATE_STATS = '''INSERT OR IGNORE INTO stats (number)
                              SELECT number FROM pokemon'''

UPDATE_STATS = '''UPDATE stats 
                  SET hp = ?, atk = ?, def = ?, spatk = ?, spdef = ?, speed = ? 
                  WHERE number = ?'''

ADD_POKEMON = '''INSERT INTO pokemon (name, number, type1, type2, ability1, ability2, hidden_ability)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''

GET_STATUS = '''SELECT COUNT(*) FROM pokemon WHERE name = ? OR number = ?'''

GET_POKEMON = '''SELECT p.name, p.number, p.type1, p.type2, p.ability1, p.ability2, p.hidden_ability,
                 s.hp, s.atk, s.def, s.spatk, s.spdef, s.speed
                 FROM pokemon p
                 LEFT JOIN stats s ON p.number = s.number
                 WHERE p.name = ? OR p.number = ?'''

__all__ = [
            'CREATE_POKEMON_TABLE', 'CREATE_STATS_TABLE', 'POPULATE_STATS'
            ,'UPDATE_STATS', 'ADD_POKEMON', 'GET_STATUS', 'GET_POKEMON'
          ]