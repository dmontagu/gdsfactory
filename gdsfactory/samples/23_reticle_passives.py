"""Write a sample reticle together with GDS file."""

import gdsfactory as gf
from gdsfactory.dft import add_label_yaml
from gdsfactory.read.labels import add_port_markers
from gdsfactory.types import Component


def mzi_te(**kwargs) -> Component:
    gc = gf.c.grating_coupler_elliptical_tm()
    c = gf.c.mzi_phase_shifter_top_heater_metal(delta_length=40)
    c = gf.routing.add_fiber_single(
        c, get_input_label_text_function=None, grating_coupler=gc
    )
    add_label_yaml(c)
    c = c.rotate(-90)
    return c


def test_mask() -> Component:
    c = gf.grid(
        [
            mzi_te(),
            mzi_te(),
            gf.functions.rotate(mzi_te),
            add_label_yaml(
                gf.functions.mirror(gf.routing.add_fiber_single(gf.components.mmi1x2))
            ),
        ]
    )
    gdspath = c.write_gds("mask.gds")
    csvpath = gf.mask.write_labels_gdspy(gdspath, prefix="component_name")

    # make sure that all the ports will be tested by adding port markers
    c2 = add_port_markers(gdspath=gdspath, csvpath=csvpath, marker_size=40)
    return c2


if __name__ == "__main__":
    c = test_mask()
    c.show()