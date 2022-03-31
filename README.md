1. Run "Split Training and Testing Query.ipynb" in "AOL_clean".

2. Run "Query Log Processing.ipynb" and then "Reduce Gram and Get Statistic.ipynb" in 
"Training Part" and "Testing Part", respectively.

3. Run "Intersect Gram.ipynb" and then run "Add_query_index_filter_not_occur_continuous_id.ipynb"
in "Intersection Gram".

4. Run "Generate First Layer Index.ipynb" in "Intersection Gram/query log for PISA".

5. Finally, run "Compute Two-Layer Hit Ratio Choose Top 10.ipynb" (treat every gram the same.)
   or run "Compute Two-Layer Hit Ratio Choose Top 10 Longer Gram Prior.ipynb" (priority for
   longer gram).