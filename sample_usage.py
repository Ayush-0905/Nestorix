from nestorix import Glaze,Nexel

# Step 1: Raw nested curriculum data
curriculum = [
    [  # Subject: Math
        ["Algebra", ["Linear Equations", "Quadratics"]],
        ["Geometry", "Trigonometry"]
    ],
    [  # Subject: Science
        ["Biology", ["Cells", "Genetics"]],
        ["Chemistry", ["Atoms", "Periodic Table"]]
    ],
    [  # Subject: CS
        ["Programming", ["Python", "Loops"]],
        "Data Structures"
    ]
]

# Step 2: Analyze the structure
g = Glaze(curriculum)
print("=== Curriculum Type ===")
print(g._type)  # Should detect list of list of mixed nesting
print("Max Depth:", g.max_depth)
print("Number of actual topics:", g.size)

# Step 3: Convert to structured tree
tree = g.organize_data(preserveNesting=True, preserveDuplication=True)

print("\n=== Full Curriculum Tree ===")
print(tree.info)

# Step 4: How complete is the tree?
print("\nTree Shape (depth x count):", tree.shape)
print("Total capacity:", tree.symmetric_size)
print("Topics actually filled:", tree.size)
print("Missing to make tree complete:", tree.missing_to_make_tree)

# Step 5: Access a specific subtopic (e.g., "Quadratics")
depth,count=tree.index_node_tree('Quadratics')
print(f"\n'Quadratics' is at Level {depth}, Count {count}")
print("Accessed via fetch():", tree.fetch(depth, count).data)

# Step 6: Access previous/next content
print("Previous of 'Quadratics':", tree.fetch_prev_of("Quadratics"))
print("Next of 'Algebra':", tree.fetch_next_of("Algebra"))

# Step 7: Functional update – make all topic titles UPPERCASE
uppercased = tree.apply(lambda x: str(x).upper())
print("\n=== UPPERCASED Curriculum ===")
print(uppercased.info)

# Step 8: Modify content using index and assignment
print("\nOriginal at index 1:", tree[1].info)
tree.insert(1, ["Physics", "Thermodynamics"])
print("After Inserting Physics at index 1:", tree[1].info)

# Step 9: Append new topic
tree.append(["Robotics", "AI"])
print("\nAfter Appending Robotics:", tree.info)

# Step 10: Remove a topic
tree.remove("Geometry")
print("\nAfter Removing 'Geometry':", tree.info)

# Step 11: Pop index
tree.pop(0)
print("\nAfter Popping Subject 0:", tree.info)

# Step 12: Check depth of a topic
try:
    print("Depth of 'Genetics':", tree.depth_of("Genetics"))
    print("This means error as index 1 is now ['Physics' ,'Thermodynamics']")
except:
    print('Genetics already removed')

# Step 13: Iteration (print all topics)
print("\nAll topics (Level-0):")
print(tree.information(tree.fetch(1)))

# Step 14: Matrix form for Excel/DataFrame
print("\nMatrix View:")
matrix = tree.make_matrix()
for row in matrix:
    print([n.data for n in row])

# Step 15: NumPy Tree
print("\nNumPy Tree View:")
print(tree.make_numpy_tree())

# Step 16: NumPy flat
print("\nFlat NumPy Array of topics:")
print(tree.make_numpy_original())

# Step 17: Equality check
copy = tree.__copy__()
print("\nCopy is equal to tree:", copy == tree)

# Step 18: Index in level-0
try:
    idx = tree[1].index(["Programming", ["Python", "Loops"]])
    print("Index of CS topic in 2nd element of the data is:", idx)
except:
    print("Topic not found in level-0")

# Step 19: Add with +
new = Nexel(["Cybersecurity", ["Networking"]])
combined = tree + new
print("\nCombined Tree Info (after +):", combined.info)

# Step 20: In-place add with +=
tree += ["IoT", ["Sensors"]]
print("\nAfter += ['IoT', ['Sensors']]:", tree.info)