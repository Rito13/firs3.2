from cargo import Cargo

cargo = Cargo(
    id="gold",
    type_name="TTD_STR_CARGO_PLURAL_GOLD",
    unit_name="TTD_STR_CARGO_SINGULAR_GOLD",
    type_abbreviation="TTD_STR_ABBREV_GOLD",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes = ["CC_ARMOURED"],
    cargo_label="GOLD",
    units_of_cargo="TTD_STR_BAGS",
    items_of_cargo="TTD_STR_QUANTITY_GOLD",
    penalty_lowerbound="30",
    single_penalty_length="255",
    price_factor=152,
    capacity_multiplier="1",
    icon_indices=(3, 2),
    sprites_complete=False,
)
