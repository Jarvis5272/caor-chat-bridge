<div style="overflow-x:auto;">
<h3 style="text-align:center;">Table PART2: Datasets 7–12</h3>
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
</tbody></table>
<p style="font-size:10px;color:#888;">CAPPED_17_MATCHED scope. Bold=best within dataset-metric. * = ITR partial (2/17 datasets). ITR failed on 15/17 datasets.</p>
</div>