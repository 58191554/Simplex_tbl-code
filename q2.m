A = [-2,-0,1,9,1,0;
    1/3,1,-1/3,-2,0,1];

c = [-2, -3, 1, 12, 0, 0];

cvx_begin
variables x(6)
minimize c*x

subject to 
A*x == 0
x >= 0

cvx_end

x

cvx_optval
