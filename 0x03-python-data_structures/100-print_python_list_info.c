#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>


void print_python_list_info(PyObject *p)
{
	long int pyl_size = PyList_Size(p);
	int n;
	PyListObject *object = (PyListObject *)p;


	printf("[*] Size of the Python List = %li\n", pyl_size);
	printf("[*] Allocated = %li\n", object->allocated);

	for (n = 0; n < pyl_size; n++)
		printf("Element %i: %s\n", n, Py_TYPE(object->ob_item[n])->tp_name);
}
