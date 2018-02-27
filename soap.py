import osa

currencysystem = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')


def webservicex_client(service):
    return osa.Client('http://www.webservicex.net/{}.asmx?WSDL'.format(service))


# Задача №1
def average_temperature(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
        f_values = data.split('\n')
        c_values = []
        for temp in f_values:
            temp = temp.replace(' F', '')
            c_values.append(webservicex_client('ConvertTemperature')
                            .service.ConvertTemp(temp, 'degreeFahrenheit', 'degreeCelsius'))
        return round(float(sum(c_values) / len(c_values)), 1)


print('Средняя температура за неделю: {} C'.format(average_temperature('temps.txt')))


# Задача №2
def flights_total(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
        flights = data.split('\n')
        flight_prices = []
        for flight in flights:
            price = flight.split(' ')[1]
            currency = flight.split(' ')[2]
            flight_prices.append(currencysystem.service.ConvertToNum('', currency, 'RUB', price, 'false', '', ''))
        return round(sum(flight_prices))


print('На путешествие потрачено {} рублей'.format(flights_total('currencies.txt')))


# Задача №3
def convert_length_unit(value):
    return


def travel_length(file_path):
    with open(file_path, 'rt') as f:
        data = f.read()
        segments = data.split('\n')
        lengths = []
        for segment in segments:
            miles = float(segment.split(' ')[1].replace(',', ''))
            lengths.append(webservicex_client('length').service.ChangeLengthUnit(miles, 'Miles', 'Kilometers'))
        return round(sum(lengths), 2)
        

print('Суммарное расстояние пути: {} км.'.format(travel_length('travel.txt')))


