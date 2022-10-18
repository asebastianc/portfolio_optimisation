import pandas as pd
import lzma

df = pd.read_csv("../../results/alg2/alg2_results.csv")
df = df.iloc[:, -2:]
df = df.fillna("-")

with open("../../results/alg2/alg2_results_format.txt", "a") as file:
	for index, row in df.iterrows():
		if row["Return"] == "-":
			file.write("\n")
		else:
			file.write("{} {}\n".format((row["Return"]), (row["Risk"])))

lzc = lzma.LZMACompressor()
with open("../../results/alg2/alg2_results_format.txt", "r") as fin, open("../../results/alg2/alg2_results_format.xz", "wb") as fout:
	for chunk in fin:
		compressed_chunk = lzc.compress(chunk.encode("ascii"))
		fout.write(compressed_chunk)
	fout.write(lzc.flush())

with open("../../results/alg2/alg2_config.txt", "w") as file:
	file.write("Algorithm 2 Configuration\n")
	file.write("----------------------------------------------\n")
	file.write("• Uncertainty implementation: True.\n")
	file.write("• Second constraint: None.\n")
	file.write("• Reference points: [0.2, 0.02], [0.4, 0.07].\n")
	file.write("• Population size: 100.\n")
	file.write("• Epsilon: 0.01.\n")
	file.write("• Number of generations: 200.\n")
	file.write("• Number of iterations (n): 400.\n")
	file.write("• Seed for each iteration: n.\n")