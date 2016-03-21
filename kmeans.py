
#initialize

input_name=raw_input("Enter the name of the input file:")
output_name=raw_input("Enter the name of the output file:")
num_clusters=input("Enter the number of clusters:");

file_input=open(input_name,'r')

data_points=[float(x.rstrip()) for x in file_input]

k=num_clusters


centroids = dict(zip(range(k),data_points[0:k]))
clusters = dict(zip(range(k),[[] for i in range(k)]))
point_assignments= dict(zip(range(k), clusters))
old_point_assignments=dict()


def assign_to_clusters(data_points, clusters, centroids,point_assignments):
    for key,point in enumerate(data_points):
        closest_index = ('inf')
        index = 0
        for i in range(len(centroids)):
            distance = abs(point-centroids[i])
            if distance < closest_index:
                closest_index = distance
                index = i
        clusters[index].append(point)
        point_assignments[index]=closest_index
    return point_assignments

def update_location(data_points, clusters, centroids):
    new_centroids={k:sum(v)/float(len(v)) for k,v in clusters.items()}
    centroids.update(new_centroids) 
    return centroids

#Algorithm

iteration=0
point_assignments = assign_to_clusters(data_points, clusters, centroids,point_assignments)
np=dict(old_point_assignments)
while point_assignments != np:
    iteration += 1
    print "\n","Iteration", iteration
    for t, o in clusters.items(): 
        print t, '', o
    new_centroids=update_location(data_points, clusters, centroids)
    old_point_assignments = point_assignments
    np=dict(old_point_assignments)
    clusters = dict(zip(range(k),[[] for i in range(k)]))
    point_assignments = assign_to_clusters(data_points, clusters, new_centroids,point_assignments)
print ""
####do output   
with open(output_name, 'w') as f:
    for c,p in clusters.items():
        for points in p:
            f.write("Point " + str(points) + " in " + str(c) + "\n")
f.close()   

    
