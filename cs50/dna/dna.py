import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print('Usage: python dna.py data.csv sequence.txt')
        sys.exit(1)
    
    # TODO: Read database file into a variable
    with open(sys.argv[1], 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        reader_dict = [dicts for dicts in reader]
        
    # TODO: Read DNA sequence file into a variable
        with open(sys.argv[2], 'r') as sequences_file:
            sequence_reader = ''.join(sequences_file.read())
            
    # TODO: Find longest match of each STR in DNA sequence
            dna_str = []
            name_list = []
            counts = {}
            for dicts in reader_dict:
                for name in dicts:
                    if name == 'name':
                        name_list.append(dicts[name])
                    if name not in dna_str and name != 'name':
                        dna_str.append(name)
            for st in dna_str:
                counts[st] = longest_match(sequence_reader, st)
            

    # TODO: Check database for matching profiles
            counts_list = [counts[count] for count in counts]

            name_seq_dict = {}
            for dicts in reader_dict:
                str_seq = []
                for name in dicts:
                    if name != 'name':
                        str_seq.append(int(dicts[name]))
                name_seq_dict[dicts['name']] = str_seq

            for name in name_seq_dict:
                if name_seq_dict[name] == counts_list:
                    print(name)
                    sys.exit()
            print('No match')


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    #print(sequence)
    #print(subsequence)
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
