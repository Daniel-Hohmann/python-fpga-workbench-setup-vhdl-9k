# fpga-pyfpga-setup-9k
a quick installation and setup guide for the Tang Nano 9k and vhdl

## Tools:
- Openfpgaloader
- yosys
- nextpnr-himbaechel
- apicula

## Programming tools/libs
### Projektmanagement Python
- fpga-pyfpga-setup-9k



pyfpga ist im endeffekt nur ein Projektmanager lib mit der man nicht nur Projekte bauen kann sondern auch simulieren kann mit der lib kann man einfach sein komplettes fpga Projekt managen.
```
pip3 install pyfpga
```

```
pip3 install cocotb numpy matplotlib pandas
```

libary fuer schnelles prototypen von HDL in python convertiert in verilog
```
pip3 install nmigen
```

1. VHDL – FPGA-Design und Synthese
VHDL ist die Hauptsprache für dein FPGA-Design.

Du definierst damit die digitale Logik und Architektur deines FPGA-Designs.

Du kannst damit Komponenten wie Filter, FFTs, Speichercontroller, Bus-Systeme usw. implementieren.

2. PyFPGA – FPGA-Toolchain in Python steuern
PyFPGA hilft dabei, FPGA-Projekte mit Python zu verwalten und Build-Prozesse zu automatisieren.

Es kann Synthese- und Implementierungsprozesse für verschiedene FPGA-Tools wie Vivado, Quartus oder Yosys steuern.

Du kannst damit verschiedene Konfigurationen ausprobieren, Skripte für das Generieren von VHDL-Code schreiben und Design-Flows optimieren.

3. Cocotb – Testen des FPGA-Designs mit Python
Cocotb (Coroutine Co-Simulation Testbench) ist eine coole Testumgebung für VHDL/Verilog-Designs.

Du kannst dein FPGA-Design mit Python-Skripten testen, anstatt komplexe Testbenches in VHDL zu schreiben.

Unterstützt Co-Simulation mit Simulatoren wie GHDL, ModelSim oder Xilinx XSim.

Du kannst damit gezielt Testfälle schreiben, Signalverläufe prüfen und Verifikationsaufgaben automatisieren.

4. NumPy – Mathematische und numerische Berechnungen
Falls dein FPGA-Design mathematische Berechnungen macht (z. B. DSP, Signalverarbeitung), kannst du mit NumPy Algorithmen in Python simulieren.

Vor der FPGA-Implementierung kannst du deine Algorithmen in NumPy testen und optimieren.

Nach dem Test kannst du sie in VHDL umsetzen und die Ergebnisse vergleichen.

5. Matplotlib – Visualisierung von FPGA-Signalen
Perfekt für das Plotten von Test- und Simulationsdaten, z. B. Signale, FFTs oder Zeitverläufe.

Du kannst Signale aus Cocotb-Simulationen oder echten FPGA-Messungen grafisch darstellen.

Ideal für Debugging und Analyse von Zeitverläufen.

6. Pandas – Datenanalyse und Log-Management
Wenn du viele Testläufe machst, kannst du mit Pandas die Testergebnisse analysieren.

Du kannst CSV-Dateien mit Simulationsergebnissen speichern und später auswerten.

Nützlich für komplexe Testauswertungen oder Regressionstests über viele FPGA-Versionen hinweg.


# wichtig 
https://github.com/YosysHQ/nextpnr?tab=readme-ov-file#nextpnr-himbaechel
das installieren und apicula nicht vergessen sehr wichtig um den code zu synthetisieren!!!


# Commands
zum flashen
```sudo openFPGALoader -b tangnano9k pack.fs```
zum Place & Route
```nextpnr-himbaechel \
  --json top.json \
  --write pnrblinky.json \
  --device GW1NR-LV9QN88PC6/I5 \
  --vopt family=GW1N-9C \
  --vopt cst=constraints.cst
```
apicula fuer Bitstream generation
``` gowin_pack -d GW1N-9C -o pack.fs blink_routed.json```
yosys synthese
```
yosys -m ghdl -p "ghdl blinky.vhdl -e blink; synth_gowin -json blinky.json"
```
