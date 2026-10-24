import logging
from datetime import datetime, timedelta

from homeassistant.core import HomeAssistant

from .const import OPEN_METEO_FORECAST_SENSORS
from .statistics import build_daily_summary

_LOGGER = logging.getLogger(__name__)


async def capture_daily_data(
    hass: HomeAssistant,
    storage,
    tariff: float,
    export_entity: str,
):
    """Capture daily forecast and actual export data."""

    today = datetime.now().date()

    _LOGGER.warning(
        "SEM: export entity supplied = %s",
        export_entity,
    )

    export_state = hass.states.get(
        export_entity
    )

    _LOGGER.warning(
        "SEM: export state object = %s",
        export_state,
    )

    if export_state:
        _LOGGER.warning(
            "SEM: export state value = %s",
            export_state.state,
        )

    try:
        actual_export = float(
            export_state.state
        ) if export_state else 0.0

    except Exception as err:

        _LOGGER.error(
            "SEM: failed reading export sensor: %s",
            err,
        )

        actual_export = 0.0

    actual_earnings = round(
        actual_export * tariff,
        2,
    )

    actual_record = {
        "date": today.isoformat(),
        "capture_timestamp": datetime.now().isoformat(),
        "source_entity": export_entity,
        "source_state": (
            export_state.state
            if export_state
            else None
        ),
        "actual_kwh": round(
            actual_export,
            2,
        ),
        "tariff": tariff,
        "actual_earnings": actual_earnings,
    }

    storage.data.setdefault(
        "actuals",
        []
    ).append(
        actual_record
    )

    #
    # Build/replace today's summary
    #

    matching_forecasts = [

        x for x in
        storage.data.get(
            "forecasts",
            []
        )

        if x["forecast_date"]
        == today.isoformat()

    ]

    if matching_forecasts:

        latest_forecast = (
            matching_forecasts[-1]
        )

        summary = build_daily_summary(
            actual_record,
            latest_forecast,
        )

        daily_summaries = storage.data.setdefault(
            "daily_summaries",
            []
        )

        #
        # Remove any existing summary
        # for today before adding a new one
        #

        daily_summaries[:] = [

            x for x in daily_summaries

            if x["date"]
            != actual_record["date"]

        ]

        daily_summaries.append(
            summary
        )

    #
    # Capture 8-day Open-Meteo forecast
    #

    for offset, entity_id in enumerate(
        OPEN_METEO_FORECAST_SENSORS
    ):

        entity = hass.states.get(
            entity_id
        )

        try:

            forecast_value = (
                float(entity.state)
                if entity
                else 0.0
            )

        except Exception:

            forecast_value = 0.0

        forecast_date = (
            today + timedelta(days=offset)
        ).isoformat()

        forecast_record = {
            "capture_timestamp":
                datetime.now().isoformat(),

            "capture_date":
                today.isoformat(),

            "forecast_date":
                forecast_date,

            "forecast_kwh":
                round(
                    forecast_value,
                    2,
                ),

            "tariff":
                tariff,

            "forecast_earnings":
                round(
                    forecast_value * tariff,
                    2,
                ),
        }

        storage.data.setdefault(
            "forecasts",
            []
        ).append(
            forecast_record
        )

    await storage.async_save()