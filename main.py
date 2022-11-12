def transition(A):
  result = []
  for row in A:
    count = 0
    temp = []
    for i in range(len(row)):
      if (row[i] == 1):
        count += 1
        temp.append(i)
    for item in temp:
      row[item] = 1 / count
    result.append(row)
  return result


def transpose(A):
  result = []
  for i in range(len(A[0])):
    row = []
    for j in A:
      row.append(j[i])
    result.append(row)
  return result


def powerIteration(A, num_iteration):
  transition_matrix = transition(A)
  p = transpose(transition_matrix)
  link = []
  n = 0
  for node in p:
    n += 1
    node_link = []
    for i in range(len(node)):
      if(node[i] != 0):
        node_link.append(i)
    link.append(node_link)

  result = [1/n] * n
  iteration_count = 0
  prev_iteration = [1/n] * n
  while(iteration_count < num_iteration):
    iteration_count += 1
    print("# of iteration:", iteration_count)
    r = [0] * n
    for i in range(n):
      r[i] = (1 - 0.85)/n
      for index in link[i]:
        r[i] += 0.85 * p[i][index] * prev_iteration[index]
    result.append(r)
    for j in range(n):
      prev_iteration[j] = r[j]
    print("prev_iteration:", prev_iteration)
  
  return result[iteration_count]
  
a = [[0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0]]

print("page rank result: ",powerIteration(a, 30))
