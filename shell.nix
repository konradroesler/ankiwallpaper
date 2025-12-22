{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    python3
    python3Packages.manim
		python312Packages.black

	  cairo
    pango
    ffmpeg
    pkg-config
  ];
}
