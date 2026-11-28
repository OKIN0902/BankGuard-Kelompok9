# ERD SQLite (satu tabel)
Sesuai kontrak v0.2; tiap VM menyimpan data terpisah.

```mermaid
erDiagram
    transactions {
        TEXT id PK
        TEXT user_id
        INTEGER amount
        INTEGER historical_average
        INTEGER destination_new
        INTEGER transfers_10min
        INTEGER score
        TEXT level
        TEXT reasons
        TEXT created_at
    }
```

UUID dibuat backend; waktu UTC ISO; reasons JSON array; destination_new 0/1 di SQLite dan boolean pada API. Tidak ada tabel akun/foreign key. Lihat backend/schema.sql. Tidak ada integrasi bank atau database terpusat.
