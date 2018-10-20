log_file_paths = [
                    'random_gen/random_gen',
                    'random_gen/random_gen_uniform_random_init',
                    'random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__comma_',
                    'random_gen/random_gen__tournament_parent__fitness_proportional_survival__comma_',
                    'random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__plus_',
                    'random_gen/random_gen__tournament_parent__fitness_proportional_survival__plus_',
                    'random_gen/random_gen__fitness_proportional_parent__tournament_survival__comma_',
                    'random_gen/random_gen__tournament_parent__tournament_survival__comma_',
                    'random_gen/random_gen__fitness_proportional_parent__tournament_survival__plus_',
                    'random_gen/random_gen__tournament_parent__tournament_survival__plus_',

                    'website_puzzle/website_puzzle',
                    'website_puzzle/website_puzzle_uniform_random_init',
                    'website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__comma_',
                    'website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__comma_',
                    'website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__plus_',
                    'website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__plus_',
                    'website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__comma_',
                    'website_puzzle/website_puzzle__tournament_parent__tournament_survival__comma_',
                    'website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__plus_',
                    'website_puzzle/website_puzzle__tournament_parent__tournament_survival__plus_'
                 ]


log_file_paths = ['../output/' + filename + '_log.txt' for filename in log_file_paths]


# In-depth EA comparison stats data files

random_gen_test_cases = \
    [
        ('../output/random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__comma__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__comma__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__plus__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__fitness_proportional_survival__plus__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__fitness_proportional_parent__tournament_survival__comma__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__tournament_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__tournament_survival__comma__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__fitness_proportional_parent__tournament_survival__plus__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__tournament_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__fitness_proportional_parent__tournament_survival__plus__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__tournament_parent__fitness_proportional_survival__comma__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__fitness_proportional_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__fitness_proportional_survival__comma__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__tournament_parent__fitness_proportional_survival__plus__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__fitness_proportional_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__fitness_proportional_survival__plus__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__tournament_parent__tournament_survival__comma__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__tournament_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__tournament_survival__comma__last_best_local_ratios.txt'),

        ('../output/random_gen/random_gen__tournament_parent__tournament_survival__plus__last_best_local_black_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__tournament_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/random_gen/random_gen__tournament_parent__tournament_survival__plus__last_best_local_ratios.txt')
    ]


website_puzzle_test_cases = \
    [
        ('../output/website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__comma__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__comma__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__plus__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__fitness_proportional_survival__plus__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__comma__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__comma__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__plus__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__fitness_proportional_parent__tournament_survival__plus__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__comma__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__comma__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__plus__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__fitness_proportional_survival__plus__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__tournament_parent__tournament_survival__comma__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__tournament_survival__comma__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__tournament_survival__comma__last_best_local_ratios.txt'),

        ('../output/website_puzzle/website_puzzle__tournament_parent__tournament_survival__plus__last_best_local_black_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__tournament_survival__plus__last_best_local_bulb_constrs.txt',
        '../output/website_puzzle/website_puzzle__tournament_parent__tournament_survival__plus__last_best_local_ratios.txt')
    ]


# Initialization stats data files

test_cases = \
    [
        (
            '../output/random_gen/random_gen_last_best_local_fits.txt',
            '../output/random_gen/random_gen_uniform_random_init_last_best_local_fits.txt'
        ),
        (
            '../output/website_puzzle/website_puzzle_last_best_local_fits.txt',
            '../output/website_puzzle/website_puzzle_uniform_random_init_last_best_local_fits.txt'
        )
    ]


# t-critical two tailed table for CI = 95% (alpha = 0.05)
# List with index representing df, value representing t-critical
t_table = \
    [
        0,
        0,
        4.3027,
        3.1824,
        2.7765,
        2.5706,
        2.4469,
        2.3646,
        2.3060,
        2.2622,
        2.2281,
        2.2010,
        2.1788,
        2.1604,
        2.1448,
        2.1315,
        2.1199,
        2.1098,
        2.1009,
        2.0930,
        2.0860,
        2.0796,
        2.0739,
        2.0687,
        2.0639,
        2.0595,
        2.0555,
        2.0518,
        2.0484,
        2.0452,
        2.0423,
        2.0395,
        2.0369,
        2.0345,
        2.0322,
        2.0301,
        2.0281,
        2.0262,
        2.0244,
        2.0227,
        2.0211,
        2.0195,
        2.0181,
        2.0167,
        2.0154,
        2.0141,
        2.0129,
        2.0117,
        2.0106,
        2.0096,
        2.0086,
        2.0076,
        2.0066,
        2.0057,
        2.0049,
        2.0040,
        2.0032,
        2.0025,
        2.0017,
        2.0010,
        2.0003,
        1.9996,
        1.9990,
        1.9983,
        1.9977,
        1.9971,
        1.9966,
        1.9960,
        1.9955,
        1.9949,
        1.9944,
        1.9939,
        1.9935,
        1.9930,
        1.9925,
        1.9921,
        1.9917,
        1.9913,
        1.9908,
        1.9905,
        1.9901,
        1.9897,
        1.9893,
        1.9890,
        1.9886,
        1.9883,
        1.9879,
        1.9876,
        1.9873,
        1.9870,
        1.9867,
        1.9864,
        1.9861,
        1.9858,
        1.9855,
        1.9852,
        1.9850,
        1.9847,
        1.9845,
        1.9842,
        1.9840
    ]
