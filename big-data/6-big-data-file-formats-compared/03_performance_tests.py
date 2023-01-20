# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:48:18 2023

@author: Pablo Aguirre

GitHub: https://github.com/pabloaguirrenck
Website: https://pabloagn.com
Contact: https://pabloagn.com/contact

Part of Blog Article: 6-big-data-file-formats-compared
"""





import pyarrow.feather as feather
import pyarrow.parquet as pq
import fastparquet as fp
import timeit


df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]})

print("pandas df to disk ####################################################")
print('example_feather:')
%timeit feather.write_feather(df, 'example_feather')
# 2.62 ms ± 35.8 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
print('example_parquet:')
%timeit pq.write_table(pa.Table.from_pandas(df), 'example.parquet')
# 3.19 ms ± 51 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
print()

print("for comparison:")
print('example_pickle:')
%timeit df.to_pickle('example_pickle')
# 2.75 ms ± 18.8 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
print('example_fp_parquet:')
%timeit fp.write('example_fp_parquet', df)
# 7.06 ms ± 205 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
print('example_hdf:')
%timeit df.to_hdf('example_hdf', 'key_to_store', mode='w', table=True)
# 24.6 ms ± 4.45 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
print()

print("pandas df from disk ##################################################")
print('example_feather:')
%timeit feather.read_feather('example_feather')
# 969 µs ± 1.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
print('example_parquet:')
%timeit pq.read_table('example.parquet').to_pandas()
# 1.9 ms ± 5.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

print("for comparison:")
print('example_pickle:')
%timeit pd.read_pickle('example_pickle')
# 1.07 ms ± 6.21 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
print('example_fp_parquet:')
%timeit fp.ParquetFile('example_fp_parquet').to_pandas()
# 4.53 ms ± 260 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
print('example_hdf:')
%timeit pd.read_hdf('example_hdf')
# 10 ms ± 43.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

# pandas version: 0.22.0
# fastparquet version: 0.1.3
# numpy version: 1.13.3
# pandas version: 0.22.0
# pyarrow version: 0.8.0
# sys.version: 3.6.3
# example Dataframe taken from https://arrow.apache.org/docs/python/parquet.html