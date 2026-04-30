#===
#DNA_analyser.py
#Author : Suraj Panjabi
# Date : May 2026 
# ===

def analyse_dna(sequence, name="Unknown"):
    sequence = sequence.upper()
    length = len(sequence)                  
    a= sequence.count('A')
    t= sequence.count('T')      
    g= sequence.count('G')
    c= sequence.count('C')  
    gc = (g+c)/length*100

    print(f"\n{'='*45}")
    print(f"gene: {name}")
    print(f"{'-'*45}")
    print(f"Sequence: {sequence}")
    print(f"Length: {length} base pairs")
    print(f"Nucleotide Counts - A: {a}, T: {t}, G: {g}, C: {c}")
    print(f"GC Content: {gc:.2f}%")
    # Real gene fragments
analyse_dna("ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAAT", "BRCA1")
analyse_dna("ATGGAGGAGCCGCAGTCAGATCCTAGCGTTGAATCCAG", "TP53")
analyse_dna("ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGT", "GFP")