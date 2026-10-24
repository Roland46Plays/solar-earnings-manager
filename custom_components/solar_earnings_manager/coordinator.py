from homeassistant.helpers.event import (
    async_track_time_change,
)

from .recorder import capture_daily_data

from .const import (
    CAPTURE_TIME,
    DOMAIN,
    DATA_STORAGE,
    CONF_TARIFF,
    CONF_EXPORT_ENTITY,
)


async def setup_scheduler(
    hass,
    entry,
):
    """Set up daily capture scheduler."""

    async def scheduled_capture(now):
        storage = (
            hass.data[DOMAIN]
            [entry.entry_id]
            [DATA_STORAGE]
        )

        tariff = entry.data.get(
            CONF_TARIFF,
            0.0,
        )

        export_entity = entry.data.get(
            CONF_EXPORT_ENTITY
        )

        if not export_entity:
            return

        await capture_daily_data(
            hass=hass,
            storage=storage,
            tariff=tariff,
            export_entity=export_entity,
        )

    async_track_time_change(
        hass,
        scheduled_capture,
        hour=CAPTURE_TIME.hour,
        minute=CAPTURE_TIME.minute,
        second=0,
    )