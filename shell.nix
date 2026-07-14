{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "puppeteer-shell";

  packages = [
    pkgs.nodejs_20
    pkgs.chromium

		(pkgs.python3.withPackages (ps: [
			ps.regex
		]))
  ];

  # Chromium runtime deps Puppeteer expects
  buildInputs = with pkgs; [
    atk
    at-spi2-atk
    cairo
    cups
    dbus
    expat
    fontconfig
    freetype
    gdk-pixbuf
    glib
    gtk3
    libdrm
    libxkbcommon
    mesa
    nspr
    nss
    pango
    systemd
    xorg.libxcb
  ];

  shellHook = ''
    export PUPPETEER_SKIP_DOWNLOAD=true
    export PUPPETEER_EXECUTABLE_PATH=${pkgs.chromium}/bin/chromium
    echo "Puppeteer ready"
  '';
}
