from user import User
from client import Client
from taxidriver import TaxiDriver
from car import Car
from taxi import Taxi
from taxi_run import TaxiRun


if __name__ == '__main__':

    dados_cliente_1 = {
        'id' : 1234,
        'cpf' : 9209209209,        
        'name' : 'Ricardo Tavares',
        'address' : 'UCAM',
        'email' : 'ricardo.tavares@ucam-campos.br',
        'phone_number' : '123456789',
        'login' : 'rickardotavares',
        'password' : '951357'
    }

    cliente_1 = Client(**dados_cliente_1)
    print(cliente_1.name)
    print(cliente_1.login)
    cliente_1.login = 'ricardo_tavares'
    print(cliente_1.login)

    dados_taxista_1 = {
        'id' : 4321,
        'cpf' : 98765432132,        
        'name' : 'Zé do Taxi',
        'address' : 'Avenida Pelinca',
        'email' : 'ze@ze_do_taxi.com',
        'phone_number' : '789456123',
        'login' : 'ze_do_taxi',
        'password' : '1598753',
        'drivers_license' : '321654987'
    }

    taxista_1 = TaxiDriver(**dados_taxista_1)
    print(taxista_1.name)
    print(taxista_1.email)
    taxista_1.email = 'ze_do_taxi@taxi.com.br'
    print(taxista_1.email)

    dados_car_1 = {
        'id' : 1,        
        'name' : 'Golf Sapão 2004',
        'brand' : 'VW',
    }

    car_1 = Car(**dados_car_1)
    print(car_1.id)
    print(car_1.name)
    print(car_1.brand)
    car_1.id = 12
    print(car_1.id)
    print(car_1.name)
    print(car_1.brand)

    dados_taxi_1 = {
        'id' : 654,        
        'description' : 'Rebaixado, banco de couro, ar condicionado quebrado',
        'license_number' : 'QPSO10923',
        'license_plate' : 'XPT1O23',
        'km' : 999999,
        'type' : car_1,
    }

    taxi_1 = Taxi(**dados_taxi_1)
    print(taxi_1.id)
    print(taxi_1.description)
    print(taxi_1.km)
    print(taxi_1.type.brand)
    print(taxi_1.type.name)

    dados_car_2 = {
        'id' : 2,        
        'name' : 'Corolla',
        'brand' : 'Toyota',
    }

    car_2 = Car(**dados_car_2)

    taxi_1.type = car_2
    print(taxi_1.id)
    print(taxi_1.description)
    print(taxi_1.km)
    print(taxi_1.type.brand)
    print(taxi_1.type.name)

    dados_taxi_run_1 = {
        'id' : 1,        
        'address_start' : 'Avenida Pelinca, 1234',
        'address_stop' : 'UCAM',

        'latitude_start' : '123456',
        'longitude_start' : '654321',
        'latitude_stop' : '987564',
        'longitude_stop' : '4564123',

        'client' : cliente_1,
        'taxi_driver' : taxista_1,
        'taxi' : taxi_1,
    }
    print(' ')
    print('#### Extrato da Corrida ####')
    taxi_run_1 = TaxiRun(**dados_taxi_run_1)
    taxi_run_1.iniciar_corrida()
    taxi_run_1.finalizar_corrida()
    print(taxi_run_1.datetime_start)
    print(taxi_run_1.datetime_stop)
    print(taxi_run_1.duration_in_minutes)
    print(taxi_run_1.taxi_run_value)
    print(taxi_run_1.client.name)
    print(taxi_run_1.taxi_driver.name)
    print(taxi_run_1.taxi.description)
    print(taxi_run_1.taxi.type.name)
    print(taxi_run_1.taxi.type.brand)

