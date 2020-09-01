import dataclasses


__all__ = ('const', )


@dataclasses.dataclass(frozen=True)
class produce:
    a = 1
    b = 1


@dataclasses.dataclass(frozen=True)
class develop(produce):
    a = 2


const = develop()