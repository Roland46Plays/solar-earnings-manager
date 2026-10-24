DOMAIN = "solar_earnings_manager"

CONF_EXPORT_ENTITY = "export_entity"
CONF_TARIFF = "tariff"
CONF_CURRENCY = "currency"

DEFAULT_TARIFF = 0.175
DEFAULT_CURRENCY = "GBP"

STORAGE_VERSION = 1
STORAGE_KEY = DOMAIN

DATA_STORAGE = "storage"

from datetime import time

CAPTURE_TIME = time(
    hour=20,
    minute=30,
    second=0,
)

OPEN_METEO_FORECAST_SENSORS = [
    "sensor.home_energy_production_today",
    "sensor.home_energy_production_tomorrow",
    "sensor.home_energy_production_d2",
    "sensor.home_energy_production_d3",
    "sensor.home_energy_production_d4",
    "sensor.home_energy_production_d5",
    "sensor.home_energy_production_d6",
    "sensor.home_energy_production_d7",
]