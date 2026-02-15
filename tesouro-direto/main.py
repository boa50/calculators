from datetime import date

one_year_weekdays = 252


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


def get_total_interest_rate_multiplier(
    annual_interest_rate: float, n_total_weekdays: int
):
    taxa_contratada_total = (1 + (annual_interest_rate / 100)) ** (
        n_total_weekdays / one_year_weekdays
    )

    return taxa_contratada_total


# Current value into future
# IPCA + 2045
dt_extracao_dados = date(2026, 2, 14)
dt_compra = date(2019, 11, 21)
dt_vencimento = date(2045, 5, 15)

valor_bruto = 3822.34
# valor_liquido = 3810.79  # valor_bruto - taxa_b3 - IR
taxa_b3 = 11.55

# quantidade_compra = 3.11
# preco_compra = 1447.35
valor_compra = 4501.25  # quatidade_compra * preco_compra
# IPCA = 0
IPCA = 5.85

taxa_contratada = 3.23  # + IPCA
taxa_atual = 7.15  # + IPCA

### Bringing to actual value

n_total_weekdays_expiry = get_total_weekdays(dt_compra, dt_vencimento)

taxa_contratada_total = get_total_interest_rate_multiplier(
    taxa_contratada, n_total_weekdays_expiry
)

valor_final_esperado = valor_compra * taxa_contratada_total

# print(valor_final_esperado)


n_total_weekdays = get_total_weekdays(dt_extracao_dados, dt_vencimento)

taxa_venda = taxa_atual  # + IPCA
taxa_venda_total = get_total_interest_rate_multiplier(taxa_venda, n_total_weekdays)

valor_final_esperado2 = valor_bruto * taxa_venda_total


n_total_weekdays_update_bought = get_total_weekdays(dt_compra, dt_extracao_dados)
taxa_update_total = get_total_interest_rate_multiplier(
    IPCA, n_total_weekdays_update_bought
)

valor_updated = valor_compra * taxa_update_total
valor_updated_venda_hoje = valor_updated * taxa_contratada_total / taxa_venda_total

print(valor_updated, valor_updated_venda_hoje)
print(
    valor_updated * taxa_contratada_total, valor_updated_venda_hoje * taxa_venda_total
)


### Selling in 2 years
dt_venda = date(2026, 5, 15)

taxa_dois_anos = 6.8

n_total_weekdays_expiry = get_total_weekdays(dt_compra, dt_vencimento)
taxa_contratada_total = get_total_interest_rate_multiplier(
    taxa_contratada, n_total_weekdays_expiry
)

n_total_weekdays_venda = get_total_weekdays(dt_venda, dt_vencimento)
taxa_venda_total_pos = get_total_interest_rate_multiplier(
    taxa_dois_anos, n_total_weekdays_venda
)

valor_updated_venda_pos = valor_updated * taxa_contratada_total / taxa_venda_total_pos

print(valor_updated_venda_pos)


dt_vencimento_longo = date(2065, 5, 15)
taxa_longo = 7
n_total_weekdays_longo = get_total_weekdays(dt_extracao_dados, dt_vencimento_longo)
taxa_contratada_total_longo = get_total_interest_rate_multiplier(
    taxa_longo, n_total_weekdays_longo
)

n_total_weekdays_venda_longo = get_total_weekdays(dt_venda, dt_vencimento_longo)
taxa_venda_total_pos_longo = get_total_interest_rate_multiplier(
    taxa_dois_anos, n_total_weekdays_venda_longo
)

print(valor_updated_venda_hoje * taxa_contratada_total_longo)
print(
    valor_updated_venda_hoje * taxa_contratada_total_longo / taxa_venda_total_pos_longo
)
