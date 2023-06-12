#include <Python.h>

/**
 * print_python_list_info - C function that prints basic py list
 * @p: pointer to structure
 */

void print_python_list_info(PyObject *p)
{
	int length;
	int i;
	int alloc;
	PyObject *item;


	length = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < length; i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}

}
