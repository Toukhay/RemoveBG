import argparse
import os
import sys
from pathlib import Path


def remove_background(input_path: Path, output_path: Path):
    try:
        from rembg import remove
        from PIL import Image
    except ImportError as ex:
        raise ImportError(
            "Faltan dependencias. Instala 'rembg' y 'Pillow' (pip install rembg pillow)"
        ) from ex

    if not input_path.exists():
        raise FileNotFoundError(f"El archivo de entrada no existe: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(input_path) as img_in:
        result = remove(img_in)

        if result is None:
            raise RuntimeError("La eliminación del fondo devolvió None. Revisa el archivo de entrada.")

        result.save(output_path, format="PNG")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convertir imagen a PNG con fondo removido usando rembg"
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Ruta del archivo de entrada (por ejemplo, leon/leon.jpg)",
    )
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Ruta del archivo de salida (por defecto: mismo nombre + .png)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescribir salida existente",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    input_path = args.input

    if args.output:
        output_path = args.output
    else:
        output_path = input_path.with_suffix(".png")

    if output_path.exists() and not args.force:
        print(f"Error: El archivo de salida ya existe: {output_path}. Usa --force para sobrescribir.")
        sys.exit(1)

    try:
        remove_background(input_path, output_path)
        print(f"OK: Imagen procesada y guardada en {output_path}")
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
