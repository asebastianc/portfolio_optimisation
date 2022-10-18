import pandas as pd
import lzma

df = pd.read_csv("../../results/alg1/alg1_results.csv")
df = df.iloc[:, -2:]
df = df.fillna("-")

with open("../../results/alg1/alg1_results_format.txt", "a") as file:
	for index, row in df.iterrows():
		if row["Return"] == "-":
			file.write("\n")
		else:
			file.write("{} {}\n".format((row["Return"]), (row["Risk"])))

lzc = lzma.LZMACompressor()
with open("../../results/alg1/alg1_results_format.txt", "r") as fin, open("../../results/alg1/alg1_results_format.xz", "wb") as fout:
	for chunk in fin:
		compressed_chunk = lzc.compress(chunk.encode("ascii"))
		fout.write(compressed_chunk)
	fout.write(lzc.flush())

with open("../../results/alg1/alg1_config.txt", "w") as file:
	file.write("Algorithm 1 Configuration\n")
	file.write("----------------------------------------------\n")
	file.write("• Uncertainty implementation: False.\n")
	file.write("• Second constraint: Return > 0.2.\n")
	file.write("• Reference points: [0.05, 0.2], [0.07, 0.7].\n")
	file.write("• Population size: 100.\n")
	file.write("• Epsilon: 0.5.\n")
	file.write("• Number of generations: 200.\n")
	file.write("• Number of iterations (n): 400.\n")
	file.write("• Seed for each iteration: 500 + n.\n")