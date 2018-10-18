#!/usr/bin/env python3

import analysis_config as config
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


for q in range(len(config.log_file_paths)):
    with open(config.log_file_paths[q], 'r') as log_file:
        # Create a list of lines from the log file, disregarding all config parameters and empty lines
        log_file = log_file.read().split('\n')
        log_file = [line for line in log_file[log_file.index('Run 1'):] if not line == '']


        # key: evaluation number, value: [average fitness, local best fitness]
        eval_dict = {}

        curr_run = 1

        # Scrape data from the log file
        max_num_evals = 0
        for line in log_file:
            if not line[0] == 'R':
                # This line has data
                eval_num, avg_shine_ratio, best_shine_ratio, avg_bulb_constr, best_bulb_constr, \
                    avg_black_cell_constr, best_black_cell_constr = line.split('\t')

                eval_num = int(eval_num)
                avg_shine_ratio = float(avg_shine_ratio)
                best_shine_ratio = float(best_shine_ratio)
                avg_bulb_constr = float(avg_bulb_constr)
                best_bulb_constr = int(best_bulb_constr)
                avg_black_cell_constr = float(avg_black_cell_constr)
                best_black_cell_constr = int(best_black_cell_constr)

                if eval_num in eval_dict:
                    eval_dict[eval_num][0] += avg_shine_ratio
                    eval_dict[eval_num][1] += best_shine_ratio
                    eval_dict[eval_num][2] += avg_bulb_constr
                    eval_dict[eval_num][3] += best_bulb_constr
                    eval_dict[eval_num][4] += avg_black_cell_constr
                    eval_dict[eval_num][5] += best_black_cell_constr
                    eval_dict[eval_num][6] += 1
                else:
                    eval_dict[eval_num] = [avg_shine_ratio, best_shine_ratio, avg_bulb_constr,
                        best_bulb_constr, avg_black_cell_constr, best_black_cell_constr, 1]
                
                max_num_evals = max(eval_dict[eval_num][6], max_num_evals)

        evals = []
        avg_shine_ratios = []
        best_shine_ratios = []
        avg_bulb_constrs = []
        best_bulb_constrs = []
        avg_black_cell_constrs = []
        best_black_cell_constrs = []

        for eval_num in sorted(eval_dict.keys()):
            evals.append(eval_num)
            avg_shine_ratios.append(eval_dict[eval_num][0] / eval_dict[eval_num][6])
            best_shine_ratios.append(eval_dict[eval_num][1] / eval_dict[eval_num][6])
            avg_bulb_constrs.append(eval_dict[eval_num][2] / eval_dict[eval_num][6])
            best_bulb_constrs.append(eval_dict[eval_num][3] / eval_dict[eval_num][6])
            avg_black_cell_constrs.append(eval_dict[eval_num][4] / eval_dict[eval_num][6])
            best_black_cell_constrs.append(eval_dict[eval_num][5] / eval_dict[eval_num][6])


        # Configure graphing data
        if 'web' in config.log_file_paths[q]:
            black_cell_constr_y_lim = 40 
        else:
            black_cell_constr_y_lim = 10

        plot_data = \
            [
                (avg_shine_ratios, best_shine_ratios, "Lit Cell Ratio", "lit_cell_ratio", 1), 
                (avg_bulb_constrs, best_bulb_constrs, 
                    "Number of Bulb Shine Constraints Violated", "bulb_shine_constr", 2),
                (avg_black_cell_constrs, best_black_cell_constrs, 
                    "Number of Black Cell Constraints Violated", "black_cell_constr", 
                    black_cell_constr_y_lim)
            ]

        # Plot the results
        for plot_datum in plot_data:

            fig, ax = plt.subplots()

            ax.step(evals[:len(plot_datum[0])], plot_datum[0], '-r')
            ax.step(evals[:len(plot_datum[1])], plot_datum[1], '-b')
    
            plt.ylim(0, plot_datum[4])
    
            red_patch = mpatches.Patch(color='red', label='Average Local ' + plot_datum[2])
            blue_patch = mpatches.Patch(color='blue', label='Local Best ' + plot_datum[2])
            plt.legend(handles=[blue_patch, red_patch])
    
            # Include necessary labels
            plt.xlabel('Evaluations')
            plt.ylabel(plot_datum[2])
    
    
            # Save and close the plot
            plt.savefig(config.log_file_paths[q][:config.log_file_paths[q].find('log')] + 
                plot_datum[3] + '__graph.png')
            plt.close()

