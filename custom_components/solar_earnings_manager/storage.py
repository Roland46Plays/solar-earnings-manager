from homeassistant.helpers.storage import Store

from .const import (
    STORAGE_KEY,
    STORAGE_VERSION,
)


class SolarStorage:
    """Persistent storage for Solar Earnings Manager."""

    def __init__(self, hass):

        self.hass = hass

        self.store = Store(
            hass,
            STORAGE_VERSION,
            STORAGE_KEY,
        )

        self.data = {
            "actuals": [],
            "forecasts": [],
            "daily_summaries": [],
        }

    async def async_load(self):
        """Load data from Home Assistant storage."""

        stored = await self.store.async_load()

        if stored:
            self.data = stored

        # Handle upgrades from older versions
        self.data.setdefault(
            "actuals",
            [],
        )

        self.data.setdefault(
            "forecasts",
            [],
        )
        
        self.data.setdefault(
            "daily_summaries",
            [],
        )

    async def async_save(self):
        """Save data to Home Assistant storage."""

        await self.store.async_save(
            self.data
        )

    async def add_actual(
        self,
        record: dict,
    ):
        """Add an actual production/export record."""

        self.data["actuals"].append(
            record
        )

        await self.async_save()

    async def add_forecast(
        self,
        record: dict,
    ):
        """Add a forecast record."""

        self.data["forecasts"].append(
            record
        )

        await self.async_save()

    def get_actuals(self):
        """Return all actual records."""

        return self.data.get(
            "actuals",
            [],
        )

    def get_forecasts(self):
        """Return all forecast records."""

        return self.data.get(
            "forecasts",
            [],
        )

    def get_latest_actual(self):
        """Return newest actual record."""

        actuals = self.data.get(
            "actuals",
            [],
        )

        if not actuals:
            return None

        return actuals[-1]

    def get_latest_forecast(self):
        """Return newest forecast record."""

        forecasts = self.data.get(
            "forecasts",
            [],
        )

        if not forecasts:
            return None

        return forecasts[-1]

    def clear_all(self):
        """Clear all records in memory."""

        self.data = {
            "actuals": [],
            "forecasts": [],
            "daily_summaries": [],
        }
        
        