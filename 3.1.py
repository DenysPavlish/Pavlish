amount_uah = 25000
interest_rate_uah = 11.5 / 100
interest_rate_usd = 4 / 100
buy_rate = 27
sell_rate = 28.6

final_uah = amount_uah * (1 + interest_rate_uah)
amount_usd = amount_uah / buy_rate
final_usd = amount_usd * (1 + interest_rate_usd)
final_uah_from_usd = final_usd * sell_rate

if final_uah > final_uah_from_usd:
    print("Вклад у гривнях буде вигідніший.")
else:
    print("Вклад у доларах буде вигідніший.")
