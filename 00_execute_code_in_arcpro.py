filename = "02_add_raster_layers.py"
with open(filename, 'r') as f:
    code = compile(f.read(), filename, 'exec')
    exec(code)