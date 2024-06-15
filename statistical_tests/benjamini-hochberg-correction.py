from scipy import stats

p_values = [0.104, 0.090, 3.30e-13, 5.75e-15, 9.30e-06, 4.35e-06, 2.46e-05, 1.41e-05, 0.999, 0.999,
            0.001, 0.001, 0.484, 0.443, 0.003, 0.001, 0.019, 0.012, 0.138, 0.100, 0.902, 0.860,
            0.999, 0.999, 3.59e-11, 2.50e-10, 3.75e-14, 9.67e-16]

p_values_corrected = stats.false_discovery_control(p_values)

paired_p_values = list(zip(p_values, p_values_corrected))

sorted_paired_p_values = sorted(paired_p_values, key=lambda x: x[0], reverse=False)

# Print the sorted p-values
print(f"{'P-value':<20} {'Corrected P-value'}")
print("-" * 40)
for raw, corrected in sorted_paired_p_values:
    print(f"{raw:<20} {corrected}")