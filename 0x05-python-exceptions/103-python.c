#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>


void print_python_list(PyObject *p)
{
	Py_ssize_t list_size;
	Py_ssize_t n;
	PyObject *object;

	printf("[*] Python list info\n");
    
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	list_size = ((PyVarObject *)p)->ob_size;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (n = 0; n < list_size; n++)
	{
		object = PyList_GET_ITEM(p, n);
		printf("Element %ld: %s\n", n, object->ob_type->tp_name);

		if (PyBytes_Check(object))
		{
			print_python_bytes(object);
		}
		if (PyFloat_Check(object))
		{
			print_python_float(object);
		}
	}
}



void print_python_bytes(PyObject *p)
{
	Py_ssize_t obj_size = 0;
	Py_ssize_t n;
	char *str = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	obj_size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %zd\n", obj_size);
	printf("  trying string: %s\n", str);
	printf("  first %zi bytes:", obj_size < 10 ? obj_size + 1 : 10);

	for (n = 0; n < obj_size + 1 && n < 10; n++)
	{
   		printf(" %02hhx", str[n]);
	}
	printf("\n");

}


void print_python_float(PyObject *p)
{
	double d = ((PyFloatObject *)p)->ob_fval;
	char *str = NULL;

	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %.17g\n", PyFloat_AsDouble(p));
}
