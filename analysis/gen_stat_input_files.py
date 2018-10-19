#!/usr/bin/env python3

import analysis_config as config

BEST_INVERSE_CONSTR = 2

for i in range(len(config.log_file_paths)):
    with open(config.log_file_paths[i], 'r') as log_file:
        # Create a list of lines from the log file, disregarding all config parameters and empty lines
        log_text = log_file.read().split('\n')
        log_text = [line for line in log_text[log_text.index('Run 1'):] if not line == '']

        last_best_ratios = []
        all_best_ratios = []
        last_best_bulb_constrs = []
        all_best_bulb_constrs = []
        last_best_black_constrs = []
        all_best_black_constrs = []

        prev_run_count = 1

        # Scrape average fitness data from the log file
        for line in log_text:
            if line[0] == 'R':
                curr_run_count = int(line.split()[1])
                if not prev_run_count == curr_run_count:
                    last_best_ratios.append(float(all_best_ratios[-1]))
                    last_best_bulb_constrs.append(float(all_best_bulb_constrs[-1]))
                    last_best_black_constrs.append(float(all_best_black_constrs[-1]))
                    prev_run_count = curr_run_count

            else:
                # This line has eval and fitness data
                line = line.split('\t')

                # Append the best ratio
                all_best_ratios.append(line[2])

                # Append the inverse of the constraints violated to ensure a maximization problem
                if float(line[4]) == 0.0:
                    all_best_bulb_constrs.append(BEST_INVERSE_CONSTR)
                else:
                    all_best_bulb_constrs.append(1 / float(line[4]))
                    
                if float(line[6]) == 0.0:
                    all_best_black_constrs.append(BEST_INVERSE_CONSTR)
                else:
                    all_best_black_constrs.append(1 / float(line[6]))

        last_best_ratios.append(float(all_best_ratios[-1]))
        last_best_bulb_constrs.append(float(all_best_bulb_constrs[-1]))
        last_best_black_constrs.append(float(all_best_black_constrs[-1]))
        
    # Write the last (local) best subfitnesses (listed below) to three separate files
    # 1: best ratios
    # 2: best bulb constraints
    # 3: best black cell constraints
    with open(config.log_file_paths[i][:config.log_file_paths[i].find('log')] + 'last_best_local_ratios.txt', 'w') as out:
        for k in range(len(last_best_ratios)):
            out.write(str(last_best_ratios[k]) + '\n')

    with open(config.log_file_paths[i][:config.log_file_paths[i].find('log')] + 'last_best_local_bulb_constrs.txt', 'w') as out:
        for k in range(len(last_best_ratios)):
            out.write(str(last_best_bulb_constrs[k]) + '\n')

    with open(config.log_file_paths[i][:config.log_file_paths[i].find('log')] + 'last_best_local_black_constrs.txt', 'w') as out:
        for k in range(len(last_best_ratios)):
            out.write(str(last_best_black_constrs[k]) + '\n')

