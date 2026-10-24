from datetime import datetime, timedelta


def get_latest_actual(storage):

    actuals = storage.data.get(
        "actuals",
        []
    )

    if not actuals:
        return None

    return actuals[-1]

def get_history(storage):

    return storage.data.get(
        "daily_summaries",
        []
    )

def get_latest_forecast(storage):

    forecasts = storage.data.get(
        "forecasts",
        []
    )

    today = (
        datetime.now()
        .date()
        .isoformat()
    )

    todays = [

        x for x in forecasts

        if x["forecast_date"]
        == today

    ]

    if not todays:
        return None

    return todays[-1]


def get_today_summary(storage):

    summaries = storage.data.get(
        "daily_summaries",
        []
    )

    if not summaries:
        return None

    return summaries[-1]


def build_daily_summary(
    actual_record,
    forecast_record,
):

    variance_kwh = round(
        actual_record["actual_kwh"]
        - forecast_record["forecast_kwh"],
        2,
    )

    variance_income = round(
        actual_record["actual_earnings"]
        - forecast_record["forecast_earnings"],
        2,
    )

    accuracy = 0

    if forecast_record["forecast_kwh"] > 0:

        accuracy = round(
            (
                actual_record["actual_kwh"]
                /
                forecast_record["forecast_kwh"]
            ) * 100,
            2,
        )

    return {

        "date":
            actual_record["date"],

        "forecast_kwh":
            forecast_record["forecast_kwh"],

        "actual_kwh":
            actual_record["actual_kwh"],

        "forecast_earnings":
            forecast_record["forecast_earnings"],

        "actual_earnings":
            actual_record["actual_earnings"],

        "variance_kwh":
            variance_kwh,

        "variance_earnings":
            variance_income,

        "accuracy_percent":
            accuracy,
    }


def get_weekly_summary(storage):

    summaries = storage.data.get(
        "daily_summaries",
        []
    )

    today = datetime.now().date()

    week_start = (
        today -
        timedelta(
            days=today.weekday()
        )
    )

    weekly = [

        x for x in summaries

        if datetime.fromisoformat(
            x["date"]
        ).date() >= week_start

    ]

    return {

        "actual_kwh":
            round(
                sum(
                    x["actual_kwh"]
                    for x in weekly
                ),
                2,
            ),

        "forecast_kwh":
            round(
                sum(
                    x["forecast_kwh"]
                    for x in weekly
                ),
                2,
            ),

        "actual_income":
            round(
                sum(
                    x["actual_earnings"]
                    for x in weekly
                ),
                2,
            ),

        "forecast_income":
            round(
                sum(
                    x["forecast_earnings"]
                    for x in weekly
                ),
                2,
            ),
    }

def get_weekly_accuracy(storage):

    weekly = get_weekly_summary(
        storage
    )

    forecast = weekly[
        "forecast_kwh"
    ]

    if forecast == 0:
        return 0

    return round(
        (
            weekly["actual_kwh"]
            / forecast
        ) * 100,
        2,
    )


def get_monthly_accuracy(storage):

    monthly = get_monthly_summary(
        storage
    )

    forecast = monthly[
        "forecast_kwh"
    ]

    if forecast == 0:
        return 0

    return round(
        (
            monthly["actual_kwh"]
            / forecast
        ) * 100,
        2,
    )


def get_yearly_accuracy(storage):

    yearly = get_yearly_summary(
        storage
    )

    forecast = yearly[
        "forecast_kwh"
    ]

    if forecast == 0:
        return 0

    return round(
        (
            yearly["actual_kwh"]
            / forecast
        ) * 100,
        2,
    )

def get_monthly_summary(storage):

    summaries = storage.data.get(
        "daily_summaries",
        []
    )

    now = datetime.now()

    monthly = [

        x for x in summaries

        if datetime.fromisoformat(
            x["date"]
        ).month == now.month

        and

        datetime.fromisoformat(
            x["date"]
        ).year == now.year

    ]

    return {

        "actual_kwh":
            round(
                sum(
                    x["actual_kwh"]
                    for x in monthly
                ),
                2,
            ),

        "forecast_kwh":
            round(
                sum(
                    x["forecast_kwh"]
                    for x in monthly
                ),
                2,
            ),

        "actual_income":
            round(
                sum(
                    x["actual_earnings"]
                    for x in monthly
                ),
                2,
            ),

        "forecast_income":
            round(
                sum(
                    x["forecast_earnings"]
                    for x in monthly
                ),
                2,
            ),
    }


def get_yearly_summary(storage):

    summaries = storage.data.get(
        "daily_summaries",
        []
    )

    now = datetime.now()

    yearly = [

        x for x in summaries

        if datetime.fromisoformat(
            x["date"]
        ).year == now.year

    ]

    return {

        "actual_kwh":
            round(
                sum(
                    x["actual_kwh"]
                    for x in yearly
                ),
                2,
            ),

        "forecast_kwh":
            round(
                sum(
                    x["forecast_kwh"]
                    for x in yearly
                ),
                2,
            ),

        "actual_income":
            round(
                sum(
                    x["actual_earnings"]
                    for x in yearly
                ),
                2,
            ),

        "forecast_income":
            round(
                sum(
                    x["forecast_earnings"]
                    for x in yearly
                ),
                2,
            ),
    }