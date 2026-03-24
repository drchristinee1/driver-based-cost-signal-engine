import argparse
from drivers.detector import run_driver_detection
from drivers.action_mapper import generate_actions


def main():
    parser = argparse.ArgumentParser(
        description="Driver-Based Cost Signal Engine CLI"
    )

    subparsers = parser.add_subparsers(dest="module")

    # drivers module
    drivers_parser = subparsers.add_parser("drivers", help="Driver-based operations")
    drivers_subparsers = drivers_parser.add_subparsers(dest="action")

    # detect command
    detect_parser = drivers_subparsers.add_parser(
        "detect",
        help="Run driver-based detection"
    )
    detect_parser.add_argument(
        "--service",
        default="all",
        help="Optional service filter, e.g. lambda, ec2"
    )

    # actions command
    drivers_subparsers.add_parser(
        "actions",
        help="Generate actions from detected driver alerts"
    )

    args = parser.parse_args()

    if args.module == "drivers" and args.action == "detect":
        run_driver_detection(service=args.service)

    elif args.module == "drivers" and args.action == "actions":
        generate_actions()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
