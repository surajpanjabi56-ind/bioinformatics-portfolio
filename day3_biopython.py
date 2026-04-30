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