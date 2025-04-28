from utils import load_data
from reconciliation import reconcile_data
from report_generator import generate_report

def main():
    df1 = load_data('sample_data/source1.csv')
    df2 = load_data('sample_data/source2.csv')

    mismatches = reconcile_data(df1, df2, key_columns=['ID'])  # assuming 'ID' is the key
    generate_report(mismatches)

    print(f"Reconciliation complete. Report generated.")

if __name__ == "__main__":
    main()
