CREATE TABLE IF NOT EXISTS transactions (
    id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL CHECK(length(user_id) BETWEEN 1 AND 64),
    amount INTEGER NOT NULL CHECK(amount BETWEEN 1 AND 1000000000000),
    historical_average INTEGER NOT NULL CHECK(historical_average BETWEEN 1 AND 1000000000000),
    destination_new INTEGER NOT NULL CHECK(destination_new IN (0, 1)),
    transfers_10min INTEGER NOT NULL CHECK(transfers_10min BETWEEN 1 AND 1000000),
    score INTEGER NOT NULL CHECK(score IN (0,25,35,40,60,65,75,100)),
    level TEXT NOT NULL CHECK(level IN ('RENDAH','SEDANG','TINGGI')),
    reasons TEXT NOT NULL CHECK(json_valid(reasons) AND json_type(reasons) = 'array'),
    created_at TEXT NOT NULL,
    CHECK(level = CASE WHEN score >= 60 THEN 'TINGGI' WHEN score >= 40 THEN 'SEDANG' ELSE 'RENDAH' END)
) STRICT;
CREATE INDEX IF NOT EXISTS idx_transactions_created ON transactions(created_at DESC, id DESC);
CREATE INDEX IF NOT EXISTS idx_transactions_user ON transactions(user_id);
