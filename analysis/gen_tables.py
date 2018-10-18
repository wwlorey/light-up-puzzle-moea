#!/usr/bin/env python3

# '+' indicates index at which to place tabular data
table_template = r'\begin{table}[] \
\tablecaption{TODO caption}        \
\label{TODO label}                 \
\resizebox{\textwidth}{!}{%        \
\begin{tabular}{|l|l|l|}           \
\hline               \
  & + & +  \\ \hline \
 + & + & + \\ \hline \
 + & + & + \\ \hline \
 + & + & + \\ \hline \
 + & + & + \\ \hline \
 + & + & + \\ \hline \
 + & + &   \\ \hline \
 + & + &   \\ \hline \
 + &  &    \\ \hline \
  &  &     \\ \hline \
  + & + &  \\ \hline \
  + & + &  \\ \hline \
  + & + &  \\ \hline \
  + & + &  \\ \hline \
  + & + &  \\ \hline \
  + &  &   \\ \hline \
  \end{tabular}%     \
}                    \
\end{table} '

# Remove backslashes from table_template
table_template = '\n'.join([line[:-1] for line in table_template.split('\n')])
                    
with open('stats.txt', 'r') as f:
    results = f.read().split('\n\n\n')[:-1]

    with open('stats_tables.txt', 'w') as output_f:
        for raw_result in results:
            splits = raw_result.split('\n')

#            for split in splits:
#                split += ','

            result = []

            for split in splits:
                result += [item.strip() for item in split.split(',')]

            while True:
                if not result[0]:
                    result = result[1:]
                else:
                    break

            result = [item for item in result if item]

            output_table = table_template

            result_index = 0

            next_insertion_index = output_table.find('+')
            while next_insertion_index >= 0:
                output_table = output_table[:next_insertion_index] + result[result_index] + \
                    output_table[next_insertion_index + 1:]
                
                result_index += 1
                next_insertion_index = output_table.find('+')

            output_f.write(output_table.replace('_', r'\_'))
            output_f.write('\n\n')
