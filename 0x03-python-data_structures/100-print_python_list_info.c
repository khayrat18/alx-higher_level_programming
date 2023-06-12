#include <Python.h>

/**
 */

void print_python_list_info(PyObject *p)
{
	int length;
	int i;
	int alloc
	PyObject *item;
	if(!PyList_Check(p))
	{
		printf("Not a list1");
		return;
	}

	length = Py_Size(p);
	alloc = ((PylistObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", alloc)

	for (i = 0; i < length; i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
		
}
