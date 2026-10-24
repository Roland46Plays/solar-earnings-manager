import voluptuous as vol

from homeassistant import config_entries

from .const import (
    DOMAIN,
    CONF_EXPORT_ENTITY,
    CONF_TARIFF,
    CONF_CURRENCY,
    DEFAULT_TARIFF,
    DEFAULT_CURRENCY,
)


class SolarEarningsConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):

    VERSION = 1

    async def async_step_user(
        self,
        user_input=None,
    ):

        if user_input is not None:

            data = {
                CONF_EXPORT_ENTITY:
                    user_input[
                        CONF_EXPORT_ENTITY
                    ],

                CONF_TARIFF:
		    float(
                    user_input[
                        CONF_TARIFF
                    ]),

                CONF_CURRENCY:
                    user_input[
                        CONF_CURRENCY
                    ],
            }

            return self.async_create_entry(
                title="Solar Earnings Manager",
                data=data,
            )

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_EXPORT_ENTITY,
                ): str,

                vol.Required(
                    CONF_TARIFF,
                    default=DEFAULT_TARIFF,
                ): float,

                vol.Required(
                    CONF_CURRENCY,
                    default=DEFAULT_CURRENCY,
                ): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )