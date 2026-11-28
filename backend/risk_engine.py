"""Aturan risiko fiktif; bukan penentu penipuan."""
def _integer(name, value, upper):
    if type(value) is not int or not 1 <= value <= upper:
        raise ValueError(f"{name} harus bilangan bulat 1–{upper}.")
    return value


def score_transaction(amount, historical_average, destination_new, transfers_10min):
    _integer("Nominal transfer", amount, 10**12)
    _integer("Rata-rata historis", historical_average, 10**12)
    _integer("Frekuensi transfer", transfers_10min, 10**6)
    if type(destination_new) is not bool:
        raise ValueError("Status tujuan baru harus berupa boolean.")
    score, reasons = 0, []
    if destination_new:
        score += 40
        reasons.append("Rekening tujuan baru")
    if amount > historical_average * 3:
        score += 35
        reasons.append("Nominal tidak biasa")
    if transfers_10min > 3:
        score += 25
        reasons.append("Frekuensi tinggi")
    return {
        "score": score,
        "level": "TINGGI" if score >= 60 else "SEDANG" if score >= 40 else "RENDAH",
        "reasons": reasons,
    }
