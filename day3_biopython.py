# ============================================
# DAY 3 - Biopython & FASTA Files
# Author: Suraj Panjabi
# ============================================

from Bio import SeqIO

print("--- FASTA File Analysis ---")

for record in SeqIO.parse("c:/Bioinformatics/sequences.fasta", "fasta"):
    sequence = str(record.seq).upper()
    g = sequence.count("G")
    c = sequence.count("C")
    gc = ((g + c) / len(sequence)) * 100

    print(f"\nID:       {record.id}")
    print(f"Sequence: {sequence}")
    print(f"Length:   {len(sequence)} bp")
    print(f"GC:       {gc:.2f}%")

# ---;--- Lesson 3: Downloading Sequences from NCBI ---
from Bio import Entrez  
Entrez.email = "surajpanjabi56@gmail.com"  # Always provide your email when using Entrez           
print("\n--- Downloading BRCA1 from NCBI ---")
print("Fetching BRCA1 sequence...")
handle = Entrez.efetch(db="nucleotide", id="NM_007294", rettype="fasta", retmode="text")

#read it
brca1_record = SeqIO.read(handle, "fasta")
handle.close()  

# show results
print(f"\nID:       {brca1_record.id}")
print(f"Sequence: {brca1_record.seq}")
print(f"Length:   {len(brca1_record.seq)} bp")      

# save to file
with open("c:/Bioinformatics/brca1.fasta", "w") as f:
    SeqIO.write(brca1_record, f, "fasta")    
    print ("\nBRCA1 sequence saved to brca1.fasta")

# Analyse the real BRCA1
sequence = str(brca1_record.seq).upper()
g = sequence.count("G")
c = sequence.count("C")
a = sequence.count("A")
t = sequence.count("T")
gc = ((g + c) / len(sequence)) * 100

print(f"\n--- Real BRCA1 Analysis ---")
print(f"Length:     {len(sequence)} bp")
print(f"A: {a} | T: {t} | G: {g} | C: {c}")
print(f"GC Content: {gc:.2f}%")

# ---- Lesson 4: Writing FASTA Files ----
print("\n--- Creating My Own FASTA File ---")

# Write FASTA manually - no special library needed
sequences = [
    ("BRCA1_custom", "My custom BRCA1 fragment", "ATGGATTTATCTGCTCTTCGCGTTGAAGAAG"),
    ("TP53_custom", "My custom TP53 fragment", "ATGGAGGAGCCGCAGTCAGATCCTAGCGTTG"),
    ("GFP_custom", "My custom GFP fragment", "ATGGTGAGCAAGGGCGAGGAGCTGTTCACCG")
]

with open("c:/Bioinformatics/my_sequences.fasta", "w") as f:
    for seq_id, description, sequence in sequences:
        f.write(f">{seq_id} {description}\n")
        f.write(f"{sequence}\n\n")

print("Written 3 sequences to my_sequences.fasta ✅")

# Read it back to verify
print("\n--- Verifying ---")
for record in SeqIO.parse("c:/Bioinformatics/my_sequences.fasta", "fasta"):
    print(f"{record.id}: {len(record.seq)} bp")

print("\n✅ Day 3 Complete!")