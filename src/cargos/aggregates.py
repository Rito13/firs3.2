from cargo import Cargo

cargo = Cargo(
    id="aggregates",
    type_name="string(STR_CARGO_NAME_AGGREGATES)",
    unit_name="string(STR_CARGO_NAME_AGGREGATES)",
    type_abbreviation="string(STR_CID_AGGREGATES)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_OPEN_BULK", "CC_NON_POTABLE"],
    cargo_label="AGRV",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_AGGREGATES)",
    penalty_lowerbound="40",
    single_penalty_length="255",
    price_factor=91,
    capacity_multiplier="1",
    icon_indices=(5, 1),
    sprites_complete=True,
)
