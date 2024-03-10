#include <Python.h>
#include <stdio.h>


void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


/**
 * print_python_list - Prints Python list.
 * @p: Pyobject.
 */


void print_python_list(PyObject *p)
{
	Py_ssize_t list_size;
	Py_ssize_t n;
	PyListObject *object;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	list_size = PyList_Size(p);
	object = (PyListObject *)p;

	for (n = 0; n < list_size; n++)
	{
		printf("Element %ld: %s\n", n, (object->ob_item[n])->ob_type->tp_name);
		if (!strcmp((object->ob_item[n])->ob_type->tp_name, "bytes"))
		{
			print_python_bytes(object->ob_item[n]);
		}
	}
}


/**
 * print_python_bytes - Prints Python bytes object.
 * @p: Pyobject.
 */


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

	if (PyBytes_AsStringAndSize(p, &str, &obj_size) != -1)
	{
		printf("  size: %ld\n", obj_size);
		printf("  trying string: %s\n", str);
		printf("  first %zi bytes:", obj_size < 10 ? size + 1 : 10);

		for (n = 0; n < obj_size && n < 10; n++)
		{
    			printf(" %02hhx", str[n]);
		}
		printf("\n");
	}
}
