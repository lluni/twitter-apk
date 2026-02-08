{
  description = "A development environment for twitter-apk with Java";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            jre          # Java Runtime Environment (OpenJDK)
          ];

          shellHook = ''
            echo "Environment loaded!"
            echo "Java: $(java --version | head -n1)"
          '';
        };
      }
    );
}
