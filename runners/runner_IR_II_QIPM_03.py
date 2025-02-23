import os
import sys
sys.path.insert(1, os.getcwd())
from ipm import *


parameters 	= Parameters()


parameters.seed  			= int(sys.argv[1])
method 						= int(sys.argv[2])
LO_Precision 				= float(sys.argv[3])


parameters.b 				= 1
parameters.condition_number = 1

parameters.have_interior 	= False
parameters.do_print 		= False


A, b, c, _, _, _, _, _, _						= generate_problem(m=2, n=4, parameters=parameters)

model 						= Model(A, b, c)

model.Params.HHL_Method 	= 2

model.Params.Method 		= "II-QIPM" if method == 1 else "IR-II-QIPM"
model.Params.LO_Precision	= 1e-4 if method == 1 else LO_Precision
model.Params.IR_Precision 	= 1e-4

model.Params.LO_Verbosity 	= 2
model.Params.IR_Verbosity 	= 2

model.Params.Omega 			= 1e3
model.Params.Stop_Precision = 1e-3
model.Params.Stop_Cond_Num 	= 5e3
model.Params.qlsa_precision = 1e0


# model.Params.num_ancillae 	= 4
# model.Params.num_time_slices= 1
# model.Params.expansion_order= 2

# model.Params.Beta_2			= 1e-2
# model.Params.Beta_1			= 0.5

model.Params.ScalFact 		= 1e2							# Scaling factor
# model.Params.IncScalLim 	= IncScalLim




model.solve()
