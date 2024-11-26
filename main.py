import copy

def fifo_page_replacement(pages, frame_size):
    """
    First In First Out (FIFO) Page Replacement Algorithm
    """
    fifo_frames = []
    page_faults = 0
    page_hits = 0

    print("\n--- FIFO Page Replacement Frame Progression ---")
    for page in pages:
        if page in fifo_frames:
            page_hits += 1
        else:
            page_faults += 1

            if len(fifo_frames) < frame_size:
                fifo_frames.append(page)
            else:
                fifo_frames.pop(0)  # Remove the first page
                fifo_frames.append(page)

        print(f"Frames: {fifo_frames}")

    hit_ratio = page_hits / len(pages)
    fault_ratio = page_faults / len(pages)

    # Print results in comparison format
    print("\nFIFO Page Replacement Results:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Algorithm", "Page Hits", "Page Faults", "Hit Ratio", "Fault Ratio", "Total Pages"))
    print("-" * 90)
    print("{:<15} {:<15} {:<15} {:<15.2%} {:<15.2%} {:<15}".format(
        "FIFO", page_hits, page_faults, hit_ratio, fault_ratio, len(pages)))

    return page_hits, page_faults, hit_ratio, fault_ratio


def lru_page_replacement(pages, frame_size):
    """
    Least Recently Used (LRU) Page Replacement Algorithm
    """
    lru_frames = []
    recent_order = []  # New list to track the order of page references
    page_faults = 0
    page_hits = 0

    print("\n--- LRU Page Replacement Frame Progression ---")
    for page in pages:
        if page in lru_frames:
            page_hits += 1
            # Remove the existing index of the page in recent_order
            # and move it to the end to mark as most recently used
            recent_order.remove(lru_frames.index(page))
            recent_order.append(lru_frames.index(page))
        else:
            page_faults += 1
            if len(lru_frames) < frame_size:
                # Add new page to frames and track its initial position
                lru_frames.append(page)
                recent_order.append(len(lru_frames) - 1)
            else:
                # Find the least recently used page index
                # (first index in recent_order)
                lru_index = recent_order.pop(0)

                # Replace the least recently used page
                lru_frames[lru_index] = page

                # Add the new page's index to recent_order
                recent_order.append(lru_index)

        print(f"Frames: {lru_frames}")

    hit_ratio = page_hits / len(pages)
    fault_ratio = page_faults / len(pages)

    # Print results in comparison format
    print("\nLRU Page Replacement Results:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Algorithm", "Page Hits", "Page Faults", "Hit Ratio", "Fault Ratio", "Total Pages"))
    print("-" * 90)
    print("{:<15} {:<15} {:<15} {:<15.2%} {:<15.2%} {:<15}".format(
        "LRU", page_hits, page_faults, hit_ratio, fault_ratio, len(pages)))

    return page_hits, page_faults, hit_ratio, fault_ratio


def optimal_page_replacement(pages, frame_size):
    """
    Optimal Page Replacement Algorithm
    """
    optimal_frames = []
    page_faults = 0
    page_hits = 0

    print("\n--- Optimal Page Replacement Frame Progression ---")
    for i, page in enumerate(pages):
        if page in optimal_frames:
            page_hits += 1
        else:
            page_faults += 1

            if len(optimal_frames) < frame_size:
                optimal_frames.append(page)
            else:
                # Find the page that won't be used for the longest time
                max_future_index = -1
                page_to_replace = optimal_frames[0]

                for frame_page in optimal_frames:
                    try:
                        future_index = pages[i + 1:].index(frame_page)
                    except ValueError:
                        # If page is not found in future, replace it
                        page_to_replace = frame_page
                        break

                    if future_index > max_future_index:
                        max_future_index = future_index
                        page_to_replace = frame_page

                optimal_frames.remove(page_to_replace)
                optimal_frames.append(page)

        print(f"Frames: {optimal_frames}")

    hit_ratio = page_hits / len(pages)
    fault_ratio = page_faults / len(pages)

    # Print results in comparison format
    print("\nOptimal Page Replacement Results:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Algorithm", "Page Hits", "Page Faults", "Hit Ratio", "Fault Ratio", "Total Pages"))
    print("-" * 90)
    print("{:<15} {:<15} {:<15} {:<15.2%} {:<15.2%} {:<15}".format(
        "Optimal", page_hits, page_faults, hit_ratio, fault_ratio, len(pages)))

    return page_hits, page_faults, hit_ratio, fault_ratio


def compare_page_replacement_algorithms(fifo_pages, lru_pages, optimal_pages, frame_size):
    """
    Compare all three page replacement algorithms
    """
    print("\n--- Comparison of Page Replacement Algorithms ---")

    # Perform algorithms
    fifo_hits, fifo_faults, fifo_hit_ratio, fifo_fault_ratio = fifo_page_replacement(fifo_pages, frame_size)
    lru_hits, lru_faults, lru_hit_ratio, lru_fault_ratio = lru_page_replacement(lru_pages, frame_size)
    optimal_hits, optimal_faults, optimal_hit_ratio, optimal_fault_ratio = optimal_page_replacement(optimal_pages,
                                                                                                    frame_size)

    # Create a formatted comparison table
    print("\nComparison Results:")
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "Algorithm", "Page Hits", "Page Faults", "Hit Ratio", "Fault Ratio"))
    print("-" * 90)

    # Print results for each algorithm
    algorithms = [
        ("FIFO", fifo_hits, fifo_faults, fifo_hit_ratio, fifo_fault_ratio),
        ("LRU", lru_hits, lru_faults, lru_hit_ratio, lru_fault_ratio),
        ("Optimal", optimal_hits, optimal_faults, optimal_hit_ratio, optimal_fault_ratio)
    ]

    for name, hits, faults, hit_ratio, fault_ratio in algorithms:
        print("{:<15} {:<15} {:<15} {:<15.2%} {:<15.2%}".format(
            name, hits, faults, hit_ratio, fault_ratio))


def main():
    while True:
        print("\n--- Page Replacement Algorithms ---")
        print("1. Implement FIFO")
        print("2. Implement LRU")
        print("3. Implement Optimal Page Replacement")
        print("4. Compare All Algorithms")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the program...")
            break

        # Get frame size from user
        frame_size = int(input("Enter the frame size: "))

        # Pages array
        # Get pages array from user
        pages_input = input("Enter the pages (comma-separated): ")
        pages = list(map(int, pages_input.split(',')))

        fifo_page = copy.deepcopy(pages)
        lru_page = copy.deepcopy(pages)
        optimal_page = copy.deepcopy(pages)

        # Switch case for algorithm selection
        if choice == '1':
            fifo_page_replacement(fifo_page, frame_size)
        elif choice == '2':
            lru_page_replacement(lru_page, frame_size)
        elif choice == '3':
            optimal_page_replacement(optimal_page, frame_size)
        elif choice == '4':
            compare_page_replacement_algorithms(fifo_page, lru_page, optimal_page, frame_size)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()