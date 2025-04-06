import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
import logging
import csv
import os

@cocotb.test()
async def test_led_blink(dut):
    clock = Clock(dut.clk, 10, units="ns")  # 100 MHz
    cocotb.start_soon(clock.start())
    dut._log.setLevel(logging.INFO)

    measurements = []  # Liste für [Zeit, LED-Wert]
    timestep_ns = 10  # Taktperiode

    for cycle in range(10000):  # Weniger Zyklen zum Testen
        await RisingEdge(dut.clk)
        timestamp = cycle * timestep_ns  # Simzeit in ns
        led_val = int(dut.led.value)
        measurements.append((timestamp, led_val))

        if cycle % 1000 == 0:
            dut._log.info(f"Takt {cycle}, LED={led_val}")

    # Ergebnisse in CSV speichern
    output_path = os.path.join(os.path.dirname(__file__), "led_trace.csv")
    with open(output_path, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time_ns", "led_value"])
        writer.writerows(measurements)

    dut._log.info(f"📊 Messdaten in {output_path} gespeichert.")

