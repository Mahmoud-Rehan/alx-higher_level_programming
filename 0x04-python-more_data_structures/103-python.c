#include <Python.h>
#include <stdio.h>


/**
 * print_python_list - Prints Python list.
 * @p: Pyobject.
 */


void print_python_list(PyObject *p)
{
	Py_ssize_t list_size;
	Py_ssize_t n;
	PyObject *object;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	list_size = PyList_Size(p);

	for (n = 0; n < list_size; n++)
	{
		object = PyList_GetItem(p, n);
		printf("Element %ld: %s\n", n, Py_TYPE(object)->tp_name);
	}
}


/**
 * print_python_bytes - Prints Python bytes object.
 * @p: Pyobject.
 */


void print_python_bytes(PyObject *p)
{
	Py_ssize_t obj_size;
	Py_ssize_t n;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	obj_size = PyBytes_Size(p);

	printf("  size: %ld\n", obj_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	printf("  first 10 bytes:");

	str = ((PyBytesObject *)p)->ob_sval;

	for (n = 0; n < obj_size && n < 10; n++)
	{
    		printf(" %02x", string[i]);
	}
	printf("\n");
}
