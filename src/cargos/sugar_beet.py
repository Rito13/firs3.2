from cargo import Cargo

cargo = Cargo(
    id="sugar_beet",
    type_name="string(STR_CARGO_NAME_SUGAR_BEET)",
    unit_name="string(STR_CARGO_NAME_SUGAR_BEET)",
    type_abbreviation="string(STR_CID_SUGAR_BEET)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_BULK"],
    cargo_label="SGBT",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_SUGAR_BEET)",
    penalty_lowerbound="5",
    single_penalty_length="30",
    price_factor=99,
    capacity_multiplier="1",
    icon_indices=(14, 1),
    sprites_complete=False,
)
