TOPLEVEL_LANG ?= vhdl
SIM ?= ghdl

TOPLEVEL := top
MODULE := test_top

VHDL_SOURCES := ../top.vhd

include $(shell cocotb-config --makefiles)/Makefile.sim
GHDL_SIM_ARGS += --vcd=wave.vcd
