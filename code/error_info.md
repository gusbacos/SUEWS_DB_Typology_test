# SuPy Error Report

## Timestamp
2025-01-22T13:05:45.471723

## Error Type
`KeyError`

## Error Message
```shell
'faimethod'
```

## Traceback
```python
  File "c:\Users\xbacos\miniconda3\envs\supy_env\Lib\site-packages\supy\_run.py", line 398, in run_supy_ser
    suews_cal_tstep_multi(dict_state_input, df_forcing, debug_mode)
  File "c:\Users\xbacos\miniconda3\envs\supy_env\Lib\site-packages\supy\_run.py", line 150, in suews_cal_tstep_multi
    dict_input = {k: dict_input[k] for k in list_var_input_multitsteps}
                     ~~~~~~~~~~^^^
```
