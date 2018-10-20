#!/bin/bash

bold=$(tput bold)
normal=$(tput sgr0)

./gen_stat_input_files.py
./gen_stats.py > best_configs.txt

# The depreciated statistical analysis method uses the following commands:
# ./gen_stats.py > stats.txt
# ./gen_tables.py
# echo "Statistical analysis (in LaTeX table form): ${bold}stats_tables.txt${normal}"

