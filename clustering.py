
import math

# -- Compute the distance between two entries
def entry_distance(entry1, entry2):
    d = 0.0
    return d

# -- Compute the minimum distance between two clusters
#    Loop over all pairs of entries (one from c1 and
#    one from c2), compute the distance between the
#    pairs, and choose the SMALLEST of the distances.
def min_cluster_distance(c1, c2):
    d = 0.0
    return d

# -- Compute the maximum distance between two clusters
#    Loop over all pairs of entries (one from c1 and
#    one from c2), compute the distance between the
#    pairs, and choose the LARGEST of the distances.
def max_cluster_distance(c1, c2):
    d = 0.0
    return d

# -- Compute the average distance between two clusters
#    Loop over all pairs of entries (one from c1 and
#    one from c2), compute the average of ALL the distances.
def average_cluster_distance(c1, c2):
    d = 0.0
    return d

# -- Find the closest pair of clusters
#    Loop over all the possible pairs of clusters, figure out
#    which pair are closest together according to the choice
#    of metric:
#       1 means minimum distance
#       2 means maximum distance
#       3 means average distance
def find_closest_pair(clusters, metric):
    result = (None, None)
    return result

# -- Main clustering algorithm
#    Start by creating a set of clusters where each one has
#    just a single data item in it. Then merge clusters by
#    picking the two that are closest together and merging
#    them into one until we reach the target number of
#    clusters.
def do_clustering(data, target, metric):
    num_iterations = 0
    clusters = make_clusters(data)
    while len(clusters) > target:
        # -- Find the pair of clusters closest together
        (c1, c2) = find_closest_pair(clusters, metric)

        # -- Merge them together
        clusters.remove(c1)
        clusters.remove(c2)
        c3 = c1 + c2
        clusters.append(c3)

        num_iterations += 1
        print("Iteration " + str(num_iterations) + " " + str(len(clusters)) + " clusters")

    return clusters


# -- Make an initial set of clusters
#    Just put each entry in its own cluster
def make_clusters(data):
    clusters = []
    for entry in data:
        clusters.append([entry])
    return clusters

# ---------------------------------------------------------
#  Code to read in and normalize the data
#  You shouldn't need to modify anything here

# -- Read in the data file
def read_data_file(datafile):
    data = []
    with open(datafile) as f:
        done = False
        while not done:
            line = f.readline().rstrip()
            if line:
                if not line.startswith('#'):
                    fstrs = line.split(' ')
                    name = fstrs[0]
                    features = []
                    for i in range(1, len(fstrs)):
                        features.append(int(fstrs[i]))
                    entry = (name, features)
                    data.append(entry)
            else:
                done = True
    return data

def get_num_features(data):
    entry0 = data[0]
    features = entry0[1]
    return len(features)

# -- Compute the max value of each feature
def compute_max_features(data):
    num_features = get_num_features(data)
    max_values = [0 for _ in range(0, num_features)]
    for entry in data:
        features = entry[1]
        for i in range(0, num_features):
            if features[i] > max_values[i]:
                max_values[i] = features[i]
    return max_values

# -- Normalize the feature values to 0 -- 1
def normalize(data):
    new_data = []
    num_features = get_num_features(data)
    max_values = compute_max_features(data)
    for entry in data:
        name = entry[0]
        features = entry[1]
        new_features = []
        for i in range(0, num_features):
            val = float(features[i])
            max_val = float(max_values[i])
            norm = val/max_val
            new_features.append(norm)
        new_entry = (name, new_features)
        new_data.append(new_entry)
    return new_data

# -- Find a data entry by name
def find_entry(name, data):
    for entry in data:
        if entry[0] == name:
            return entry
    return None

# ---------------------------------------------------------
# -- Here's where the program actually starts running...
filename = input('Enter data file name: ')
data_raw = read_data_file((filename))

# -- Normalize the data
data = normalize(data_raw)
print("Read in {} data entries".format(len(data)))

# -- User interaction
done = False
while not done:
    print("Enter choice:")
    print(" 1: Test entry distance function")
    print(" 2: Do clustering")

    choice = int(input("Enter 1-2: "))

    if choice == 1:
        s1 = input("Entry 1 name: ")
        s2 = input("Entry 2 name: ")
        entry1 = find_entry(s1, data)
        entry2 = find_entry(s2, data)
        if entry1 and entry2:
            d = entry_distance(entry1, entry2)
            print("Distance " + s1 + " to " + s2 + " = " + str(d))
    elif choice == 2:
        target_s = input("Target number of clusters: ")
        target = int(target_s)

        clusters = do_clustering(data, target)

        cnum = 1
        for c in clusters:
            print("Cluster " + str(cnum))
            for entry in c:
                print("    " + entry[0])
            cnum += 1
    else:
        done = True
