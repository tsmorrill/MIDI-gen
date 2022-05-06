C0 = 12
Db0 = 13
D0 = 14
Eb0 = 15
E0 = 16
F0 = 17
Gb0 = 18
G0 = 19
Ab0 = 20
A0 = 21
Bb0 = 22
B0 = 23
C1 = 24
Db1 = 25
D1 = 26
Eb1 = 27
E1 = 28
F1 = 29
Gb1 = 30
G1 = 31
Ab1 = 32
A1 = 33
Bb1 = 34
B1 = 35
C2 = 36
Db2 = 37
D2 = 38
Eb2 = 39
E2 = 40
F2 = 41
Gb2 = 42
G2 = 43
Ab2 = 44
A2 = 45
Bb2 = 46
B2 = 47
C3 = 48
Db3 = 49
D3 = 50
Eb3 = 51
E3 = 52
F3 = 53
Gb3 = 54
G3 = 55
Ab3 = 56
A3 = 57
Bb3 = 58
B3 = 59
C4 = 60
Db4 = 61
D4 = 62
Eb4 = 63
E4 = 64
F4 = 65
Gb4 = 66
G4 = 67
Ab4 = 68
A4 = 69
Bb4 = 70
B4 = 71
C5 = 72
Db5 = 73
D5 = 74
Eb5 = 75
E5 = 76
F5 = 77
Gb5 = 78
G5 = 79
Ab5 = 80
A5 = 81
Bb5 = 82
B5 = 83
C6 = 84
Db6 = 85
D6 = 86
Eb6 = 87
E6 = 88
F6 = 89
Gb6 = 90
G6 = 91
Ab6 = 92
A6 = 93
Bb6 = 94
B6 = 95
C7 = 96
Db7 = 97
D7 = 98
Eb7 = 99
E7 = 100
F7 = 101
Gb7 = 102
G7 = 103
Ab7 = 104
A7 = 105
Bb7 = 106
B7 = 107
C8 = 108
Db8 = 109
D8 = 110
Eb8 = 111
E8 = 112
F8 = 113
Gb8 = 114
G8 = 115
Ab8 = 116
A8 = 117
Bb8 = 118
B8 = 119
C9 = 120
Db9 = 121
D9 = 122
Eb9 = 123
E9 = 124
F9 = 125
Gb9 = 126
G9 = 127

pp = 22
p = 43
mp = 64
mf = 85
f = 106
ff = 127


def process_function(func, t):
    if isinstance(func, int):
        return func
    return func(t)


def none_cmd(pitch, vel, t):
    midi_note = process_function(pitch, t)
    midi_vel = process_function(vel, t)
    print(f"At time {t} play pitch {midi_note} with velocity {midi_vel}.")


def print_cmd(pitch, vel, t):
    midi_note = process_function(pitch, t)
    midi_vel = process_function(vel, t)
    print(f"At time {t} play pitch {midi_note} with velocity {midi_vel}.")


def process_chain(chain):
    def process_phrase(phrase):
        for t, [pitch, vel, cmd] in enumerate(phrase):
            if cmd is None:
                cmd = none_cmd
            cmd(pitch, vel, t)

    for phrase in chain:
        process_phrase(phrase)


if __name__ == "__main__":
    phrase = [[C3,  f, print_cmd],
              [C3, mf, print_cmd],
              [C3, mp, print_cmd],
              [C3,  p, print_cmd]]
    chain = [phrase, phrase]
    process_chain(chain)
