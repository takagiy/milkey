{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39Packages.pygame

    # keep this line if you use bash
    pkgs.bashInteractive
  ];
}
