# Modbus client
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time
import random

print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502)
reg=0; address=0

k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 0, 0

while True:
   # random data oluştur
   x = random.randint(80, 1300)
   print(x)

   if 0 < x < 200:
      k1, k2, k3, k4, k5, k6, k7 = 1, 0, 0, 0, 0, 0, 0
   elif 200 < x < 400:
      k1, k2, k3, k4, k5, k6, k7 = 0, 1, 0, 0, 0, 0, 0
   elif 400 < x < 600:
      k1, k2, k3, k4, k5, k6, k7 = 0, 0, 1, 0, 0, 0, 0
   elif 600 < x < 800:
      k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 1, 0, 0, 0
   elif 800 < x < 1000:
      k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 1, 0, 0
   elif 1000 < x < 1200:
      k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 1, 0
   elif 1200 < x < 1400:
      k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 0, 1
   else:
      k1, k2, k3, k4, k5, k6, k7 = 0, 0, 0, 0, 0, 0, 0

   print(k1, k2, k3, k4, k5, k6, k7)

   data = [k1, k2, k3, k4, k5, k6, k7]

   # print('-'*7,'Cycle ',i,'-'*30)
   time.sleep(1.0)

   # increment data by one
   # for i,d in enumerate(data):
   #    data[i] = d + 1

   # write holding registers (40001 to 40005)
   print('Write',data)
   builder = BinaryPayloadBuilder(byteorder=Endian.Big,\
                                  wordorder=Endian.Little)
   for d in data:
      builder.add_16bit_int(int(d))
   payload = builder.build()
   result  = client.write_registers(int(reg), payload,\
              skip_encode=True, unit=int(address))

   # read holding registers
   rd = client.read_holding_registers(reg,len(data)).registers
   print('Read',rd)

client.close()