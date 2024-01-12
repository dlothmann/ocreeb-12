print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB
from midi import Midi


# KEYTBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [layers, encoders, tapdance]

# SWITCH MATRIX
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoders.pins = ((board.A2, board.A1, board.A0, False), (board.SCK, board.MISO, board.MOSI, False),)

# EXTENSIONS
rgb_ext = RGB(pixel_pin = board.D10, num_pixels=4, hue_default=173)
midi_ext = Midi()
keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(midi_ext)
keyboard.debug_enabled = False

# MACROS ROW 1
GIT_PULL = simple_key_sequence([KC.G, KC.I, KC.T, KC.SPACE, KC.P, KC.U, KC.L, KC.L, KC.SPACE, KC.MACRO_SLEEP_MS(500), KC.ENTER])
SAVE = simple_key_sequence([KC.LCTRL(KC.S)])
COPY = simple_key_sequence([KC.LCTRL(KC.C)])
PASTE = simple_key_sequence([KC.LCTRL(KC.V)])

# MACROS ROW 2
G_FETCH = simple_key_sequence([KC.G, KC.I, KC.T, KC.SPACE, KC.F, KC.E, KC.T, KC.C, KC.H, KC.MACRO_SLEEP_MS(500), KC.ENTER])
G_ADD = simple_key_sequence([KC.G, KC.I, KC.T, KC.SPACE, KC.A, KC.D, KC.D, KC.SPACE, KC.LSHIFT(KC.RBRACKET), KC.MACRO_SLEEP_MS(500), KC.ENTER])
G_COMMIT = simple_key_sequence([KC.G, KC.I, KC.T, KC.SPACE, KC.C, KC.O, KC.M, KC.M, KC.I, KC.T, KC.SPACE, KC.SLASH, KC.M, KC.SPACE, KC.LSHIFT(KC.N2),KC.LSHIFT(KC.N2), KC.LEFT]) 
G_PUSH = simple_key_sequence([KC.G, KC.I, KC.T, KC.SPACE, KC.P, KC.U, KC.S, KC.H, KC.MACRO_SLEEP_MS(500), KC.ENTER])


# MACROS ROW 3
TERMINAL = simple_key_sequence([KC.LCMD(KC.R), KC.MACRO_SLEEP_MS(1000), KC.W, KC.T, KC.DOT, KC.E, KC.X, KC.E, KC.MACRO_SLEEP_MS(1000), KC.ENTER])
WORKSPACE = simple_key_sequence([KC.LCMD(KC.R), KC.MACRO_SLEEP_MS(500), KC.C, KC.LSHIFT(KC.DOT), KC.RALT(KC.MINUS), KC.W, KC.O, KC.R, KC.K, KC.S, KC.P, KC.A, KC.C, KC.E, KC.S, KC.MACRO_SLEEP_MS(500), KC.ENTER])
CAM = simple_key_sequence([KC.LCTRL(KC.LSFT(KC.O))])
MSTMUTE = simple_key_sequence([KC.LCTRL(KC.LSFT(KC.M))])


_______ = KC.TRNS
xxxxxxx = KC.NO

# LAYER SWITCHING TAP DANCE
TD_LYRS = KC.TD(MSTMUTE, KC.MO(1), xxxxxxx, KC.TO(2))
MIDI_OUT = KC.TD(KC.MIDI(70), xxxxxxx, xxxxxxx, KC.TO(0))

# array of default MIDI notes
# midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# KEYMAPS

keyboard.keymap = [
    # MACROS
    [
        TERMINAL,   WORKSPACE,     CAM,    TD_LYRS,
        G_FETCH,    G_ADD,          G_COMMIT,    G_PUSH,
        GIT_PULL,    SAVE,       COPY,     PASTE,
    ],
    # RGB CTL
    [
        xxxxxxx,    xxxxxxx,            xxxxxxx,                xxxxxxx,
        xxxxxxx,    KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,     KC.RGB_MODE_BREATHE_RAINBOW,
        xxxxxxx,    KC.RGB_MODE_PLAIN,  KC.RGB_MODE_BREATHE,    KC.RGB_MODE_RAINBOW,
    ],
    # MIDI
    [
        KC.MIDI(30),    KC.MIDI(69),      KC.MIDI(70),       MIDI_OUT,
        KC.MIDI(67),    KC.MIDI(66),      KC.MIDI(65),       KC.MIDI(64),
        KC.MIDI(60),    KC.MIDI(61),      KC.MIDI(62),       KC.MIDI(63),
    ]
]

encoders.map = [    ((KC.RGB_HUD, KC.RGB_HUI, KC.RGB_TOG),   (KC.VOLD,      KC.VOLU,        KC.MUTE)),   # MACROS
                    ((KC.RGB_AND, KC.RGB_ANI, xxxxxxx),     (KC.RGB_HUD,    KC.RGB_HUI,     _______   )),   # RGB CTL
                    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MIDI
                ]


if __name__ == '__main__':
    keyboard.go()
