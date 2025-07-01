class DeriveTools:
    def __init__(self):
        pass

    def calc_call_init_margin(self, spot_price, strike_price, mark_price):
        return (
            -max(0.15 - max(0, (strike_price - spot_price) / strike_price), 0)
            * spot_price
            + mark_price
        )

    def calc_call_maintenance_margin(self, spot_price, mark_price):
        return -0.09 * spot_price + mark_price

    def calc_put_init_margin(self, spot_price, strike_price, mark_price):
        return -max(
            max(0.15 - max(spot_price - strike_price, 0) / spot_price, 0.13)
            * spot_price
            - mark_price,
            -1.05 * self.calc_put_maintenance_margin(spot_price, mark_price),
        )

    def calc_put_maintenance_margin(self, spot_price, mark_price):
        return -max(0.09 * -mark_price, 0.09 * spot_price) + mark_price
    
    def calc_naked_call_contract(short_contract_size, long_contract_size):
        return -max(short_contract_size - long_contract_size, 0)
    
    def calc_naked_put_contract(short_contract_size, long_contract_size):
        return -max(short_contract_size - long_contract_size, 0)