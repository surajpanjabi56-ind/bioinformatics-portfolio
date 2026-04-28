#----Lesson 1:VARIABLES---
# Storing a DNA sequence
dna_sequence="ATCGATCGTAGCTAGC"
#Storing a gene name
gene_name="BRCA1"
#storing a number 
chromosome=17
#storing True/False
is_mutated=True
print("gene:",gene_name)
print("chromosome:",chromosome)
print("sequence:",dna_sequence)
print("mutatetd",is_mutated)

# ---- Lesson 2: Lists ----
# A list of DNA sequences

dna_sequences = [
    "ATCGATC",
    "GCTAGCTA",
    "TTAACCGG",
    "AATTGGCC"
]

print("Number of sequences:", len(dna_sequences))
print("First sequence:", dna_sequences[0])
print("Last sequence:", dna_sequences[-1])
print("All sequences:", dna_sequences)
print("Sequences 1 and 2:", dna_sequences[1:3])

# ---- Lesson 3: Loops ----

#Loop 1: Print every sequence
print("\nAll DNA sequences:")
for seq in dna_sequences:
    print(seq)  
#Loop 2: Print sequences and its length
print("\nDNA sequences and their lengths:")
for seq in dna_sequences:
    print(seq, "Length:",len(seq))
    
#loops Number each sequence 
print("\nNumbered DNA sequences:")
for i, seq in enumerate(dna_sequences, start=1):
    print(f"{i}. {seq}")    

#loop4: Count total number of nucleotides
total_nucleotides = 0
for seq in dna_sequences:
    total_nucleotides += len(seq)   
print("\nTotal number of nucleotides:", total_nucleotides)      
        
    #loop5: Calculate GC content for each sequence
print("\nGC content for each sequence:")
for seq in dna_sequences:
    gc_count = seq.count('G') + seq.count('C')
    gc_content = (gc_count / len(seq)) * 100
    print(f"{seq}: {gc_content:.1f}% GC content")