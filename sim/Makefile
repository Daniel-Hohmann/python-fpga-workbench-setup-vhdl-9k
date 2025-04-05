TOPLEVEL_LANG ?= vhdl
SIM ?= ghdl
MODULE := $(shell echo $$MODULE)
TOPLEVEL := $(shell echo $$TOPLEVEL)
VHDL_SOURCES := ../top.vhdl

include $(shell cocotb-config --makefiles)/Makefile.sim
