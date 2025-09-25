from functools import cache
from numbers import Number

@cache
def sort(width: Number, height: Number, length: Number, mass: Number) -> str:
    invalid_check = lambda x: x.real <= 0 or x.imag != 0
    input_args = {
        "width": invalid_check(width),
        "height": invalid_check(height),
        "length": invalid_check(length),
        "mass": invalid_check(mass)
    }
    def validate_inputs(validate_args: dict) -> None:
        invalids = list(map(lambda b: b[0], (
            filter(lambda k: k[1] is True, zip(validate_args, map(lambda x: x[1] is True, validate_args.items()))))))
        if len(invalids) > 0:
            raise ValueError(f'Invalid input arguments: ({",".join(invalids)}), all numbers must be positive and real')

    def match_package(dimensions: list[Number], input_mass: Number) -> str:
        check_fn = lambda x, y: sum(map(lambda k: 1 if k >= x else 0, y))
        heavy = check_fn(20, [input_mass]) > 0
        any_exceed = check_fn(150, dimensions) > 0
        all_exceed = check_fn(100, dimensions) == 3
        bulky = (any_exceed or all_exceed)
        if heavy and bulky:
            return "rejected"
        if heavy or bulky:
            return "special"
        return "standard"

    validate_inputs(input_args)
    return match_package([width, height, length], mass)