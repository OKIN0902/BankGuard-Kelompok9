# Cara bekerja bersama di GitHub (untuk pemula)

## Arti istilah
| Istilah | Artinya |
|---|---|
| Repository | Folder proyek bersama di GitHub |
| Clone repository | Mengunduh salinan proyek ke laptop; berbeda dari clone VM |
| Branch | Ruang kerja sendiri tanpa mengubah kode utama |
| Commit | Menyimpan catatan perubahan di laptop |
| Push | Mengirim commit ke GitHub |
| Fetch/Pull | Memeriksa/mengambil perubahan terbaru |
| Pull Request (PR) | Permintaan agar hasil kerja diperiksa dan digabungkan |
| Merge | Menggabungkan perubahan yang sudah diperiksa |
| Issue | Catatan tugas yang harus dikerjakan |

## Pertama kali
1. Terima undangan repository menggunakan akun sendiri. Instal [GitHub Desktop](https://desktop.github.com/) dan [VS Code](https://code.visualstudio.com/). Tim kode dan pengujian juga instal Python 3.12. Tidak semua perlu VM.
2. GitHub Desktop → File → Clone repository → pilih BankGuard-Kelompok9. Tentukan folder penyimpanan, klik Clone.
3. Repository → Open in Visual Studio Code. Pilih Current branch sesuai tugas yang sudah dibuat; tidak perlu New branch.
4. Baca Issue dan panduan tugas. Latihan awal: buat `docs/members/<role>.md` berisi peran, tugas dan status (jangan isi nama pribadi saat repo Public).

## Setiap mulai bekerja
1. Simpan/commit pekerjaan sebelumnya. Pindah ke main, klik Fetch origin dan Pull origin bila tersedia.
2. Kembali ke branch sendiri. Branch → Merge into current branch → pilih main untuk membawa perubahan terbaru. Jika ada konflik, koordinasikan dengan ketua; jangan menimpa kode teman.
3. Edit hanya file tanggung jawab sendiri, simpan dan uji.
4. GitHub Desktop → Changes → periksa perubahan → isi Summary → Commit to branch sendiri → Push origin.
5. Buat Pull Request: base main, compare branch sendiri. Tulis apa yang berubah, Issue terkait dan hasil uji sebenarnya. Ketua memeriksa Files changed, menguji, lalu merge. Jangan hapus branch yang masih dipakai.

## Aturan
Jangan push langsung ke main. Jangan unggah data nyata, rahasia, ISO/VDI dan video besar. Simpan bukti sensitif terpisah. Jika belum diuji, tulis belum diuji. Urutan kerja: sepakati panduan teknis → database/scoring → backend/frontend → pengujian → template → clone → jaringan → demo. Tim infrastruktur boleh mulai paralel.
