<div style="overflow-x:auto;">
<h3 style="text-align:center;">Table PART1: Datasets 1–6</h3>
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
</tbody></table>
<p style="font-size:10px;color:#888;">CAPPED_17_MATCHED scope. Bold = best within each dataset-metric. Time/Cluster in s. ITR pending.</p>
</div>