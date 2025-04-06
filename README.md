# fpga-pyfpga-setup-9k
das reposetroy ist speziel fuer den tang nano 9k geeignet und ihn mit vhdl zu Programmieren mit opensource tools auf nixos um ein komplettes enviroment aufzusetzen einfach den schritten folgen:
```
git clone https://github.com/Daniel-Hohmann/python-fpga-workbench-setup-vhdl-9k.git
cd python-fpga-workbench-setup-vhdl-9k
```
Danach einfach den Befehl:
```
nix-shell
```
sobald die installation abgeschlossen ist sind die Tools:
- **yosys:** zum Synthetisieren der schaltung.
- **nextpnr:** zum Place-and-Routing
- **apicula(im python venv):** zum erzeugt die endgültigen Bitstreams(theoretisch noch viel mehr features).
- **openfpgaloader:** zum flashen vom bitstream auf den fpga.
zum einfachen benutzen und testen ob alles funktioniert hat den tang nano an den Computer anstecken und jetzt einfach die datei fpga_project_manager.py ausfuehren mit dem befehl:
```
python3 fpga_project_manager.py
```
die datei fpga_project_manager.py ist ein einfacher fpga Projektmanager der einem viel befehlzeilen arbeit abnimmt und das fpga Projekt managet er kann nach belieben veraendert und um funktionen ergaenzt werden wie testbranches mit Cocotb oder aber analyse von daten mit numpy,pandas und zum visualizieren matplotlib diese libs sind auch alle im venv enthalten und koennen einfach so genuzt werden.