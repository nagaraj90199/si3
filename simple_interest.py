#!/usr/bin/env python3
"""
Simple Interest calculator

Provides a function `calculate_simple_interest(principal, rate, time)` that
returns (interest, total_amount). Also includes a small CLI and a self-test.
"""
from __future__ import annotations


def calculate_simple_interest(principal: float, rate: float, time: float) -> tuple[float, float]:
    """Calculate simple interest and total amount.

    Args:
        principal: Principal amount (must be >= 0).
        rate: Annual interest rate in percent (e.g., 5 for 5%). Must be >= 0.
        time: Time period in years. Must be >= 0.

    Returns:
        (interest, total_amount)

    Raises:
        ValueError: if any input is negative.
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("principal, rate and time must be non-negative")
    interest = principal * (rate / 100.0) * time
    total = principal + interest
    return interest, total


def _parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Simple Interest calculator")
    parser.add_argument("-p", "--principal", type=float, help="Principal amount")
    parser.add_argument("-r", "--rate", type=float, help="Annual interest rate (percent)")
    parser.add_argument("-t", "--time", type=float, help="Time in years")
    parser.add_argument("--test", action="store_true", help="Run simple self-test")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    if args.test:
        _run_tests()
        return

    try:
        principal = args.principal if args.principal is not None else float(input("Principal: "))
        rate = args.rate if args.rate is not None else float(input("Annual rate (percent): "))
        time = args.time if args.time is not None else float(input("Time (years): "))
    except ValueError:
        print("Invalid numeric input. Exiting.")
        return

    try:
        interest, total = calculate_simple_interest(principal, rate, time)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    print(f"Interest: {interest:.2f}")
    print(f"Total Amount: {total:.2f}")


def _run_tests() -> None:
    """Run a few quick sanity tests for the calculation."""
    cases = [
        # (principal, rate, time, expected_interest)
        (1000.0, 5.0, 1.0, 50.0),
        (2000.0, 3.5, 2.0, 140.0),
        (0.0, 10.0, 1.0, 0.0),
    ]
    for p, r, t, expected in cases:
        interest, total = calculate_simple_interest(p, r, t)
        assert abs(interest - expected) < 1e-9, f"Failed for {(p, r, t)}: got {interest}, expected {expected}"
        assert abs(total - (p + expected)) < 1e-9
    print("All tests passed.")


if __name__ == "__main__":
    main()
