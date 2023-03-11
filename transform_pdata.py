########################################################################

import sys
import numpy
import vtk
from vtk_py import *

########################################################################

def transform_pdata(pdata, transvec, rotatevec, scalevec=[1,1,1]):

    	transform = vtk.vtkTransform()
    	transform.Translate(transvec[0],transvec[1],transvec[2])
    	transform.RotateX(rotatevec[0])
    	transform.RotateY(rotatevec[1])
    	transform.RotateZ(rotatevec[2])
    	transform.Scale(scalevec)

    	transform.Update()

	transformfilter = vtk.vtkTransformPolyDataFilter()
    	if (vtk.vtkVersion.GetVTKMajorVersion() >= 6):
		transformfilter.SetInputData(pdata)
	else:
		transformfilter.SetInput(pdata)
	transformfilter.SetTransform(transform)
	transformfilter.Update()

	return transformfilter.GetOutput()





