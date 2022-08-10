
data_request = {
    "watt_eastron": {
        "addr": 1,
        "func": 4,
        "start_reg": 12,
        "qty_reg": 2,
        "alive": 0,
        "raw": 0x00,
    },

    "deye_chint_1p": {
        "addr": 1,
        "func": 3,
        "start_reg": 8192,
        "qty_reg": 6,
        "alive": 0,
        "raw": 0x00,
    }
}

data_register_master = {
    30013: {
        "alive": 0,
        "raw": b'\x00',
        "value": 0,
        "act": {"unpack": ">f", "scale": 1, "unit": "W", },
    },

    48193: {
        "alive": 0,
        "raw": b'\x00',
        "value": 0,
        "act": None,
    },
}


data_register_slave = {

    # solax ask from: func 03 , 00 0e = 14+1 = offset 40015
    40015: {
        "master": 30013,
        "func": 0x03,
        "act": {"pack": ">h", "scale": 1, "data_type": "int"}
    },

    # solax ask from: func 03,  00 0b = 11+1 = offset 40012
    40012: {
        "master": -1,
        "func": 0x03,
        "act": {"pack": ">h", "scale": 1, "value": 0}
    },

    # solax ask from: func 03, 8+1 = offset 40009
    40009: {
        "master": -1,
        "func": 0x03,
        "act": {"pack": ">h", "scale": 1, "value": 0}
    },

    # daye ask from: func 03, 00 0e = 14+1 = offset 48193
    48193: {
        "master": 48193,
        "func": 0x03,
        "act": None
    },
}

panel_slave_addr = [1]
