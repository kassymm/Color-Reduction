param m, integer, > 0;
/* number of clusters */

param n, integer, > 0;
/* number of colors */

param k, integer, > 0;

set S := 1..m;
/* set of clusters */

set P := 1..n;
/* set of colors */

param D{i in S}, >= 0;
/* cost of cluster */

param C{i in S, j in P}, binary;
/* whether cluster i has a color j */


var beta{i in S}, binary;



s.t. k_clusters:
    sum{i in S} beta[i] = k;

s.t. assign_color{j in P}:
    sum{i in S} C[i, j] * beta[i] = 1;

minimize total_cost:
    sum{i in S} D[i] * beta[i];

solve;

display total_cost;

end;


