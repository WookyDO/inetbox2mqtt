from machine import Pin

# this routine isn't nessecary - see bytes.hex(" ")
# def format_bytes(bytestring):
#     return " ".join("{:02x}".format(c) for c in bytestring)


def calculate_checksum(bytestring):
    # The checksum contains the inverted eight bit sum with carry over all data bytes or all data bytes and the protected identifier.
    cs = 0
    for b in bytestring:
        cs = (cs + b) % 0xFF

    cs = ~cs & 0xFF
    if cs == 0xFF:
        cs = 0
    return cs

PIN_MAPS = {
    # dc: in=true, pin-no, inverted=true
    
    
    "ESP32":
    {
    "mqtt_led": 14,
    "lin_led": 12,
    "lan": 0,
    "mdc" : 0,
    "mdio": 0,
    "ref_clk": 0,
    "lin_uart": 2,
    "lin_rx": 16,
    "lin_tx": 17,
    "dc_green_pin": [1, 18, 1], 
    "dc_red_pin": [1, 19, 1],
    "dc_i_pin": [0, 22, 1], 
    "dc_ii_pin": [0, 23, 1], 
    "sl_i2c": 1,
    "sl_sda": 26,
    "sl_scl": 25,
    },
    
    "LAN_WOMOLIN":
    {
    "mqtt_led": 14,
    "lin_led": 12,
    "lan": 1,
    "mdc" : 23,
    "mdio": 18,
    "ref_clk": 16,
    "lin_uart": 1,
    "lin_rx": 16,
    "lin_tx": 14,
    "dc_green_pin": [1, 18, 1], 
    "dc_red_pin": [1, 19, 1],
    "dc_i_pin": [0, 22, 1], 
    "dc_ii_pin": [0, 23, 1], 
    "sl_i2c": 1,
    "sl_sda": 26,
    "sl_scl": 25,
    },
    
    "WLAN_WOMOLIN_V1":
    {
    "mqtt_led": 14,
    "lin_led": 12,
    "lan": 0,
    "mdc" : 0,
    "mdio": 0,
    "ref_clk": 0,
    "lin_uart": 1,
    "lin_rx": 16,
    "lin_tx": 14,
    "dc_green_pin": [1, 18, 1], 
    "dc_red_pin": [1, 19, 1],
    "dc_i_pin": [0, 22, 1], 
    "dc_ii_pin": [0, 23, 1], 
    "sl_i2c": 1,
    "sl_sda": 26,
    "sl_scl": 25,
    },

    "WLAN_WOMOLIN_V2":
    {
    "mqtt_led": 13,
    "lin_led": 12,
    "lan": 0,
    "mdc" : 0,
    "mdio": 0,
    "ref_clk": 0,
    "lin_uart": 1,
    "lin_rx": 14,
    "lin_tx": 15,
    "dc_green_pin": [1, 18, 1], 
    "dc_red_pin": [1, 19, 1],
    "dc_i_pin": [0, 22, 1], 
    "dc_ii_pin": [0, 23, 1], 
    "sl_i2c": 1,
    "sl_sda": 26,
    "sl_scl": 25,
    },
    
    "RP2":
    {
    "mqtt_led": 14,
    "lin_led": 12,
    "lan": 0,
    "mdc" : 0,
    "mdio": 0,
    "ref_clk": 0,
    "lin_uart": 1,
    "lin_rx": 5,
    "lin_tx": 4,
    "dc_green_pin": [1, 18, 1], 
    "dc_red_pin": [1, 19, 1],
    "dc_i_pin": [0, 22, 1], 
    "dc_ii_pin": [0, 23, 1], 
    "sl_i2c": 1,
    "sl_sda": 2,
    "sl_scl": 3,
    },
    
    }
    


class PIN_MAP():
    
    _PIN_MAP = {}

    def __init__(self, p):
        self._PIN_MAP = p
        
    def get_pin(self, s):
        return self._PIN_MAP[s]

    def get_data(self, s):
        return self._PIN_MAP[s]

    def set_led(self, s, b):
        p = Pin(self._PIN_MAP[s], Pin.OUT)
        if b: p.value(0)
        else: p.value(1)
        
    def toggle_led(self, s):
        p = Pin(self._PIN_MAP[s], Pin.OUT)
        p.value(not(p.value()))
        
    def dtoggle_led(self, s):
        p = Pin(self._PIN_MAP[s], Pin.OUT)
        p.value(not(p.value()))
        p.value(not(p.value()))
     
    # input pin, mode:inverted
    def get_gpio(self, s):
        if self._PIN_MAP[2]:
            p0 = Pin(self._PIN_MAP[s][1], Pin.IN, Pin.PULL_UP)
        else:
            p0 = Pin(self._PIN_MAP[s][1], Pin.IN, Pin.PULL_DOWN)
        v = (p0.value() != self._PIN_MAP[2])    
    #    print("check pin", p, " inv: ", i, " Val: ", v)
        return v

    # pin, inverted, value ("ON", "OFF")
    def set_gpio(self, s, v):
   #     p, i, v):
        p0 = Pin(self._PIN_MAP[s][1], Pin.OUT)
        v = (v != self._PIN_MAP[s][2])
        p0.value(v)
    #    print("set pin", p, " inv: ", i, " to: ", v)

