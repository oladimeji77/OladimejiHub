import uuid, random
import decimal
from decimal import Decimal
x = 0.1
y = 0.1
z = 0.1

print(x + y + z)

x = Decimal('0.1')
y = Decimal('0.1')
z = Decimal('0.1')

print(x + y + z)
print(Decimal(49000000.0) - Decimal(2000))
dec= Decimal("49000000.0") - Decimal("2000")
print(dec)

rnd = random.Random()
#rnd.seed(123) # NOTE: Of course don't use a static seed in production
new_uuid = uuid.UUID(int=rnd.getrandbits(128), version=4)
print(new_uuid)


random.Random()
print(random.random())
random.seed(10)
print(random.random())
