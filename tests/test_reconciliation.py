import pandas as pd
from app.reconciliation import reconcile_data

def test_reconcile_data():
    df1 = pd.DataFrame({'ID': [1, 2, 3], 'Amount': [100, 200, 300]})
    df2 = pd.DataFrame({'ID': [1, 2, 4], 'Amount': [100, 200, 400]})

    mismatches = reconcile_data(df1, df2, key_columns=['ID'])
    assert not mismatches.empty
