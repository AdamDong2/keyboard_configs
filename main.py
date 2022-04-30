print("Starting")

import board
from digitalio import DigitalInOut, Direction, Pull
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# sck = DigitalInOut(board.SCK)
# sck.direction = Direction.INPUT
# sck.pull = Pull.DOWN

keyboard.col_pins = (board.D0,board.D1,board.D2,board.A1,board.D3,board.D4,board.SDA,board.SCL,board.D7,board.D9,
                     board.D10,board.D11,board.D12,board.SCK)
keyboard.row_pins = (board.A2,board.A3,board.A4,board.A5,board.A0,)    # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.COL2ROW

xx = KC.NO
MO = KC.MO(1)
keyboard.keymap = [
    #df
    [
        KC.GRAVE, KC.N1 ,KC.N2 ,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.MINUS,KC.EQUAL,KC.BSPC,
        KC.TAB, KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.LBRC,KC.RBRC,KC.DEL,
        KC.ESCAPE,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCOLON,KC.QUOTE,KC.BSLASH,KC.ENTER,
        KC.LSHIFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMMA,KC.DOT,KC.SLASH,KC.RSHIFT,KC.UP,KC.PSCREEN,
        KC.LCTRL,xx,MO,KC.LALT,KC.INS,KC.SPC,KC.SPC,KC.HOME,KC.PGUP,KC.PGDN,KC.END,KC.LEFT,KC.DOWN,KC.RIGHT
    ],
    [
        xx,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,xx,
        xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,
        xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,
        xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,KC.CAPS,
        xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,xx,
    ]
]

if __name__ == '__main__':
    keyboard.go()
