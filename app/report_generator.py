import pandas as pd

def generate_report(mismatches_df, output_file='reconciliation_report.xlsx'):
    mismatches_df.to_excel(output_file, index=False)
