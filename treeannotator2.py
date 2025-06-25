import pandas as pd
import sys
import shutil

#TO RUN: python3 treeannotator2.py annotations.csv oldtree.contree newtree.contree
#ALSO WORKS FOR .TREEFILE!
#annotations.csv should be in the format oldheader, newheader

df = pd.read_csv(str(sys.argv[1]))
tf = str(sys.argv[2])
tf_out = str(sys.argv[3])
print(df)
print(tf)
shutil.copy(tf, tf+".backup")

with open(tf, 'r') as f:
	content = f.read()

print(content)
for index, row in df.iterrows():
	orig = str(row[df.columns[0]])
	replacement = str(row[df.columns[1]])
	print(f"Annotating {orig} as: {replacement}")
	content = content.replace(orig, replacement)
with open(tf_out, 'w') as out:
	out.write(content)
print(f"Annotations saved in {tf_out}")
