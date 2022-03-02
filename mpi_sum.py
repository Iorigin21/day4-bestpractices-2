from mpi4py import MPI
import numpy as np

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

value=np.random.rand(1)

print(' Rank:', rank, 'value=',value)

value_sum = np.array(0.0,'d')
comm.Reduce(value,value_sum,op=MPI.SUM,root=0)

if rank ==0:
    print(' Rank 0: value_sum= ',value_sum)