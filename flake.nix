# flake.nix
{
  description = "Arduino-IDE, uses unstable";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs}: 
    let pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {

      devShell.x86_64-linux =
        pkgs.mkShell {
          buildInputs = [         
            pkgs.bashInteractive
            pkgs.arduino-ide
            pkgs.gnumake
            pkgs.wget
            pkgs.cmake
            pkgs.python3
            pkgs.python311Packages.pytest
            pkgs.python311Packages.colorama
            pkgs.sshpass
          ];

        };
   };
}
