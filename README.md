# FPGA-Python-Setup-9K

Das Repository ist speziell für den Tang Nano 9K geeignet und ermöglicht die Programmierung mit VHDL unter Verwendung von Open-Source-Tools auf NixOS. Um ein vollständiges Entwicklungsumfeld einzurichten, folgen Sie einfach diesen Schritten:
```
git clone https://github.com/Daniel-Hohmann/python-fpga-workbench-setup-vhdl-9k.git
cd python-fpga-workbench-setup-vhdl-9k
```
Danach einfach den Befehl:
```
nix-shell
```
Nach Abschluss der Installation stehen folgende Tools zur Verfügung:
- **Yosys**: Zum Synthetisieren der Schaltung.
- **Nextpnr**: Für Place-and-Routing.
- **Apicula (im Python venv)**: Erzeugt die endgültigen Bitstreams (und bietet theoretisch viele weitere Features).
- **OpenFPGALoader**: Zum Flashen des Bitstreams auf den FPGA.

## Nutzung und Testen
1. Schließen Sie den Tang Nano 9K an den Computer an.
2. Führen Sie die Datei `fpga_project_manager.py` aus:
```
python3 fpga_project_manager.py
```
### FPGA-Projektmanager
Die Datei `fpga_project_manager.py` ist ein einfacher Projektmanager, der viele Befehlszeilenarbeiten automatisiert und das FPGA-Projekt verwaltet. Sie kann nach Belieben angepasst und um Funktionen wie Testbranches mit Cocotb oder Datenanalysen mit **Numpy**, **Pandas** und **Matplotlib** erweitert werden. Diese Bibliotheken sind bereits im virtuellen Python-Umfeld (venv) enthalten.

## To Do
1. **Ordnung in Build-Dateien**: 
- Implementieren, dass alle Build-Dateien in einem `build`-Ordner gespeichert werden, organisiert in Unterordnern je nach Tool.

2. **Automatische Visualisierung von Simulationsergebnissen**:
- Ergebnisse, die als CSV-Dat