from typing import Callable


def process_function(func, t):
    if isinstance(func, Callable):
        return func(t)
    return func


def none_cmd(pitch, vel, s, t):
    midi_note = process_function(pitch, t)
    midi_vel = process_function(vel, t)
    print(f"At phrase {s}, time {t} play pitch {midi_note} "
          + f"with velocity {midi_vel}.")


def print_cmd(pitch, vel, s, t):
    midi_note = process_function(pitch, t)
    midi_vel = process_function(vel, t)
    print(f"At phrase {s}, time {t} play pitch {midi_note} "
          + f"with velocity {midi_vel}.")


class Note:
    def __init__(self, pitch, vel, cmd):
        if cmd is None:
            cmd = none_cmd
        self.pitch = pitch
        self.vel = vel
        self.cmd = cmd

    def render(self, s=0, t=0):
        return(self.cmd(self.pitch, self.vel, s, t))


class Phrase:
    def __init__(self, notes, time_sig):
        self.notes = []

        for note in notes:
            if note is None:
                note = Note(0, 0, None)
            self.notes.append(note)

        self.time_sig = time_sig

    @classmethod
    def from_pitches(cls, pitches, vel=88, cmd=None, time_sig=None):
        notes = []
        for pitch in pitches:
            if pitch is None:
                note = None
            else:
                note = Note(pitch, vel, cmd)
            notes.append(note)
        return(Phrase(notes, time_sig))

    @classmethod
    def from_trigs(cls, trigs, pitch=60, vel=88, cmd=None, time_sig=None):
        notes = [Note(pitch, vel, cmd) if bool else None for bool in trigs]
        return(Phrase(notes, time_sig))

    def render(self, s=0):
        render = [note.render(s, t) for t, note in enumerate(self.notes)]
        return render


class Chain:
    def __init__(self, phrases):
        self.phrases = phrases


class Track:
    def __init__(self, chains):
        self.chains = chains


class Song:
    def __init__(self, tracks):
        self.chains = tracks


if __name__ == "__main__":
    phrase = Phrase.from_trigs([True, True, False, True])
    for note in phrase.notes:
        print(note.pitch)
