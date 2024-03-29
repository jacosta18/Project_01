import json

class RatesParser():
    def __init__(self,rates_file):   # we must pass in a valid json file at object instantiation
        rate_info = self.open_json_file(rates_file)
        self.base = rate_info['base']
        self.date = rate_info['date']
        self.rates = rate_info ['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    # rate_info is a dictionary
    # rate is another dictionary or another json file

    def open_json_file(self,json_file):
        with open(json_file) as rates:
            return json.load(rates)

rate_reader = RatesParser("exchange_rate.json")

print(rate_reader.gbp)
print(rate_reader.aud)



