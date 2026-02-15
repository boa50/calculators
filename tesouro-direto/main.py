from datetime import date

one_year_weekdays = 252

dt_vencimento_2045 = date(2045, 5, 15)
dt_vencimento_2065 = date(2065, 5, 15)


def get_total_weekdays(d0: date, d1: date):
    dt_delta = d1 - d0
    dt_delta_days = dt_delta.days - 1

    n_full_years = int(dt_delta_days / 365)
    n_weekdays_full_years = (
        n_full_years * one_year_weekdays
    )  # just weekdays without holidays
    n_remaining_days = dt_delta_days % 365
    n_remaining_weekdays = (int(n_remaining_days / 7) * 5) + (n_remaining_days % 7)
    n_total_weekdays = n_weekdays_full_years + n_remaining_weekdays

    return n_total_weekdays


def get_total_interest_rate_multiplier(annual_interest_rate: float, d0: date, d1: date):
    n_total_weekdays = get_total_weekdays(d0, d1)

    total_interest_rate_multiplier = (1 + (annual_interest_rate / 100)) ** (
        n_total_weekdays / one_year_weekdays
    )

    return total_interest_rate_multiplier


def get_updated_value(
    value_bought: float, dt_bought: date, dt_today: date, IPCA: float = 5.85
):
    ipca_period = get_total_interest_rate_multiplier(
        annual_interest_rate=IPCA, d0=dt_bought, d1=dt_today
    )

    updated_value = value_bought * ipca_period

    return updated_value


def calculate_final_value(
    value,
    hired_interest_rate,
    selling_interest_rate,
    d0: date,
    d1: date,
    value_bought_previously=None,
):
    if value_bought_previously is None:
        value_bought_previously = value

    final_value = value * hired_interest_rate / selling_interest_rate
    final_value_after_taxes = final_value

    profit = final_value - value_bought_previously

    if profit > 0:
        taxes = profit * get_taxes_percentage(d0, d1)
        final_value_after_taxes -= taxes

    return final_value, final_value_after_taxes


def get_taxes_percentage(d0: date, d1: date):
    dt_delta = d1 - d0
    dt_delta_days = dt_delta.days - 1

    if dt_delta_days <= 180:
        return 0.225
    elif dt_delta_days <= 360:
        return 0.20
    elif dt_delta_days <= 720:
        return 0.175
    else:
        return 0.15


# Current value into future
# IPCA + 2045
dt_extracao_dados = date(2026, 2, 14)

sellings = [
    {
        "dt_compra": date(2019, 11, 21),
        "valor_compra": 4501.25,
        "taxa_contratada": 3.23,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2019, 12, 4),
        "valor_compra": 3360.57,
        "taxa_contratada": 3.36,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2019, 12, 19),
        "valor_compra": 4240.60,
        "taxa_contratada": 3.47,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 1, 21),
        "valor_compra": 6991.92,
        "taxa_contratada": 3.50,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 3, 20),
        "valor_compra": 4997.13,
        "taxa_contratada": 4.61,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 3, 24),
        "valor_compra": 4991.89,
        "taxa_contratada": 4.80,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 4, 22),
        "valor_compra": 3390.93,
        "taxa_contratada": 4.08,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 4, 27),
        "valor_compra": 19995.21,
        "taxa_contratada": 4.67,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 5, 20),
        "valor_compra": 1989.16,
        "taxa_contratada": 4.42,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 6, 22),
        "valor_compra": 6997.38,
        "taxa_contratada": 4.12,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 7, 28),
        "valor_compra": 1317.60,
        "taxa_contratada": 3.53,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 9, 21),
        "valor_compra": 5283.17,
        "taxa_contratada": 4.12,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 10, 20),
        "valor_compra": 3192.00,
        "taxa_contratada": 4.01,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 11, 20),
        "valor_compra": 3821.13,
        "taxa_contratada": 4.17,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2020, 12, 18),
        "valor_compra": 5932.68,
        "taxa_contratada": 3.51,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2021, 1, 22),
        "valor_compra": 8995.21,
        "taxa_contratada": 3.78,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2021, 3, 23),
        "valor_compra": 4996.74,
        "taxa_contratada": 4.06,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2021, 4, 22),
        "valor_compra": 2495.57,
        "taxa_contratada": 4.17,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
    {
        "dt_compra": date(2021, 12, 17),
        "valor_compra": 2499.24,
        "taxa_contratada": 5.19,
        "taxa_contratada_total": None,
        "value_updated": None,
    },
]


taxa_atual_2045 = 7.15
valor_updated_venda_hoje = 0
items_total_value = 0

taxa_venda_2045 = get_total_interest_rate_multiplier(
    annual_interest_rate=taxa_atual_2045,
    d0=dt_extracao_dados,
    d1=dt_vencimento_2045,
)

for item in sellings:
    ### Bringing to actual value
    item["value_updated"] = get_updated_value(
        item["valor_compra"], item["dt_compra"], dt_extracao_dados
    )
    item["taxa_contratada_total"] = get_total_interest_rate_multiplier(
        annual_interest_rate=item["taxa_contratada"],
        d0=item["dt_compra"],
        d1=dt_vencimento_2045,
    )

    total_value, valor_updated_venda_hoje_pos_taxas = calculate_final_value(
        value=item["value_updated"],
        hired_interest_rate=item["taxa_contratada_total"],
        selling_interest_rate=taxa_venda_2045,
        d0=item["dt_compra"],
        d1=dt_extracao_dados,
        value_bought_previously=item["valor_compra"],
    )

    valor_updated_venda_hoje += valor_updated_venda_hoje_pos_taxas


### Selling beforehand
dt_venda = date(2028, 6, 1)
taxa_venda_futura = 5.5


taxa_venda_total_pos = get_total_interest_rate_multiplier(
    annual_interest_rate=taxa_venda_futura, d0=dt_venda, d1=dt_vencimento_2045
)

print()
for item in sellings:
    valor_venda_atual, valor_venda_atual_pos_taxas = calculate_final_value(
        value=item["value_updated"],
        hired_interest_rate=item["taxa_contratada_total"],
        selling_interest_rate=taxa_venda_total_pos,
        d0=item["dt_compra"],
        d1=dt_venda,
        value_bought_previously=item["valor_compra"],
    )

    items_total_value += valor_venda_atual

    # print(
    #     f"Selling with {taxa_venda_futura} interest rate at the time: {valor_venda_atual:.2f} and pos taxes {valor_venda_atual_pos_taxas:.2f}"
    # )

print(f"Items total value: {items_total_value:.2f}")


taxa_2065 = 6.97
taxa_total_2065 = get_total_interest_rate_multiplier(
    annual_interest_rate=taxa_2065, d0=dt_extracao_dados, d1=dt_vencimento_2065
)
taxa_venda_total_2065 = get_total_interest_rate_multiplier(
    annual_interest_rate=taxa_venda_futura, d0=dt_venda, d1=dt_vencimento_2065
)
valor_venda_longo, valor_venda_longo_pos_taxas = calculate_final_value(
    value=valor_updated_venda_hoje,
    hired_interest_rate=taxa_total_2065,
    selling_interest_rate=taxa_venda_total_2065,
    d0=dt_extracao_dados,
    d1=dt_venda,
)
print()
print(f"Money to invest today: {valor_updated_venda_hoje:.2f}")
print(
    f"Selling the long term with {taxa_venda_futura} interest rate at the time: {valor_venda_longo:.2f} and pos taxes {valor_venda_longo_pos_taxas:.2f}"
)
print(
    f"Real profit: {(valor_venda_longo_pos_taxas - items_total_value):.2f} ({((valor_venda_longo_pos_taxas / items_total_value) - 1) * 100:.2f}%)"
)
