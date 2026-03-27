# RemoveBG

Con este script se puede remover el bg de una imagen usando `rembg`.

## Requisitos

- Python 3.8+
- pip actualizado

## Instalación

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# o
source venv/bin/activate # macOS/Linux
pip install -r requirements.txt
```

## Uso simple

```bash
python python_bg/remove_bg.py ruta/a/tu/foto.jpg
```

Salida por defecto:
- `ruta/a/tu/foto.png`

## Uso con salida personalizada

```bash
python python_bg/remove_bg.py ruta/a/tu/foto.jpg ruta/a/tu/foto_salida.png
```

## Forzar sobrescritura

```bash
python python_bg/remove_bg.py ruta/a/tu/foto.jpg ruta/a/tu/foto_salida.png --force
```

## Qué hace

- Abre la imagen de entrada
- Remueve el fondo con `rembg`
- Guarda PNG con transparencia en la ruta de salida

## Notas

- Si no existe la entrada lanza error.
- Si el archivo de salida existe, no sobrescribe a menos que uses `--force`.

