#include <stdio.h>
#include <object.h>
#include <listobject.h>
#include <python.h>


void print_python_list_info(PyObject *p)
{
	PyListObject *object = (PyListObject *)p;
	long int pyl_size = PyList_Size(p);
	int n;

	printf("[*] Size of the Python List = %li\n", pyl_size);
	printf("[*] Allocated = %li\n", object->allocated);

	for (n = 0; n < pyl_size; n++)
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[n])->tp_name);
}
