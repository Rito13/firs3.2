from cargo import Cargo

cargo = Cargo(
    id="coke",
    type_name="string(STR_CARGO_NAME_COKE)",
    unit_name="string(STR_CARGO_NAME_COKE)",
    type_abbreviation="string(STR_CID_COKE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="COKE",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_COKE)",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=97,
    capacity_multiplier="1",
    icon_indices=(1, 3),
    sprites_complete=True,
)
