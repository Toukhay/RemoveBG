import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "leon", "leon.jpg")
output_path = os.path.join(script_dir, "leon", "leon.png")

if not os.path.exists(input_path):
    print(f"Error: El archivo {input_path} no existe.")
else:
    from rembg import remove
    from PIL import Image

    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path, format="PNG")
    print(f"Imagen procesada y guardada en {output_path}")
