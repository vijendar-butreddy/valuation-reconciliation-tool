def reconcile_data(df1, df2, key_columns):
    """
    Compare two dataframes based on given key columns.
    Returns mismatched rows.
    """
    merged = df1.merge(df2, on=key_columns, suffixes=('_src1', '_src2'), how='outer', indicator=True)
    mismatches = merged[merged['_merge'] != 'both']
    return mismatches
