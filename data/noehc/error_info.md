# SuPy Error Report

## Timestamp
2025-02-24T13:35:23.005660

## Error Type
`KeyError`

## Error Message
```shell
'n_buildings'
```

## Traceback
```python
  File "c:\Users\xbacos\miniconda3\envs\supy_env\Lib\site-packages\supy\_run.py", line 399, in run_supy_ser
    suews_cal_tstep_multi(dict_state_input, df_forcing, debug_mode)
  File "c:\Users\xbacos\miniconda3\envs\supy_env\Lib\site-packages\supy\_run.py", line 151, in suews_cal_tstep_multi
    dict_input = {k: dict_input[k] for k in list_var_input_multitsteps}
                     ~~~~~~~~~~^^^
```
