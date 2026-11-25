# BankGuard — Kelompok 9

Prototype akademik pemantauan transaksi tidak wajar dan peringatan dini. Target: satu template Ubuntu Server pada VirtualBox, tiga full clone aktif, akses browser dari perangkat lain. Flask/Jinja, SQLite lokal per VM, Gunicorn Linux. SQLite lokal menggantikan Firestore terpusat untuk demo; Flask menggantikan Cloud Functions. Data fiktif, bukan bukti fraud.

## Scoring
Tujuan baru +40; nominal >3 kali rata-rata +35; frekuensi >3 dalam 10 menit +25. RENDAH 0–39, SEDANG 40–59, TINGGI 60–100. Contoh 10 juta / rata-rata 500 ribu / tujuan baru / frekuensi 1 = 75 TINGGI.

## Mulai
Baca [kolaborasi](CONTRIBUTING.md), [kontrak](docs/contracts.md), pilih branch peran dan Issue. Python 3.12: `python -m venv .venv`, aktifkan venv, `python -m pip install -r requirements.txt`. Setelah modul selesai: `python -m flask --app bankguard.app:create_app run --port 8000`, `python -m pytest`. Saat ini masih scaffold, belum runnable.

| Peran | Branch | Panduan |
|---|---|---|
| Ketua dan integrasi | `integration/leader` | [Panduan](docs/roles/leader.md) |
| Infrastruktur Ubuntu | `infra/setup` | [Panduan](docs/roles/setup.md) |
| Template dan cloning | `infra/cloning` | [Panduan](docs/roles/cloning.md) |
| Backend Flask | `feature/backend` | [Panduan](docs/roles/backend.md) |
| Frontend dashboard | `feature/frontend` | [Panduan](docs/roles/frontend.md) |
| Database SQLite | `feature/database` | [Panduan](docs/roles/database.md) |
| Quality assurance | `test/quality-assurance` | [Panduan](docs/roles/qa.md) |
| Akses browser dan jaringan | `infra/network` | [Panduan](docs/roles/network.md) |
| Dokumentasi dan presentasi | `docs/presentation` | [Panduan](docs/roles/documentation.md) |

## Demo
Host localhost:8081, :8082, :8083 menuju guest 8000; URL belum aktif. [Checklist](docs/demo-checklist.md). Jangan commit kredensial, data pribadi, file VM. Matikan VM setelah demo.
