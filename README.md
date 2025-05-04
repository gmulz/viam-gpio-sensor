# Module gpio-pin-sensor

A very simple sensor that reports the signal of a GPIO pin on a board

## Model grant-dev:gpio-pin-sensor:gpio-pin-sensor

A Sensor component that reports the GPIO pin signal on a board, 1 for high and 0 for low.

This sensor essentially wraps the Board API's exiting GPIO pin functionality into the Sensor API, so GetReadings reports the pin signal. This may prove a useful abstraction so GPIO pins can be used in a modular way and swapped out with other kinds of sensors, or for use with very simple components like switches or buttons

### Configuration

The following attribute template can be used to configure this model:

```json
{
"pin": <string>,
"board": <string>
}
```

#### Attributes

The following attributes are available for this model:

| Name    | Type   | Inclusion | Description                              |
| ------- | ------ | --------- | ---------------------------------------- |
| `pin`   | string | Required  | The name/number of the pin               |
| `board` | string | Required  | The name of the board that the pin is on |

#### Example Configuration

```json
{
  "pin": 15,
  "board": "board-1"
}
```

### GetReadings

GetReadings will report 1 if the pin is high, and 0 if it is low
