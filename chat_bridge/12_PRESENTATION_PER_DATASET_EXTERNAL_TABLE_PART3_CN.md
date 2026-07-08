<div style="overflow-x:auto;">
<h3 style="text-align:center;">Table PART3: Datasets 13–17</h3>
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
<p style="font-size:10px;color:#888;">CAPPED_17_MATCHED scope. Bold=best within dataset-metric. * = ITR partial (2/17 datasets). ITR failed on 15/17 datasets.</p>
</div>