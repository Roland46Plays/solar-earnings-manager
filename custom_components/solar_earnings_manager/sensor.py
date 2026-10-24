from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, DATA_STORAGE

from .statistics import (
    get_latest_actual,
    get_latest_forecast,
    get_today_summary,
    get_weekly_summary,
    get_monthly_summary,
    get_yearly_summary,
    get_weekly_accuracy,
    get_monthly_accuracy,
    get_yearly_accuracy,
    get_history,
)


async def async_setup_entry(
    hass,
    entry: ConfigEntry,
    async_add_entities,
):

    storage = (
        hass.data[DOMAIN]
        [entry.entry_id]
        [DATA_STORAGE]
    )

    async_add_entities(
        [
            SolarEarningsStatusSensor(entry),
            SolarForecastTodaySensor(storage, entry),
            SolarActualExportSensor(storage, entry),
            ForecastIncomeSensor(storage, entry),
            ActualIncomeSensor(storage, entry),
            VarianceKWhSensor(storage, entry),
            VarianceIncomeSensor(storage, entry),
            AccuracySensor(storage, entry),
            WeeklyActualSensor(storage, entry,),
            WeeklyForecastSensor(storage, entry,),
            MonthlyActualSensor(storage, entry,),
            MonthlyForecastSensor(storage, entry,),
            YearlyActualSensor(storage, entry,),
            YearlyForecastSensor(storage, entry,),
            WeeklyActualIncomeSensor(storage, entry,),
            WeeklyForecastIncomeSensor(storage, entry,),
            MonthlyActualIncomeSensor(storage, entry,),
            MonthlyForecastIncomeSensor(storage, entry,),
            YearlyActualIncomeSensor(storage, entry,),
            YearlyForecastIncomeSensor(storage, entry,),
            WeeklyAccuracySensor(storage, entry,),
            MonthlyAccuracySensor(storage, entry,),
            YearlyAccuracySensor(storage, entry,),
            HistorySensor(storage, entry,),
        ]
    )


class BaseSensor(SensorEntity):

    def __init__(
        self,
        storage,
        entry,
    ):
        self.storage = storage
        self.entry = entry

        self.currency = (
            entry.data.get(
                "currency",
                "GBP"
            )
        )


class SolarEarningsStatusSensor(
    SensorEntity
):

    def __init__(self, entry):

        self._attr_name = (
            "Solar Earnings Status"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_status"
        )

    @property
    def native_value(self):
        return "running"


class SolarForecastTodaySensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Forecast Today"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_forecast_today"
        )

    @property
    def native_value(self):

        forecast = get_latest_forecast(
            self.storage
        )

        if not forecast:
            return 0

        return forecast.get(
            "forecast_kwh",
            0,
        )


class SolarActualExportSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Actual Export"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_actual_export"
        )

    @property
    def native_value(self):

        actual = get_latest_actual(
            self.storage
        )

        if not actual:
            return 0

        return actual.get(
            "actual_kwh",
            0,
        )


class ForecastIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Forecast Income Today"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_forecast_income"
        )

    @property
    def native_value(self):

        summary = get_today_summary(
            self.storage
        )

        if not summary:
            return 0

        return summary.get(
            "forecast_earnings",
            0,
        )


class ActualIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Actual Income Today"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_actual_income"
        )

    @property
    def native_value(self):

        summary = get_today_summary(
            self.storage
        )

        if not summary:
            return 0

        return summary.get(
            "actual_earnings",
            0,
        )


class VarianceKWhSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Variance kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_variance_kwh"
        )

    @property
    def native_value(self):

        summary = get_today_summary(
            self.storage
        )

        if not summary:
            return 0

        return summary.get(
            "variance_kwh",
            0,
        )


class VarianceIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Variance Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_variance_income"
        )

    @property
    def native_value(self):

        summary = get_today_summary(
            self.storage
        )

        if not summary:
            return 0

        return summary.get(
            "variance_earnings",
            0,
        )


class AccuracySensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Accuracy"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_accuracy"
        )

    @property
    def native_value(self):

        summary = get_today_summary(
            self.storage
        )

        if not summary:
            return 0

        return summary.get(
            "accuracy_percent",
            0,
        )

class WeeklyActualSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Weekly Actual kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_weekly_actual"
        )

    @property
    def native_value(self):

        return get_weekly_summary(
            self.storage
        )["actual_kwh"]


class WeeklyForecastSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Weekly Forecast kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_weekly_forecast"
        )

    @property
    def native_value(self):

        return get_weekly_summary(
            self.storage
        )["forecast_kwh"]


class MonthlyActualSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Monthly Actual kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_monthly_actual"
        )

    @property
    def native_value(self):

        return get_monthly_summary(
            self.storage
        )["actual_kwh"]


class MonthlyForecastSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Monthly Forecast kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_monthly_forecast"
        )

    @property
    def native_value(self):

        return get_monthly_summary(
            self.storage
        )["forecast_kwh"]


class YearlyActualSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Yearly Actual kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_yearly_actual"
        )

    @property
    def native_value(self):

        return get_yearly_summary(
            self.storage
        )["actual_kwh"]


class YearlyForecastSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Yearly Forecast kWh"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_yearly_forecast"
        )

    @property
    def native_value(self):

        return get_yearly_summary(
            self.storage
        )["forecast_kwh"]

class WeeklyActualIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Weekly Actual Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_weekly_actual_income"
        )

    @property
    def native_value(self):

        return get_weekly_summary(
            self.storage
        )["actual_income"]

class WeeklyForecastIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Weekly Forecast Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_weekly_forecast_income"
        )

    @property
    def native_value(self):

        return get_weekly_summary(
            self.storage
        )["forecast_income"]

class MonthlyActualIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Monthly Actual Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_monthly_actual_income"
        )
    
    @property
    def native_value(self):

        return get_monthly_summary(
            self.storage
        )["actual_income"]

class MonthlyForecastIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Monthly Forecast Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_monthly_forecast_income"
        )

    @property
    def native_value(self):

        return get_monthly_summary(
            self.storage
        )["forecast_income"]

class YearlyActualIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Yearly Actual Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_yearly_actual_income"
        )

    @property
    def native_value(self):

        return get_yearly_summary(
            self.storage
        )["actual_income"]

class YearlyForecastIncomeSensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Yearly Forecast Income"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_yearly_forecast_income"
        )

    @property
    def native_value(self):

        return get_yearly_summary(
            self.storage
        )["forecast_income"]
        
class WeeklyAccuracySensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Weekly Accuracy"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_weekly_accuracy"
        )

    @property
    def native_value(self):

        return get_weekly_accuracy(
            self.storage
        )


class MonthlyAccuracySensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Monthly Accuracy"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_monthly_accuracy"
        )

    @property
    def native_value(self):

        return get_monthly_accuracy(
            self.storage
        )


class YearlyAccuracySensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings Yearly Accuracy"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_yearly_accuracy"
        )

    @property
    def native_value(self):

        return get_yearly_accuracy(
            self.storage
        )


        
class HistorySensor(
    BaseSensor
):

    def __init__(
        self,
        storage,
        entry,
    ):

        super().__init__(
            storage,
            entry,
        )

        self._attr_name = (
            "Solar Earnings History"
        )

        self._attr_unique_id = (
            f"{entry.entry_id}_history"
        )

    @property
    def native_value(self):

        return len(
            get_history(
                self.storage
            )
        )

    @property
    def extra_state_attributes(self):

        return {
            "summaries": get_history(
                self.storage
            )
        }