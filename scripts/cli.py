import argparse

from ats_evaluator import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ATS Evaluator")
    parser.add_argument("--ref", type=str, required=True, help="Reference text")
    parser.add_argument("--simplified", type=str, required=True, help="Simplified text")
    args = parser.parse_args()

    ref_data, ref_stats, simplified_data, simplified_stats, comparison_data, comparison_stats = main.comparison(args.ref, args.simplified)

    print("Reference Data")
    print(ref_data)
    print("Reference Stats")
    print(ref_stats)
    print("Simplified Data")
    print(simplified_data)
    print("Simplified Stats")
    print(simplified_stats)
    print("Comparison Data")
    print(comparison_data)
    print("Comparison Stats")
    print(comparison_stats)
