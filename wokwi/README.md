# Wokwi component test bench

Each numbered configuration contains one independently connected workshop
component. This avoids GPIO conflicts and makes it clear which code controls
which part.

| Wokwi configuration | Matching teacher test |
|---|---|
| `01_onboard_led/wokwi.toml` | `01_onboard_led.py` |
| `02_external_led/wokwi.toml` | `02_external_led.py` |
| `03_button/wokwi.toml` | `03_button.py` |
| `04_potentiometer/wokwi.toml` | `04_potentiometer.py` |
| `05_rgb_pixels/wokwi.toml` | `05_rgb_pixels.py` |
| `06_passive_buzzer/wokwi.toml` | `06_passive_buzzer.py` |
| `07_distance_sensor/wokwi.toml` | `07_distance_sensor.py` |

The original `wokwi.toml` and `diagram.json` remain the combined
potentiometer/pixel spinner demonstration.

## Run a test

1. In VS Code, run **Wokwi: Select Config File** and choose one of the numbered
   `.toml` files above.
2. Run **Wokwi: Start Simulator** and keep the simulator visible.
3. Run **Tasks: Run Task → Wokwi: Run component test** and choose the matching
   numbered `.py` file.
4. Stop an ongoing test with **Ctrl+C** before selecting another circuit.

## Physical wiring is different where safety requires it

These Wokwi files demonstrate component behaviour. Build physical circuits
only from the workshop's checked HTML diagrams and connection tables.

- Wokwi's virtual buzzer is driven directly from GP15 because that is how its
  simulator model accepts PWM. The physical 5 V passive buzzer must use the
  course's 1 kΩ resistor and S8050 transistor driver.
- Wokwi's basic analogue model cannot simulate the HC-SR04 Echo voltage divider
  reliably. The virtual sensor therefore uses 3.3 V and connects Echo directly
  to GP18, so the simulated GPIO is not exposed to 5 V. The physical HC-SR04
  uses 5 V and must have the course's 1 kΩ/2 kΩ Echo divider.
