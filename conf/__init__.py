import dataclasses
import configparser

__all__ = ('const', 'configure')


@dataclasses.dataclass(frozen=True)
class produce_const:
    a = 1
    b = 1


@dataclasses.dataclass(frozen=True)
class develop_const(produce_const):
    a = 2


const = develop_const()


configure = configparser.ConfigParser()
configure.read("./outside.ini")