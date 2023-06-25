#!/usr/bin/env python

import sys

# Initialize the count for each category to zero
category_count = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input
for line in sys.stdin:
    # Split the line at the tabulator ("\t")
    # Strip removes whitespaces and new lines at the beginning and end of the line
    # The result is a tuple with 2 elements
    data = line.strip().split("\t")

    # Store the 2 elements of this line in separate variables
    key, value = data

    # Do we have a previous_key (previous_key != None) and
    # is the new key different than the previous key?
    # This means the line starts with a new key (key changes e.g. from "Visa" to "Cash")
    # Remember that our keys are sorted
    if previous_key is not None and previous_key != key:
        # Then write the result of the old key (Key=category, Value=Count of Purchases)
        # to the standard output (stdout)
        # Key and value are separated by a tab (\t)
        # Line ends with a new line (\n)
        # Calculate the average sales per category
        if category_purchase_count > 0:
            average_sales = category_total_sales / category_purchase_count
            # Write the result of the old key (Key=category, Value=Average Sales)
            # to the standard output (stdout)
            # Key and value are separated by a tab (\t)
            # Line ends with a new line (\n)
            sys.stdout.write("{0}\t{1}\n".format(previous_key, average_sales))
        # Reset the variables for the new category
        category_total_sales = 0
        category_purchase_count = 0

    # Update the total sales and purchase count for the current category
    category_total_sales += float(value)
    category_purchase_count += 1
    # The previous key for the next iteration is the current key of this iteration
    previous_key = key

# Calculate and write the average sales for the last category
if category_purchase_count > 0:
    average_sales = category_total_sales / category_purchase_count
    sys.stdout.write("{0}\t{1}\n".format(previous_key, average_sales))
