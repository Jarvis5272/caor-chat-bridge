<div style="overflow-x:auto;">
<h3 style="text-align:center;">Per-Dataset External Baseline Comparison (CAPPED_17_MATCHED)</h3>
<table style="border-collapse:collapse;font-size:12px;text-align:center;width:100%;background:#edf2f9;">
<thead><tr style="background:#c8d6e5;">
<th style="padding:5px 7px;border:1px solid #fff;">数据集</th>
<th style="padding:5px 7px;border:1px solid #fff;">算法</th>
<th style="padding:5px 7px;border:1px solid #fff;">Exact</th>
<th style="padding:5px 7px;border:1px solid #fff;">Accuracy</th>
<th style="padding:5px 7px;border:1px solid #fff;">ED</th>
<th style="padding:5px 7px;border:1px solid #fff;">Time/Cluster</th>
<th style="padding:5px 7px;border:1px solid #fff;">Runtime</th>
<th style="padding:5px 7px;border:1px solid #fff;">Prefix/s</th>
<th style="padding:5px 7px;border:1px solid #fff;">Raw reads/s</th>
<th style="padding:5px 7px;border:1px solid #fff;">Speedup vs BBS</th>
</tr></thead><tbody>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">binned_nanopore</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.2564</td>
<td style="padding:4px;border:1px solid #fff;">0.9719</td>
<td style="padding:4px;border:1px solid #fff;">3.9340</td>
<td style="padding:4px;border:1px solid #fff;">0.007940 s</td>
<td style="padding:4px;border:1px solid #fff;">7.9 s</td>
<td style="padding:4px;border:1px solid #fff;">698.00</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4058.70</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.03x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0973</td>
<td style="padding:4px;border:1px solid #fff;">0.9740</td>
<td style="padding:4px;border:1px solid #fff;">3.6359</td>
<td style="padding:4px;border:1px solid #fff;">0.055840 s</td>
<td style="padding:4px;border:1px solid #fff;">55.8 s</td>
<td style="padding:4px;border:1px solid #fff;">99.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0460</td>
<td style="padding:4px;border:1px solid #fff;">0.9391</td>
<td style="padding:4px;border:1px solid #fff;">8.5191</td>
<td style="padding:4px;border:1px solid #fff;">0.168580 s</td>
<td style="padding:4px;border:1px solid #fff;">168.6 s</td>
<td style="padding:4px;border:1px solid #fff;">32.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.33x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.2102</td>
<td style="padding:4px;border:1px solid #fff;">0.9531</td>
<td style="padding:4px;border:1px solid #fff;">6.5601</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.002990</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3.0</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1854.40</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>18.68</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0009</td>
<td style="padding:4px;border:1px solid #fff;">0.4685</td>
<td style="padding:4px;border:1px solid #fff;">74.4035</td>
<td style="padding:4px;border:1px solid #fff;">0.008730 s</td>
<td style="padding:4px;border:1px solid #fff;">8.7 s</td>
<td style="padding:4px;border:1px solid #fff;">634.50</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">6.40x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9823</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9993</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.1000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.333170 s</td>
<td style="padding:4px;border:1px solid #fff;">333.2 s</td>
<td style="padding:4px;border:1px solid #fff;">16.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.17x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;">0.9659</td>
<td style="padding:4px;border:1px solid #fff;">0.9992</td>
<td style="padding:4px;border:1px solid #fff;">0.1166</td>
<td style="padding:4px;border:1px solid #fff;">8.830452 s</td>
<td style="padding:4px;border:1px solid #fff;">8786.3 s</td>
<td style="padding:4px;border:1px solid #fff;">0.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.01x</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">clover</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.9510</td>
<td style="padding:4px;border:1px solid #fff;">0.9997</td>
<td style="padding:4px;border:1px solid #fff;">0.0522</td>
<td style="padding:4px;border:1px solid #fff;">0.010790 s</td>
<td style="padding:4px;border:1px solid #fff;">10.8 s</td>
<td style="padding:4px;border:1px solid #fff;">555.90</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3798.30</strong></td>
<td style="padding:4px;border:1px solid #fff;">4.03x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.3780</td>
<td style="padding:4px;border:1px solid #fff;">0.9958</td>
<td style="padding:4px;border:1px solid #fff;">0.6740</td>
<td style="padding:4px;border:1px solid #fff;">0.043490 s</td>
<td style="padding:4px;border:1px solid #fff;">43.5 s</td>
<td style="padding:4px;border:1px solid #fff;">138.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.7272</td>
<td style="padding:4px;border:1px solid #fff;">0.9978</td>
<td style="padding:4px;border:1px solid #fff;">0.3590</td>
<td style="padding:4px;border:1px solid #fff;">0.080650 s</td>
<td style="padding:4px;border:1px solid #fff;">80.7 s</td>
<td style="padding:4px;border:1px solid #fff;">74.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.54x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.9507</td>
<td style="padding:4px;border:1px solid #fff;">0.9997</td>
<td style="padding:4px;border:1px solid #fff;">0.0527</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.004780</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4.8</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1255.70</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>9.10</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.4539</td>
<td style="padding:4px;border:1px solid #fff;">87.3790</td>
<td style="padding:4px;border:1px solid #fff;">0.009900 s</td>
<td style="padding:4px;border:1px solid #fff;">9.9 s</td>
<td style="padding:4px;border:1px solid #fff;">606.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">4.39x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.462920 s</td>
<td style="padding:4px;border:1px solid #fff;">462.9 s</td>
<td style="padding:4px;border:1px solid #fff;">13.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.09x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">clover_clusters</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.9510</td>
<td style="padding:4px;border:1px solid #fff;">0.9997</td>
<td style="padding:4px;border:1px solid #fff;">0.0522</td>
<td style="padding:4px;border:1px solid #fff;">0.010870 s</td>
<td style="padding:4px;border:1px solid #fff;">10.9 s</td>
<td style="padding:4px;border:1px solid #fff;">552.20</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3773.30</strong></td>
<td style="padding:4px;border:1px solid #fff;">3.89x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.3780</td>
<td style="padding:4px;border:1px solid #fff;">0.9958</td>
<td style="padding:4px;border:1px solid #fff;">0.6740</td>
<td style="padding:4px;border:1px solid #fff;">0.042280 s</td>
<td style="padding:4px;border:1px solid #fff;">42.3 s</td>
<td style="padding:4px;border:1px solid #fff;">141.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.7272</td>
<td style="padding:4px;border:1px solid #fff;">0.9978</td>
<td style="padding:4px;border:1px solid #fff;">0.3590</td>
<td style="padding:4px;border:1px solid #fff;">0.080390 s</td>
<td style="padding:4px;border:1px solid #fff;">80.4 s</td>
<td style="padding:4px;border:1px solid #fff;">74.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.53x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.9507</td>
<td style="padding:4px;border:1px solid #fff;">0.9997</td>
<td style="padding:4px;border:1px solid #fff;">0.0527</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.004790</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4.8</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1251.80</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>8.83</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.4539</td>
<td style="padding:4px;border:1px solid #fff;">87.3790</td>
<td style="padding:4px;border:1px solid #fff;">0.010280 s</td>
<td style="padding:4px;border:1px solid #fff;">10.3 s</td>
<td style="padding:4px;border:1px solid #fff;">583.80</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">4.11x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.460540 s</td>
<td style="padding:4px;border:1px solid #fff;">460.5 s</td>
<td style="padding:4px;border:1px solid #fff;">13.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.09x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">microsoft_cnr</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.0956</td>
<td style="padding:4px;border:1px solid #fff;">0.9615</td>
<td style="padding:4px;border:1px solid #fff;">4.2300</td>
<td style="padding:4px;border:1px solid #fff;">0.006320 s</td>
<td style="padding:4px;border:1px solid #fff;">6.3 s</td>
<td style="padding:4px;border:1px solid #fff;">859.20</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4867.50</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.71x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0157</td>
<td style="padding:4px;border:1px solid #fff;">0.9540</td>
<td style="padding:4px;border:1px solid #fff;">5.0580</td>
<td style="padding:4px;border:1px solid #fff;">0.048740 s</td>
<td style="padding:4px;border:1px solid #fff;">48.7 s</td>
<td style="padding:4px;border:1px solid #fff;">111.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0070</td>
<td style="padding:4px;border:1px solid #fff;">0.9132</td>
<td style="padding:4px;border:1px solid #fff;">9.5471</td>
<td style="padding:4px;border:1px solid #fff;">0.157870 s</td>
<td style="padding:4px;border:1px solid #fff;">157.9 s</td>
<td style="padding:4px;border:1px solid #fff;">34.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.31x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.0247</td>
<td style="padding:4px;border:1px solid #fff;">0.9314</td>
<td style="padding:4px;border:1px solid #fff;">7.5413</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001940</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.9</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2797.40</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>25.12</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0007</td>
<td style="padding:4px;border:1px solid #fff;">0.4450</td>
<td style="padding:4px;border:1px solid #fff;">61.0517</td>
<td style="padding:4px;border:1px solid #fff;">0.005910 s</td>
<td style="padding:4px;border:1px solid #fff;">5.9 s</td>
<td style="padding:4px;border:1px solid #fff;">918.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">8.25x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9580</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9991</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0967</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.219890 s</td>
<td style="padding:4px;border:1px solid #fff;">219.9 s</td>
<td style="padding:4px;border:1px solid #fff;">24.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.22x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">nbt17_id20_m2m_top500</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.8692</td>
<td style="padding:4px;border:1px solid #fff;">0.9970</td>
<td style="padding:4px;border:1px solid #fff;">0.4556</td>
<td style="padding:4px;border:1px solid #fff;">0.005660 s</td>
<td style="padding:4px;border:1px solid #fff;">2.8 s</td>
<td style="padding:4px;border:1px solid #fff;">883.90</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3712.50</strong></td>
<td style="padding:4px;border:1px solid #fff;">5.13x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.7100</td>
<td style="padding:4px;border:1px solid #fff;">0.9965</td>
<td style="padding:4px;border:1px solid #fff;">0.5260</td>
<td style="padding:4px;border:1px solid #fff;">0.029040 s</td>
<td style="padding:4px;border:1px solid #fff;">14.5 s</td>
<td style="padding:4px;border:1px solid #fff;">172.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.7276</td>
<td style="padding:4px;border:1px solid #fff;">0.9951</td>
<td style="padding:4px;border:1px solid #fff;">0.7344</td>
<td style="padding:4px;border:1px solid #fff;">0.077080 s</td>
<td style="padding:4px;border:1px solid #fff;">38.5 s</td>
<td style="padding:4px;border:1px solid #fff;">64.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.38x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.8244</td>
<td style="padding:4px;border:1px solid #fff;">0.9949</td>
<td style="padding:4px;border:1px solid #fff;">0.7576</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.002820</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.4</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1776.20</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>10.30</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0020</td>
<td style="padding:4px;border:1px solid #fff;">0.6661</td>
<td style="padding:4px;border:1px solid #fff;">50.0860</td>
<td style="padding:4px;border:1px solid #fff;">0.007620 s</td>
<td style="padding:4px;border:1px solid #fff;">3.8 s</td>
<td style="padding:4px;border:1px solid #fff;">655.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">3.81x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.145000 s</td>
<td style="padding:4px;border:1px solid #fff;">72.5 s</td>
<td style="padding:4px;border:1px solid #fff;">34.50</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.20x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">nbt17_id20_m2m_top5000</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.8662</td>
<td style="padding:4px;border:1px solid #fff;">0.9971</td>
<td style="padding:4px;border:1px solid #fff;">0.4284</td>
<td style="padding:4px;border:1px solid #fff;">0.005690 s</td>
<td style="padding:4px;border:1px solid #fff;">5.7 s</td>
<td style="padding:4px;border:1px solid #fff;">879.20</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3692.60</strong></td>
<td style="padding:4px;border:1px solid #fff;">4.97x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.7090</td>
<td style="padding:4px;border:1px solid #fff;">0.9963</td>
<td style="padding:4px;border:1px solid #fff;">0.5490</td>
<td style="padding:4px;border:1px solid #fff;">0.028260 s</td>
<td style="padding:4px;border:1px solid #fff;">28.3 s</td>
<td style="padding:4px;border:1px solid #fff;">176.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.7360</td>
<td style="padding:4px;border:1px solid #fff;">0.9955</td>
<td style="padding:4px;border:1px solid #fff;">0.6788</td>
<td style="padding:4px;border:1px solid #fff;">0.079890 s</td>
<td style="padding:4px;border:1px solid #fff;">79.9 s</td>
<td style="padding:4px;border:1px solid #fff;">62.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.35x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.8290</td>
<td style="padding:4px;border:1px solid #fff;">0.9954</td>
<td style="padding:4px;border:1px solid #fff;">0.6968</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.002900</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2.9</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1722.80</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>9.74</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.6657</td>
<td style="padding:4px;border:1px solid #fff;">50.1520</td>
<td style="padding:4px;border:1px solid #fff;">0.007250 s</td>
<td style="padding:4px;border:1px solid #fff;">7.2 s</td>
<td style="padding:4px;border:1px solid #fff;">689.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">3.90x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.125060 s</td>
<td style="padding:4px;border:1px solid #fff;">125.1 s</td>
<td style="padding:4px;border:1px solid #fff;">40.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.23x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">nbt17_id20_m2m_top500_k15</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.8692</td>
<td style="padding:4px;border:1px solid #fff;">0.9970</td>
<td style="padding:4px;border:1px solid #fff;">0.4556</td>
<td style="padding:4px;border:1px solid #fff;">0.005660 s</td>
<td style="padding:4px;border:1px solid #fff;">2.8 s</td>
<td style="padding:4px;border:1px solid #fff;">884.10</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3713.30</strong></td>
<td style="padding:4px;border:1px solid #fff;">5.16x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.7100</td>
<td style="padding:4px;border:1px solid #fff;">0.9965</td>
<td style="padding:4px;border:1px solid #fff;">0.5260</td>
<td style="padding:4px;border:1px solid #fff;">0.029220 s</td>
<td style="padding:4px;border:1px solid #fff;">14.6 s</td>
<td style="padding:4px;border:1px solid #fff;">171.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.7276</td>
<td style="padding:4px;border:1px solid #fff;">0.9951</td>
<td style="padding:4px;border:1px solid #fff;">0.7344</td>
<td style="padding:4px;border:1px solid #fff;">0.076720 s</td>
<td style="padding:4px;border:1px solid #fff;">38.4 s</td>
<td style="padding:4px;border:1px solid #fff;">65.20</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.38x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.8244</td>
<td style="padding:4px;border:1px solid #fff;">0.9949</td>
<td style="padding:4px;border:1px solid #fff;">0.7576</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.002800</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.4</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1782.70</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>10.44</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0020</td>
<td style="padding:4px;border:1px solid #fff;">0.6661</td>
<td style="padding:4px;border:1px solid #fff;">50.0860</td>
<td style="padding:4px;border:1px solid #fff;">0.008180 s</td>
<td style="padding:4px;border:1px solid #fff;">4.1 s</td>
<td style="padding:4px;border:1px solid #fff;">611.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">3.57x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.145540 s</td>
<td style="padding:4px;border:1px solid #fff;">72.8 s</td>
<td style="padding:4px;border:1px solid #fff;">34.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.20x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">ncomms19_365_dishes_full_strict_clean</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.3268</td>
<td style="padding:4px;border:1px solid #fff;">0.9730</td>
<td style="padding:4px;border:1px solid #fff;">4.0567</td>
<td style="padding:4px;border:1px solid #fff;">0.009410 s</td>
<td style="padding:4px;border:1px solid #fff;">9.4 s</td>
<td style="padding:4px;border:1px solid #fff;">611.00</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3865.30</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.32x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0223</td>
<td style="padding:4px;border:1px solid #fff;">0.9586</td>
<td style="padding:4px;border:1px solid #fff;">6.2159</td>
<td style="padding:4px;border:1px solid #fff;">0.068890 s</td>
<td style="padding:4px;border:1px solid #fff;">68.9 s</td>
<td style="padding:4px;border:1px solid #fff;">83.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0505</td>
<td style="padding:4px;border:1px solid #fff;">0.8951</td>
<td style="padding:4px;border:1px solid #fff;">15.7355</td>
<td style="padding:4px;border:1px solid #fff;">0.239300 s</td>
<td style="padding:4px;border:1px solid #fff;">239.3 s</td>
<td style="padding:4px;border:1px solid #fff;">24.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.29x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.1620</td>
<td style="padding:4px;border:1px solid #fff;">0.9468</td>
<td style="padding:4px;border:1px solid #fff;">7.9798</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.002830</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2.8</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2029.50</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>24.34</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.6481</td>
<td style="padding:4px;border:1px solid #fff;">52.7877</td>
<td style="padding:4px;border:1px solid #fff;">0.012220 s</td>
<td style="padding:4px;border:1px solid #fff;">12.2 s</td>
<td style="padding:4px;border:1px solid #fff;">470.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">5.64x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9986</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9999</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0141</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.460280 s</td>
<td style="padding:4px;border:1px solid #fff;">460.3 s</td>
<td style="padding:4px;border:1px solid #fff;">12.50</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.15x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">ncomms19_space_shuttle_k15_min5</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.1821</td>
<td style="padding:4px;border:1px solid #fff;">0.9583</td>
<td style="padding:4px;border:1px solid #fff;">6.2576</td>
<td style="padding:4px;border:1px solid #fff;">0.003580 s</td>
<td style="padding:4px;border:1px solid #fff;">3.6 s</td>
<td style="padding:4px;border:1px solid #fff;">1135.30</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3251.60</strong></td>
<td style="padding:4px;border:1px solid #fff;">9.85x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.1693</td>
<td style="padding:4px;border:1px solid #fff;">0.9639</td>
<td style="padding:4px;border:1px solid #fff;">5.4181</td>
<td style="padding:4px;border:1px solid #fff;">0.035250 s</td>
<td style="padding:4px;border:1px solid #fff;">35.2 s</td>
<td style="padding:4px;border:1px solid #fff;">115.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0842</td>
<td style="padding:4px;border:1px solid #fff;">0.9444</td>
<td style="padding:4px;border:1px solid #fff;">8.3366</td>
<td style="padding:4px;border:1px solid #fff;">0.071420 s</td>
<td style="padding:4px;border:1px solid #fff;">71.4 s</td>
<td style="padding:4px;border:1px solid #fff;">56.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.49x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.1080</td>
<td style="padding:4px;border:1px solid #fff;">0.9457</td>
<td style="padding:4px;border:1px solid #fff;">8.1499</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001810</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.8</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2242.00</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>19.48</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.6664</td>
<td style="padding:4px;border:1px solid #fff;">50.0475</td>
<td style="padding:4px;border:1px solid #fff;">0.006230 s</td>
<td style="padding:4px;border:1px solid #fff;">6.2 s</td>
<td style="padding:4px;border:1px solid #fff;">651.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">5.66x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.7547</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9945</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.8182</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.042930 s</td>
<td style="padding:4px;border:1px solid #fff;">42.9 s</td>
<td style="padding:4px;border:1px solid #fff;">94.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.82x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">ncomms19_space_shuttle_min5</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.1821</td>
<td style="padding:4px;border:1px solid #fff;">0.9583</td>
<td style="padding:4px;border:1px solid #fff;">6.2576</td>
<td style="padding:4px;border:1px solid #fff;">0.003570 s</td>
<td style="padding:4px;border:1px solid #fff;">3.6 s</td>
<td style="padding:4px;border:1px solid #fff;">1138.50</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3260.70</strong></td>
<td style="padding:4px;border:1px solid #fff;">9.57x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.1693</td>
<td style="padding:4px;border:1px solid #fff;">0.9639</td>
<td style="padding:4px;border:1px solid #fff;">5.4181</td>
<td style="padding:4px;border:1px solid #fff;">0.034150 s</td>
<td style="padding:4px;border:1px solid #fff;">34.1 s</td>
<td style="padding:4px;border:1px solid #fff;">119.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0842</td>
<td style="padding:4px;border:1px solid #fff;">0.9444</td>
<td style="padding:4px;border:1px solid #fff;">8.3366</td>
<td style="padding:4px;border:1px solid #fff;">0.070780 s</td>
<td style="padding:4px;border:1px solid #fff;">70.8 s</td>
<td style="padding:4px;border:1px solid #fff;">57.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.48x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.1080</td>
<td style="padding:4px;border:1px solid #fff;">0.9457</td>
<td style="padding:4px;border:1px solid #fff;">8.1499</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001790</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.8</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2270.90</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>19.08</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.6664</td>
<td style="padding:4px;border:1px solid #fff;">50.0475</td>
<td style="padding:4px;border:1px solid #fff;">0.006280 s</td>
<td style="padding:4px;border:1px solid #fff;">6.3 s</td>
<td style="padding:4px;border:1px solid #fff;">646.80</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">5.44x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.7507</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9945</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.8290</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.043480 s</td>
<td style="padding:4px;border:1px solid #fff;">43.5 s</td>
<td style="padding:4px;border:1px solid #fff;">93.50</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.79x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">ncomms19_space_shuttle_min5_windowed</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.1992</td>
<td style="padding:4px;border:1px solid #fff;">0.9364</td>
<td style="padding:4px;border:1px solid #fff;">9.5392</td>
<td style="padding:4px;border:1px solid #fff;">0.003070 s</td>
<td style="padding:4px;border:1px solid #fff;">3.1 s</td>
<td style="padding:4px;border:1px solid #fff;">1230.90</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3284.20</strong></td>
<td style="padding:4px;border:1px solid #fff;">8.03x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.5951</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9757</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>3.6427</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.024640 s</td>
<td style="padding:4px;border:1px solid #fff;">24.6 s</td>
<td style="padding:4px;border:1px solid #fff;">153.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.1062</td>
<td style="padding:4px;border:1px solid #fff;">0.9217</td>
<td style="padding:4px;border:1px solid #fff;">11.7431</td>
<td style="padding:4px;border:1px solid #fff;">0.060720 s</td>
<td style="padding:4px;border:1px solid #fff;">60.7 s</td>
<td style="padding:4px;border:1px solid #fff;">62.20</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.41x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.1316</td>
<td style="padding:4px;border:1px solid #fff;">0.9158</td>
<td style="padding:4px;border:1px solid #fff;">12.6303</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001570</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.6</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2407.80</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>15.69</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0000</td>
<td style="padding:4px;border:1px solid #fff;">0.6637</td>
<td style="padding:4px;border:1px solid #fff;">50.4452</td>
<td style="padding:4px;border:1px solid #fff;">0.006120 s</td>
<td style="padding:4px;border:1px solid #fff;">6.1 s</td>
<td style="padding:4px;border:1px solid #fff;">616.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">4.03x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;">0.5752</td>
<td style="padding:4px;border:1px solid #fff;">0.9740</td>
<td style="padding:4px;border:1px solid #fff;">3.8962</td>
<td style="padding:4px;border:1px solid #fff;">0.036400 s</td>
<td style="padding:4px;border:1px solid #fff;">36.4 s</td>
<td style="padding:4px;border:1px solid #fff;">103.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.68x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">ncomms19_vitruvian_min5_windowed</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.2120</td>
<td style="padding:4px;border:1px solid #fff;">0.9424</td>
<td style="padding:4px;border:1px solid #fff;">8.6400</td>
<td style="padding:4px;border:1px solid #fff;">0.005110 s</td>
<td style="padding:4px;border:1px solid #fff;">5.1 s</td>
<td style="padding:4px;border:1px solid #fff;">904.50</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3649.00</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.43x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.8705</td>
<td style="padding:4px;border:1px solid #fff;">0.9943</td>
<td style="padding:4px;border:1px solid #fff;">0.8511</td>
<td style="padding:4px;border:1px solid #fff;">0.037970 s</td>
<td style="padding:4px;border:1px solid #fff;">38.0 s</td>
<td style="padding:4px;border:1px solid #fff;">121.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0582</td>
<td style="padding:4px;border:1px solid #fff;">0.8888</td>
<td style="padding:4px;border:1px solid #fff;">16.6768</td>
<td style="padding:4px;border:1px solid #fff;">0.139380 s</td>
<td style="padding:4px;border:1px solid #fff;">139.4 s</td>
<td style="padding:4px;border:1px solid #fff;">33.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.27x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.1247</td>
<td style="padding:4px;border:1px solid #fff;">0.8998</td>
<td style="padding:4px;border:1px solid #fff;">15.0249</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001910</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.9</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2423.10</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>19.88</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0011</td>
<td style="padding:4px;border:1px solid #fff;">0.6313</td>
<td style="padding:4px;border:1px solid #fff;">55.3115</td>
<td style="padding:4px;border:1px solid #fff;">0.008370 s</td>
<td style="padding:4px;border:1px solid #fff;">8.4 s</td>
<td style="padding:4px;border:1px solid #fff;">552.20</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">4.54x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.8889</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9944</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.8374</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.242790 s</td>
<td style="padding:4px;border:1px solid #fff;">242.8 s</td>
<td style="padding:4px;border:1px solid #fff;">19.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.16x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">oligo0</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.0046</td>
<td style="padding:4px;border:1px solid #fff;">0.9080</td>
<td style="padding:4px;border:1px solid #fff;">9.9322</td>
<td style="padding:4px;border:1px solid #fff;">0.007890 s</td>
<td style="padding:4px;border:1px solid #fff;">7.9 s</td>
<td style="padding:4px;border:1px solid #fff;">751.90</td>
<td style="padding:4px;border:1px solid #fff;"><strong>5034.50</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.10x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0000</td>
<td style="padding:4px;border:1px solid #fff;">0.9249</td>
<td style="padding:4px;border:1px solid #fff;">8.1079</td>
<td style="padding:4px;border:1px solid #fff;">0.056010 s</td>
<td style="padding:4px;border:1px solid #fff;">56.0 s</td>
<td style="padding:4px;border:1px solid #fff;">105.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0000</td>
<td style="padding:4px;border:1px solid #fff;">0.7818</td>
<td style="padding:4px;border:1px solid #fff;">23.5656</td>
<td style="padding:4px;border:1px solid #fff;">0.210720 s</td>
<td style="padding:4px;border:1px solid #fff;">210.7 s</td>
<td style="padding:4px;border:1px solid #fff;">28.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.27x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.0000</td>
<td style="padding:4px;border:1px solid #fff;">0.8547</td>
<td style="padding:4px;border:1px solid #fff;">15.6906</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001790</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.8</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3306.20</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>31.29</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0000</td>
<td style="padding:4px;border:1px solid #fff;">0.4460</td>
<td style="padding:4px;border:1px solid #fff;">59.8344</td>
<td style="padding:4px;border:1px solid #fff;">0.008380 s</td>
<td style="padding:4px;border:1px solid #fff;">8.4 s</td>
<td style="padding:4px;border:1px solid #fff;">707.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">6.68x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.7138</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9942</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.6297</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.429090 s</td>
<td style="padding:4px;border:1px solid #fff;">429.1 s</td>
<td style="padding:4px;border:1px solid #fff;">13.80</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.13x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">trellisbma_datatoprocess_sim</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.0068</td>
<td style="padding:4px;border:1px solid #fff;">0.9541</td>
<td style="padding:4px;border:1px solid #fff;">5.0442</td>
<td style="padding:4px;border:1px solid #fff;">0.004720 s</td>
<td style="padding:4px;border:1px solid #fff;">4.7 s</td>
<td style="padding:4px;border:1px solid #fff;">1058.90</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4447.50</strong></td>
<td style="padding:4px;border:1px solid #fff;">9.03x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0020</td>
<td style="padding:4px;border:1px solid #fff;">0.9506</td>
<td style="padding:4px;border:1px solid #fff;">5.4390</td>
<td style="padding:4px;border:1px solid #fff;">0.042620 s</td>
<td style="padding:4px;border:1px solid #fff;">42.6 s</td>
<td style="padding:4px;border:1px solid #fff;">117.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0002</td>
<td style="padding:4px;border:1px solid #fff;">0.9234</td>
<td style="padding:4px;border:1px solid #fff;">8.4298</td>
<td style="padding:4px;border:1px solid #fff;">0.119020 s</td>
<td style="padding:4px;border:1px solid #fff;">119.0 s</td>
<td style="padding:4px;border:1px solid #fff;">42.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.36x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.0024</td>
<td style="padding:4px;border:1px solid #fff;">0.9305</td>
<td style="padding:4px;border:1px solid #fff;">7.6462</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001560</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.6</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>3197.30</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>27.32</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0010</td>
<td style="padding:4px;border:1px solid #fff;">0.5554</td>
<td style="padding:4px;border:1px solid #fff;">48.9090</td>
<td style="padding:4px;border:1px solid #fff;">0.004410 s</td>
<td style="padding:4px;border:1px solid #fff;">4.4 s</td>
<td style="padding:4px;border:1px solid #fff;">1135.10</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">9.66x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0000</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.081510 s</td>
<td style="padding:4px;border:1px solid #fff;">81.5 s</td>
<td style="padding:4px;border:1px solid #fff;">61.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.52x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">uploaded_compact</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.0956</td>
<td style="padding:4px;border:1px solid #fff;">0.9615</td>
<td style="padding:4px;border:1px solid #fff;">4.2300</td>
<td style="padding:4px;border:1px solid #fff;">0.006320 s</td>
<td style="padding:4px;border:1px solid #fff;">6.3 s</td>
<td style="padding:4px;border:1px solid #fff;">859.50</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4869.00</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.52x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0157</td>
<td style="padding:4px;border:1px solid #fff;">0.9540</td>
<td style="padding:4px;border:1px solid #fff;">5.0580</td>
<td style="padding:4px;border:1px solid #fff;">0.047520 s</td>
<td style="padding:4px;border:1px solid #fff;">47.5 s</td>
<td style="padding:4px;border:1px solid #fff;">114.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0070</td>
<td style="padding:4px;border:1px solid #fff;">0.9132</td>
<td style="padding:4px;border:1px solid #fff;">9.5471</td>
<td style="padding:4px;border:1px solid #fff;">0.160850 s</td>
<td style="padding:4px;border:1px solid #fff;">160.8 s</td>
<td style="padding:4px;border:1px solid #fff;">33.80</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.30x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.0247</td>
<td style="padding:4px;border:1px solid #fff;">0.9314</td>
<td style="padding:4px;border:1px solid #fff;">7.5413</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001880</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.9</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2892.80</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>25.28</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0007</td>
<td style="padding:4px;border:1px solid #fff;">0.4450</td>
<td style="padding:4px;border:1px solid #fff;">61.0517</td>
<td style="padding:4px;border:1px solid #fff;">0.005980 s</td>
<td style="padding:4px;border:1px solid #fff;">6.0 s</td>
<td style="padding:4px;border:1px solid #fff;">908.30</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">7.95x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9562</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9991</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0989</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.219400 s</td>
<td style="padding:4px;border:1px solid #fff;">219.4 s</td>
<td style="padding:4px;border:1px solid #fff;">24.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.22x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">uploaded_real_clusters</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.0956</td>
<td style="padding:4px;border:1px solid #fff;">0.9615</td>
<td style="padding:4px;border:1px solid #fff;">4.2300</td>
<td style="padding:4px;border:1px solid #fff;">0.006280 s</td>
<td style="padding:4px;border:1px solid #fff;">6.3 s</td>
<td style="padding:4px;border:1px solid #fff;">864.20</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4895.90</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.04x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0157</td>
<td style="padding:4px;border:1px solid #fff;">0.9540</td>
<td style="padding:4px;border:1px solid #fff;">5.0580</td>
<td style="padding:4px;border:1px solid #fff;">0.044200 s</td>
<td style="padding:4px;border:1px solid #fff;">44.2 s</td>
<td style="padding:4px;border:1px solid #fff;">122.80</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0070</td>
<td style="padding:4px;border:1px solid #fff;">0.9132</td>
<td style="padding:4px;border:1px solid #fff;">9.5471</td>
<td style="padding:4px;border:1px solid #fff;">0.159650 s</td>
<td style="padding:4px;border:1px solid #fff;">159.7 s</td>
<td style="padding:4px;border:1px solid #fff;">34.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.28x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.0247</td>
<td style="padding:4px;border:1px solid #fff;">0.9314</td>
<td style="padding:4px;border:1px solid #fff;">7.5413</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001900</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.9</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2850.80</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>23.26</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0007</td>
<td style="padding:4px;border:1px solid #fff;">0.4450</td>
<td style="padding:4px;border:1px solid #fff;">61.0517</td>
<td style="padding:4px;border:1px solid #fff;">0.005970 s</td>
<td style="padding:4px;border:1px solid #fff;">6.0 s</td>
<td style="padding:4px;border:1px solid #fff;">909.90</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">7.40x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9576</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9991</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0991</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.219700 s</td>
<td style="padding:4px;border:1px solid #fff;">219.7 s</td>
<td style="padding:4px;border:1px solid #fff;">24.70</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.20x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
<tr style="background:#f7f9fc;">
<td rowspan="7" style="vertical-align:middle;padding:4px;border:1px solid #fff;background:#dce6f0;font-weight:bold;">uploaded_real_clusters_compact</td>
<td style="padding:4px;border:1px solid #fff;text-align:left;">当前方法</td>
<td style="padding:4px;border:1px solid #fff;">0.0956</td>
<td style="padding:4px;border:1px solid #fff;">0.9615</td>
<td style="padding:4px;border:1px solid #fff;">4.2300</td>
<td style="padding:4px;border:1px solid #fff;">0.006330 s</td>
<td style="padding:4px;border:1px solid #fff;">6.3 s</td>
<td style="padding:4px;border:1px solid #fff;">857.50</td>
<td style="padding:4px;border:1px solid #fff;"><strong>4857.70</strong></td>
<td style="padding:4px;border:1px solid #fff;">7.15x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BBS</td>
<td style="padding:4px;border:1px solid #fff;">0.0157</td>
<td style="padding:4px;border:1px solid #fff;">0.9540</td>
<td style="padding:4px;border:1px solid #fff;">5.0580</td>
<td style="padding:4px;border:1px solid #fff;">0.045270 s</td>
<td style="padding:4px;border:1px solid #fff;">45.3 s</td>
<td style="padding:4px;border:1px solid #fff;">120.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">1.00x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">MUSCLE</td>
<td style="padding:4px;border:1px solid #fff;">0.0070</td>
<td style="padding:4px;border:1px solid #fff;">0.9132</td>
<td style="padding:4px;border:1px solid #fff;">9.5471</td>
<td style="padding:4px;border:1px solid #fff;">0.159590 s</td>
<td style="padding:4px;border:1px solid #fff;">159.6 s</td>
<td style="padding:4px;border:1px solid #fff;">34.00</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.28x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">VS</td>
<td style="padding:4px;border:1px solid #fff;">0.0247</td>
<td style="padding:4px;border:1px solid #fff;">0.9314</td>
<td style="padding:4px;border:1px solid #fff;">7.5413</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.001860</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>1.9</strong> s</td>
<td style="padding:4px;border:1px solid #fff;"><strong>2912.00</strong></td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;"><strong>24.34</strong>x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">BMALA</td>
<td style="padding:4px;border:1px solid #fff;">0.0007</td>
<td style="padding:4px;border:1px solid #fff;">0.4450</td>
<td style="padding:4px;border:1px solid #fff;">61.0517</td>
<td style="padding:4px;border:1px solid #fff;">0.005950 s</td>
<td style="padding:4px;border:1px solid #fff;">6.0 s</td>
<td style="padding:4px;border:1px solid #fff;">912.40</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">7.61x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">CPL</td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9595</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.9991</strong></td>
<td style="padding:4px;border:1px solid #fff;"><strong>0.0959</strong></td>
<td style="padding:4px;border:1px solid #fff;">0.220780 s</td>
<td style="padding:4px;border:1px solid #fff;">220.8 s</td>
<td style="padding:4px;border:1px solid #fff;">24.60</td>
<td style="padding:4px;border:1px solid #fff;">—</td>
<td style="padding:4px;border:1px solid #fff;">0.21x</td>
</tr>
<tr style="background:#ffffff;">
<td style="padding:4px;border:1px solid #fff;text-align:left;">ITR</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
<td style="padding:4px;border:1px solid #fff;color:#999;">—</td>
</tr>
</tbody></table>
<p style="font-size:10px;color:#888;">CAPPED_17_MATCHED scope. Bold = best within each dataset-metric. Time/Cluster in s. ITR pending.</p>
</div>