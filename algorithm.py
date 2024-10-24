import numpy as np
import time

            

def original_alignment(sequences, k):
    start_time = time.time()
    divided_sequences = [sequences[i:i+k] for i in range(0, len(sequences), k)]
    aligned_sequences = []
    for group in divided_sequences:
        aligned_sequences.append(align_group(group))
    combined_result = combine_alignments(aligned_sequences)
    execution_time = time.time() - start_time

    return combined_result, execution_time


def improved_alignment(sequences, k):
    start_time = time.time()
    divided_sequences = [sequences[i:i+k] for i in range(0, len(sequences), k)]
    aligned_sequences = align_group(divided_sequences)
    combined_result = combine_alignments(aligned_sequences)
    execution_time = time.time() - start_time
    
    return combined_result, execution_time


def align_group(group):

    return ["aligned_" + seq for seq in group]


def combine_alignments(aligned_groups):
    combined = []
    for group in aligned_groups:
        combined.extend(group)
    return combined


def execute_algorithms(sequences, k_values):
    original_times = []
    improved_times = []
    
    for k in k_values:
        print(f"Executando com K={k}")
        _, original_time = original_alignment(sequences, k)
        original_times.append(original_time)
        

        _, improved_time = improved_alignment(sequences, k)
        improved_times.append(improved_time)
    
    return original_times, improved_times


sequences = [f"seq{i}" for i in range(1, 1001)]
k_values = [3, 4, 5, 6, 7, 8, 9]
original_times, improved_times = execute_algorithms(sequences, k_values)
