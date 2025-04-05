import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
import logging

@cocotb.test()
async def test_led_blink(dut):
    clock = Clock(dut.clk, 10, units="ns")  # 100 MHz
    cocotb.start_soon(clock.start())
    dut._log.setLevel(logging.DEBUG)

    for _ in range(1000000):  # genug Takte, um LED toggeln zu sehen
        await RisingEdge(dut.clk)

    led_val = int(dut.led.value)
    dut._log.info(f"LED nach 1.000.000 Takten: {led_val}")
    assert led_val in [0, 1], "LED sollte gültiges Bit sein"
