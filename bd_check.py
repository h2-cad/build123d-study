from build123d import Shape

def check(shape: Shape, name="part", volume=None, faces=None, edges=None, rel=1e-3):
    assert shape.is_valid, f"{name}: BRepCheck says invalid"   # property, not a call

    v, f, e = shape.volume, len(shape.faces()), len(shape.edges())
    print(f"{name}: volume={v:.3f}mm3 faces={f} edges={e} size={shape.bounding_box().size}")

    if volume is not None:
        assert abs(v - volume) <= rel * abs(volume), f"{name}: volume {v:.3f} != {volume:.3f}"

    if faces is not None:
        assert f == faces, f"{name}: faces {f} != {faces}"

    if edges is not None:
        assert e == edges, f"{name}: edges {e} != {edges}"

    return shape