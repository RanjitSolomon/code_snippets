# 1. Find Column Sum
# Calculate the total of any numeric column across all rows.
print("--------------1. Find Column Sum-----------------")
path = "./data/data.csv"
print(f"Total: ${sum(float(r[3]) for r in __import__('csv').reader(open(path)) if r[0] != 'transaction_id'):,.2f}")
# Total: $1,814,359.75

# Here, __import__('csv') imports the built-in CSV module inline. The generator expression skips the header row, 
# converts column values to floats, sums them, and formats with currency notation. Adjust the column index (3) and header check as needed.

# 2. Group By Maximum 
# Find which group has the highest aggregate value across your dataset.
print("----------------2. Group By Maximum-------------")
print(max({r[5]: sum(float(row[3]) for row in __import__('csv').reader(open(path)) if row[5] == r[5] and row[0] != 'transaction_id') for r in __import__('csv').reader(open(path)) if r[0] != 'transaction_id'}.items(), key=lambda x: x[1]))
# ('Mike Rodriguez', 502252.0)

# The dictionary comprehension groups by column 5, summing column 3 values for each group. One pass collects group keys and a second does the aggregation. max() with a lambda finds the highest total. Adjust column indices for different group-by operations.

# 3. Filter and Display a Subset of Rows 
# Show only rows that match a specific condition with formatted output.
print("-------------3. Filter and Display a Subset of Rows-----")
print("\n".join(f"{r[1]}: ${float(r[3]):,.2f}" for r in __import__('csv').reader(open(path)) if r[7] == 'Enterprise' and r[0] != 'transaction_id'))
# The generator expression filters rows where column 7 equals Enterprise, then formats columns 1 and 3. Using "\n".join(...) avoids printing a list of None values.

# Acme Corp: $45,000.00
# Gamma Solutions: $78,900.00
# Zeta Systems: $156,000.00
# Iota Industries: $67,500.25
# Kappa LLC: $91,200.75
# Nu Technologies: $76,800.25
# Omicron LLC: $128,900.00
# Sigma Corp: $89,700.75
# Phi Corp: $176,500.25
# Omega Technologies: $134,600.50
# Alpha Solutions: $71,200.25
# Matrix Systems: $105,600.25

# 4. Group By Sum Distribution
# Get totals for each unique value in a grouping column.
print("-------------4. Group By Sum Distribution---------")
print({g: f"${sum(float(row[3]) for row in __import__('csv').reader(open(path)) if row[6] == g and row[0] != 'transaction_id'):,.2f}" for g in set(row[6] for row in __import__('csv').reader(open(path)) if row[0] != 'transaction_id')})
# The dictionary comprehension first extracts unique values from column 6 using a set comprehension, then calculates the sum of column 3 for each group. This is memory efficient due to generator expressions. Change column indices to group by different fields.

# {'Asia Pacific': '$326,551.75', 'Europe': '$502,252.00', 'North America': '$985,556.00'}


# 5. Threshold Filter with Sort
# Find and rank all records above a certain numeric threshold.
print("-----------------5. Threshold Filter with Sort------")
print([(n, f"${v:,.2f}") for n, v in sorted([(r[1], float(r[3])) for r in list(__import__('csv').reader(open(path)))[1:] if float(r[3]) > 100000], key=lambda x: x[1], reverse=True)])
# This filters rows where column 3 exceeds 100000, creates tuples of name and numeric value, sorts by the numeric value, and then formats the values as currency for display. Adjust the threshold and columns as needed.

# [('Phi Corp', '$176,500.25'), ('Zeta Systems', '$156,000.00'), ('Omega Technologies', '$134,600.50'), ('Omicron LLC', '$128,900.00'), ('Matrix Systems', '$105,600.25')]


# 6. Count Unique Values
# Quickly determine how many distinct values exist in any column.
print("-----------------6. Count Unique Values------------")
print(len(set(r[2] for r in __import__('csv').reader(open(path)) if r[0] != 'transaction_id')))
# Here, the set comprehension extracts unique values from column 2; len() counts them. This is useful for checking data diversity or finding distinct categories.

# 3


# 7. Conditional Aggregation
# Calculate averages or other statistics for specific subsets of your data.
print("--------------------7. Conditional Aggregation---------")
print(f"Average: ${sum(float(r[3]) for r in __import__('csv').reader(open(path)) if r[6] == 'North America' and r[0] != 'transaction_id') / sum(1 for r in __import__('csv').reader(open(path)) if r[6] == 'North America' and r[0] != 'transaction_id'):,.2f}")
# This one-liner calculates the average of column 3 for rows matching the condition in column 6. It uses a sum divided by a count (via a generator expression). It reads the file twice but keeps memory usage low.

# Average: $70,396.86


# 8. Multi-Column Filter
# Apply multiple filter conditions simultaneously across different columns.
print("-------------------8. Multi-Column Filter--------------")
print("\n".join(f"{r[1]} | {r[2]} | ${float(r[3]):,.2f}" for r in __import__('csv').reader(open(path)) if r[2] == 'Software' and float(r[3]) > 50000 and r[0] != 'transaction_id'))
# It combines multiple filter conditions with and operators, checks string equality and numeric comparisons, and formats output with pipe separators for clean display.

# Zeta Systems | Software | $156,000.00
# Iota Industries | Software | $67,500.25
# Omicron LLC | Software | $128,900.00
# Sigma Corp | Software | $89,700.75
# Phi Corp | Software | $176,500.25
# Omega Technologies | Software | $134,600.50
# Nexus Corp | Software | $92,300.75
# Apex Industries | Software | $57,800.00


# 9. Compute Column Statistics
# Generate min, max, and average statistics for numeric columns in one shot.
print("------------------9. Compute Column Statistics-----------")
vals = [float(r[3]) for r in __import__('csv').reader(open(path)) if r[0] != 'transaction_id']; print(f"Min: ${min(vals):,.2f} | Max: ${max(vals):,.2f} | Avg: ${sum(vals)/len(vals):,.2f}"); print(vals)
print(vals)
# This creates a list of numeric values from column 3, then calculates min, max, and average in one line. The semicolon separates statements. It is more memory intensive than streaming but faster than multiple file reads for these statistics.

# Min: $8,750.25 | Max: $176,500.25 | Avg: $62,564.13
# [45000.0, 12500.5, 78900.0, 23400.75, 8750.25, 156000.0, 34500.5, 19800.0, 67500.25, 91200.75, 28750.0, 43200.5, 76800.25, 15600.75, 128900.0, 52300.5, 31200.25, 89700.75, 64800.0, 22450.5, 176500.25, 38900.75, 27300.0, 134600.5, 71200.25, 92300.75, 18900.5, 105600.25, 57800.0]


# 10. Export Filtered Data
# Create a new CSV file containing only rows that meet your criteria.
print("-------------------10. Export Filtered Data-------------")
print(__import__('csv').writer(open('filtered.csv','w',newline='')).writerows([r for r in list(__import__('csv').reader(open(path)))[1:] if float(r[3]) > 75000]))

# This reads the CSV, filters rows based on a condition, and writes them to a new file. The newline='' parameter prevents extra line breaks. Note that this example skips the header (it uses [1:]), so include it explicitly if you need a header in the output.















