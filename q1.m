
A = [2,1,1,1,0,0;
    3,1,2,0,1,0;
    1,2,4,0,0,1;];

c = [-500, -250, -600, 0, 0, 0];
b = [240; 150; 180];
cvx_begin
variables x(6)
minimize c*x
subject to
A*x == b
x>=0
cvx_end
x
cvx_optval
