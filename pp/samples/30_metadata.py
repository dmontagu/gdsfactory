""" # Metadata
Together with the GDS files that we send to the foundries we also store some .JSON dictionaries for each cell containing all the settings that we used to build the GDS.
By default the metadata will consists of all the parameters that were passed to the component function.
"""


if __name__ == "__main__":
    import pp

    c = pp.components.straight()

    print(c.settings)
    print(c.get_json())
