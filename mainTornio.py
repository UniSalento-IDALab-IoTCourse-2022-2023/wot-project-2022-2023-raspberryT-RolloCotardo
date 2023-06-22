from pyModbusTCP.client import ModbusClient
from time import sleep
from random import *

# Connessione al server

client = ModbusClient(host="192.168.1.25", port=12345)
client.open()

lubrificante = 100

while True:

    # Parametri tornio
    allineamento = randint(23, 52) # 0.025-0.05 (valori moltiplicati per 1000)
    vibrazioni = randint(10, 220) # 0,1-2,0 (valori moltiplicati per 100)
    rotazione = randint(1495, 1605) # 1500-1600
    lubrificante = lubrificante - randint(1, 3)
    potenza = randint(6980, 7520) # 7000, 7500


    client.write_multiple_registers(7, [allineamento, vibrazioni, rotazione, lubrificante, potenza])

    if (lubrificante < 30):
        lubrificante = 100

    sleep(5)

