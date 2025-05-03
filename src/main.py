import asyncio
from viam.module.module import Module
try:
    from models.gpio_pin_sensor import GpioPinSensor
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.gpio_pin_sensor import GpioPinSensor


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
