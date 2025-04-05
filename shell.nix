{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    cmake
    gcc
    glpk
    boost
    eigen
    python39 # Python selbst
    yosys
    yosys-ghdl
    ghdl-llvm
    nextpnr
    openfpgaloader
    usbutils
  ];

  shellHook = ''
    echo "Starte nix-shell enviroment for tang nano 9k fpga dev"
  '';
}

