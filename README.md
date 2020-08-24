# Ant Colony Algorithm

 ### Ant colony optimization (ACO) methodology is based on the ant’s capability of finding the shortest path from the nest to a food source.

  ### An ant repeatedly hops from one location to another to ultimately reach the destination (food). Each arc (i, j) of the graph G = (N, A) has an associated variable τij called the pheromone trail.

 ### Ants deposit an organic compound called pheromones while tracing a path.

  ### The intensity of the pheromone is an indicator of the utility of that arc to build better solutions.

![ants](https://user-images.githubusercontent.com/51750773/91031086-c3f59580-e608-11ea-9a9d-ee27ce5531a0.jpg)

  ### Using this decision policy, ants hop from the source to the destination.

  ### The pheromone level at each iteration is updated
  
![antsFormula](https://user-images.githubusercontent.com/51750773/91031772-b68cdb00-e609-11ea-8651-726cc444a99e.jpg)


  ### This is the process in which pheromone for certain solutions are decreased using “local” information; therefore, this step is also often referred to as local update. This step is pivotal to ensure that the ACO algorithm does not prematurely converge to a single solution

 ### This step refers to decisions made based on global information relating to the optimization problem. Note the difference between local in step 2 and global in step 3. Analog to step 2, step 3 is also often referred to as global update.

 ### The three steps highlighted above are repeated until the optimization problem has converged or is otherwise terminated via a prespecified termination condition
 
 ![antsUpdate](https://user-images.githubusercontent.com/51750773/91034877-606e6680-e60e-11ea-98cf-7d47a24593e7.jpg)


 ### Based on the above, it is clear that significant development and analysis work is required before ACO could be applied to the nonlinear topology optimization problems of concern
