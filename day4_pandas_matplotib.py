# ============================================
# DAY 4 - Pandas & Matplotlib
# Author: Suraj Panjabi
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

print("Pandas:", pd.__version__)

# ---- Lesson 2: DataFrames ----

# Create a DataFrame of gene data
gene_data = {
    "gene": ["BRCA1", "TP53", "EGFR", "GFP", "KRAS"],
    "length_bp": [7088, 1182, 5566, 720, 5828],
    "gc_content": [41.77, 55.93, 77.97, 63.16, 58.42],
    "chromosome": [17, 17, 7, 0, 12],
    "cancer_related": [True, True, True, False, True]
}

df = pd.DataFrame(gene_data)

print("\n--- Gene DataFrame ---")
print(df)
# Basic info about your data
print("\n--- DataFrame Info ---")
print("Shape:", df.shape)           # rows x columns
print("Columns:", df.columns.tolist())
print("\nFirst 3 rows:")
print(df.head(3))
print("\nBasic statistics:")
print(df.describe())
# Select one column
print("\n--- Gene Names ---")
print(df["gene"])

# Select multiple columns
print("\n--- Gene and GC Content ---")
print(df[["gene", "gc_content"]])

# Filter rows
print("\n--- Cancer Related Genes Only ---")
cancer_genes = df[df["cancer_related"] == True]
print(cancer_genes)

# Sort by GC content
print("\n--- Sorted by GC Content ---")
print(df.sort_values("gc_content", ascending=False))
# Basic info about your data
print("\n--- DataFrame Info ---")
print("Shape:", df.shape)           # rows x columns
print("Columns:", df.columns.tolist())
print("\nFirst 3 rows:")
print(df.head(3))
print("\nBasic statistics:")
print(df.describe())
# Select one column
print("\n--- Gene Names ---")
print(df["gene"])

# Select multiple columns
print("\n--- Gene and GC Content ---")
print(df[["gene", "gc_content"]])

# Filter rows
print("\n--- Cancer Related Genes Only ---")
cancer_genes = df[df["cancer_related"] == True]
print(cancer_genes)

# Sort by GC content
print("\n--- Sorted by GC Content ---")
print(df.sort_values("gc_content", ascending=False))

# ---- Lesson 3: Matplotlib Charts ----

# Chart 1: GC Content Bar Chart
plt.figure(figsize=(10, 6))

colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6"]

plt.bar(df["gene"], df["gc_content"], color=colors, edgecolor="black", linewidth=0.5)

plt.title("GC Content Comparison Across Genes", fontsize=16, fontweight="bold")
plt.xlabel("Gene", fontsize=12)
plt.ylabel("GC Content (%)", fontsize=12)
plt.ylim(0, 100)

# Add a horizontal line showing average human GC content
plt.axhline(y=41, color="red", linestyle="--", label="Human genome average (41%)")
plt.legend()

# Add value labels on top of each bar
for i, (gene, gc) in enumerate(zip(df["gene"], df["gc_content"])):
    plt.text(i, gc + 1, f"{gc}%", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("c:/Bioinformatics/gc_content_chart.png", dpi=300)
plt.show()
print("Chart saved! ✅")

# Chart 2: Nucleotide Composition of BRCA1
brca1_sequence = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAA"

nucleotides = ["A", "T", "G", "C"]
counts = [brca1_sequence.count(n) for n in nucleotides]
colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12"]

plt.figure(figsize=(8, 6))
bars = plt.bar(nucleotides, counts, color=colors, edgecolor="black", linewidth=0.5)

plt.title("BRCA1 Nucleotide Composition", fontsize=16, fontweight="bold")
plt.xlabel("Nucleotide", fontsize=12)
plt.ylabel("Count", fontsize=12)

# Add counts on top of bars
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             str(count), ha="center", fontsize=12, fontweight="bold")

plt.tight_layout()
plt.savefig("c:/Bioinformatics/brca1_nucleotides.png", dpi=300)
plt.show()
print("Nucleotide chart saved! ✅")

# Chart 3: Gene Length vs GC Content scatter plot
plt.figure(figsize=(10, 6))

scatter = plt.scatter(
    df["length_bp"],
    df["gc_content"],
    c=df["gc_content"],
    s=200,
    cmap="RdYlGn",
    edgecolors="black",
    linewidth=1
)

# Label each point with gene name
for i, row in df.iterrows():
    plt.annotate(row["gene"],
                (row["length_bp"], row["gc_content"]),
                textcoords="offset points",
                xytext=(10, 5),
                fontsize=10)

plt.colorbar(scatter, label="GC Content (%)")
plt.title("Gene Length vs GC Content", fontsize=16, fontweight="bold")
plt.xlabel("Gene Length (bp)", fontsize=12)
plt.ylabel("GC Content (%)", fontsize=12)
plt.tight_layout()
plt.savefig("c:/Bioinformatics/length_vs_gc.png", dpi=300)
plt.show()
print("Scatter plot saved! ✅")
# ---- Lesson 4: Real Biological Analysis ----

# Create a more detailed gene dataset
detailed_data = {
    "gene": ["BRCA1", "BRCA2", "TP53", "EGFR", "KRAS", "HER2", "PIK3CA", "PTEN"],
    "gc_content": [41.77, 39.52, 55.93, 77.97, 58.42, 62.14, 54.87, 43.21],
    "length_bp": [7088, 10938, 1182, 5566, 5828, 4512, 3207, 5547],
    "chromosome": [17, 13, 17, 7, 12, 17, 3, 10],
    "mutation_freq": [0.08, 0.06, 0.50, 0.15, 0.22, 0.12, 0.18, 0.09]
}

df2 = pd.DataFrame(detailed_data)

# Analysis 1: Average GC content
print("\n--- Summary Statistics ---")
print(f"Average GC content: {df2['gc_content'].mean():.2f}%")
print(f"Highest GC: {df2.loc[df2['gc_content'].idxmax(), 'gene']} ({df2['gc_content'].max():.2f}%)")
print(f"Lowest GC:  {df2.loc[df2['gc_content'].idxmin(), 'gene']} ({df2['gc_content'].min():.2f}%)")
print(f"Average length: {df2['length_bp'].mean():.0f} bp")

# Analysis 2: Most commonly mutated genes
print("\n--- Mutation Frequency (highest first) ---")
print(df2[["gene", "mutation_freq"]].sort_values("mutation_freq", ascending=False))

# Analysis 3: Genes on chromosome 17
print("\n--- Genes on Chromosome 17 ---")
chr17 = df2[df2["chromosome"] == 17]
print(chr17[["gene", "gc_content", "length_bp"]])

# Chart: Mutation frequency
plt.figure(figsize=(12, 6))
sorted_df = df2.sort_values("mutation_freq", ascending=True)
colors = ["#e74c3c" if x > 0.15 else "#3498db" for x in sorted_df["mutation_freq"]]

plt.barh(sorted_df["gene"], sorted_df["mutation_freq"] * 100, color=colors)
plt.title("Cancer Gene Mutation Frequency", fontsize=16, fontweight="bold")
plt.xlabel("Mutation Frequency in Cancer (%)", fontsize=12)
plt.axvline(x=15, color="red", linestyle="--", label="15% threshold")
plt.legend()
plt.tight_layout()
plt.savefig("c:/Bioinformatics/mutation_frequency.png", dpi=300)
plt.show()
print("Mutation frequency chart saved! ✅")

# ---- Lesson 5: Save to CSV ----

# Save your DataFrame to a CSV file
df2.to_csv("c:/Bioinformatics/gene_analysis.csv", index=False)
print("\nData saved to gene_analysis.csv ✅")

# Read it back
df_loaded = pd.read_csv("c:/Bioinformatics/gene_analysis.csv")
print("\n--- Loaded from CSV ---")
print(df_loaded)

print("\n✅ Day 4 Complete!")