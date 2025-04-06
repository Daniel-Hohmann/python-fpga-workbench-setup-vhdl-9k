import subprocess
import os

class FPGAProject:
    def __init__(self, name, top_module, sources):
        self.name = name
        self.top = top_module
        self.sources = sources
        self.tools = {}

    def add_tool(self, name, command_template):
        self.tools[name] = command_template

    def run_tool(self, name):
        if name not in self.tools:
            print(f"[❌] Tool '{name}' nicht definiert.")
            return False

        command = self.tools[name].format(top=self.top)
        print(f"[▶] Starte: {command}")
        result = subprocess.run(command, shell=True)

        if result.returncode != 0:
            print(f"[❌] Tool '{name}' fehlgeschlagen.")
            return False

        print(f"[✅] Tool '{name}' erfolgreich.")
        return True

# Shell-Command Runner für allgemeine Zwecke
def run_command(command, env=None):
    print(f"[💻] Executing: {command}")
    result = subprocess.run(command, shell=True, env=env)
    if result.returncode != 0:
        print("[❌] Fehler beim Ausführen des Befehls.")
        return False
    return True

# Cocotb Simulation
def run_cocotb_test(top_module):
    env = os.environ.copy()
    env["TOPLEVEL_LANG"] = "vhdl"
    env["TOPLEVEL"] = top_module
    env["MODULE"] = "test_top"
    env["SIM"] = "ghdl"

    print("[🔬] Starte Cocotb Test...")
    return run_command("make -C sim", env=env)

# Synthese
def synthesize(project):
    return project.run_tool("yosys")

# Place & Route
def place_and_route(project):
    return project.run_tool("nextpnr")

# Bitstream
def generate_bitstream(project):
    return project.run_tool("gowin_pack")

# Flashen
def flash_fpga(project):
    return project.run_tool("openfpgaloader")

# Projekt-Manager-Funktion
def manage_fpga_project(project_name, top_module, sources):
    project = FPGAProject(project_name, top_module, sources)

    # Tools definieren
    project.add_tool("yosys", "yosys -m ghdl -p 'ghdl {top}.vhd -e {top}; synth_gowin -json {top}.json'")
    project.add_tool("nextpnr", "nextpnr-himbaechel --json {top}.json --write pnr{top}.json --device GW1NR-LV9QN88PC6/I5 --vopt family=GW1N-9C --vopt cst=constraints.cst")
    project.add_tool("gowin_pack", "gowin_pack -d GW1N-9C -o pack.fs pnr{top}.json")
    project.add_tool("openfpgaloader", "sudo openFPGALoader -b tangnano9k pack.fs")

    # Ablauf
    if not run_cocotb_test(top_module):
        print("[🚫] Cocotb Test fehlgeschlagen.")
        return
    if not synthesize(project):
        return
    if not place_and_route(project):
        return
    if not generate_bitstream(project):
        return
    if not flash_fpga(project):
        return

    print("✅ Projekt erfolgreich abgeschlossen!")

# Einstiegspunkt
if __name__ == "__main__":
    project_name = "MyFPGAProject"
    top_module = "top"
    sources = ["top.vhd"]  # Bei Bedarf weitere Dateien ergänzen

    manage_fpga_project(project_name, top_module, sources)