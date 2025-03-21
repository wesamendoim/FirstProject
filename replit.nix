{ pkgs }: {
  deps = [
    pkgs.gdb
    pkgs.glibcLocales
    pkgs.unixODBC
    pkgs.tk
    pkgs.tcl
    pkgs.qhull
    pkgs.pkg-config
    pkgs.gtk3
    pkgs.gobject-introspection
    pkgs.ghostscript
    pkgs.freetype
    pkgs.ffmpeg-full
    pkgs.cairo
    pkgs.geckodriver
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}