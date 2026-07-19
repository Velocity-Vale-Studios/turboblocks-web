import os

FILE_PATH = r"s:\turboblocks-web\src\pages\checkout.astro"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# We need to extract payment-method-section from summary-column and put it in left column.

# 1. Find the payment-method-section
# It starts with: {/* Payment method (Hidden on Stage 0) */}
# and ends right before: {/* Pay button */}

start_marker = "{/* Payment method (Hidden on Stage 0) */}"
end_marker = "{/* Pay button */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    payment_section = content[start_idx:end_idx]
    
    # Remove from right column
    content = content[:start_idx] + content[end_idx:]
    
    # Now find where to insert it in the left column.
    # It should go right before: {/* Stage 3: Summary Success (Hidden by default) */}
    insert_marker = "{/* Stage 3: Summary Success (Hidden by default) */}"
    insert_idx = content.find(insert_marker)
    
    if insert_idx != -1:
        content = content[:insert_idx] + payment_section + "\n                " + content[insert_idx:]
        
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully moved payment section to the left column.")
    else:
        print("Insert marker not found.")
else:
    print("Payment section boundaries not found.")
