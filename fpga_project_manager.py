import pyfpga
import subprocess
import os

# Run shell commands
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print(f"Error: {err.decode('utf-8')}")
    else:
        print(out.decode('utf-8'))

# Define the project
def define_project(project_name, top_module, sources):
    project = pyfpga.Project(name=project_name, top=top_module)
    for source in sources:
        project.add_source(source)
    return project

# Add tools to project
def add_tools(project):
    project.add_tool("yosys", "yosys -m ghdl -p 'ghdl {top}.vhdl -e {top}; synth_gowin -json {top}.json'")
    project.add_tool("nextpnr", "nextpnr-himbaechel --json {top}.json --write pnr{top}.json --device GW1NR-LV9QN88PC6/I5 --vopt family=GW1N-9C --vopt cst=constraints.cst")
    project.add_tool("gowin_pack", "gowin_pack -d GW1N-9C -o pack.fs {top}_routed.json")
    project.add_tool("openfpgaloader", "sudo openFPGALoader -b tangnano9k pack.fs")

# Cocotb Testlauf
def run_cocotb_test(top_module, source_files):
    env = os.environ.copy()
    env["TOPLEVEL_LANG"] = "vhdl"
    env["TOPLEVEL"] = top_module
    env["MODULE"] = "test_top"
    env["SIM"] = "ghdl"

    print("Starte Cocotb-Test...")
    result = subprocess.run("make -C sim", shell=True, env=env)

    if result.returncode != 0:
        print("Cocotb Test fehlgeschlagen.")
        return False

    print("Cocotb Test erfolgreich.")
    return True

# Run synthesis
def synthesize_vhdl(project):
    print("Starte Synthese...")
    if not project.run("yosys"):
        print("Synthese fehlgeschlagen.")
        return False
    print("Synthese abgeschlossen.")
    return True

# Place & Route
def place_and_route(project):
    print("Starte Place & Route...")
    if not project.run("nextpnr"):
        print("Place & Route fehlgeschlagen.")
        return False
    print("PnR abgeschlossen.")
    return True

# Bitstream erzeugen
def generate_bitstream(project):
    print("Generiere Bitstream...")
    if not project.run("gowin_pack"):
        print("Bitstream-Generierung fehlgeschlagen.")
        return False
    print("Bitstream fertig.")
    return True

# Flashen
def flash_fpga(project):
    print("⚡ Flashe FPGA...")
    if not project.run("openfpgaloader"):
        print("Flash fehlgeschlagen.")
        return False
    print("FPGA geflasht.")
    return True

# Hauptfunktion
def manage_fpga_project(project_name, top_module, sources):
    project = define_project(project_name, top_module, sources)
    add_tools(project)

    # Simulieren vor Synthese
    if not run_cocotb_test(top_module, sources):
        return

    if not synthesize_vhdl(project):
        return
    if not place_and_route(project):
        return
    if not generate_bitstream(project):
        return
    if not flash_fpga(project):
        return

    print("Projekt erfolgreich abgeschlossen!")

# Einstiegspunkt
if __name__ == "__main__":
    project_name = "MyFPGAProject"
    top_module = "top"
    sources = ["top.vhdl"]  # ggf. erweitern: ["top.vhdl", "mod1.vhdl", ...]

    manage_fpga_project(project_name, top_module, sources)
